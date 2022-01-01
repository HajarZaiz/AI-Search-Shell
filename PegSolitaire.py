from General import General_problem

class PegSolitaire(General_problem):

  #Constructor
  def __init__(self, peg_goal_test, peg_initial_state, peg_operators):
    self.initial_state = peg_initial_state
    self.operators = peg_operators
    self.goal_test = peg_goal_test

  def successor_function(self, node):
    successors = []
    for x in range(0, len(node.state)):
      #if the position contains a peg
      if node.state[x] == 1:
        for i in self.operators:
          result_node = node.state[:]
          # if operator is "jump up", and we are in the third row or bellow (we cannot jump up from 1st and 2nd rows), and the above cell contains a peg, and the cell above them is blank we can jump up
          if i == "ju" and  x >= 14 and node.state[x-14]==2 and node.state[x-7]==1:
                result_node[x-14] = 1
                result_node[x-7] = 2
                result_node[x] = 2
                pair = (result_node, (i,x))
                successors.append(pair)
          #Similarly we eliminate for jd jr and jl
          elif i == "jd" and x<=34 and node.state[x+14] == 2 and node.state[x+7] == 1:
                result_node[x+14] = 1
                result_node[x+7] = 2
                result_node[x] = 2
                pair = (result_node, (i,x))
                successors.append(pair)
          elif i == "jr" and x%7 < 5 and node.state[x+2] == 2 and node.state[x+1] == 1:
                result_node[x+2] = 1
                result_node[x+1] = 2
                result_node[x] = 2
                pair = (result_node, (i,x))
                successors.append(pair)
          elif i == "jl" and x%7 > 1 and node.state[x-2] == 2 and node.state[x-1] == 1:
                result_node[x-2] = 1
                result_node[x-1] = 2
                result_node[x] = 2
                pair = (result_node, (i,x))
                successors.append(pair)
    return successors

  #Cost with each move is 1 so path cost is parent cost + 1
  def path_cost_function(self, node):
    extra_cost = 1
    return extra_cost + node.parent_node.path_cost

  #This heuristic checks the number of pegs that are isolated and have no neighbors
  def isolated_pegs(self, node):
    sum = 0
    for x in range(0, len(node.state)):
      if node.state[x] == 1:
        #For top pegs on the top cells do not check the top neighboor as it doesn't exist
        if x == 2 or x == 3 or x == 4:
          if node.state[x-1] != 1 and node.state[x+1] != 1 and node.state[x+7] != 1:
            sum = sum +1
        #For top pegs on the left cells do not check the left neighboor as it doesn't exist
        elif x == 14 or x == 21 or x == 28:
          if node.state[x-7] != 1 and node.state[x+1] != 1 and node.state[x+7] != 1:
            sum = sum +1
        #For top pegs on the right cells do not check the right neighboor as it doesn't exist
        elif x == 27 or x == 34 or x == 20:
          if node.state[x-1] != 1 and node.state[x-7] != 1 and node.state[x+7] != 1:  
            sum = sum +1 
        #For top pegs on the bottom cells do not check the bottom neighboor as it doesn't exist
        elif x == 44 or x == 45 or x == 46:
          if node.state[x-1] != 1 and node.state[x+1] != 1 and node.state[x-7] != 1:  
            sum = sum +1
        #Otherwise check all four neighbours
        else:
          if node.state[x-1] != 1 and node.state[x+1] != 1 and node.state[x+7] != 1 and  node.state[x-7] != 1:
              sum = sum +1 
    return sum