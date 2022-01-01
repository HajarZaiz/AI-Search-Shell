from General import General_problem

class MissionariesAndCannibals(General_problem):

  #Constructor
  def __init__(self, missionaries_goal_test, missionaries_initial_state, missionaries_operators):
    self.initial_state = missionaries_initial_state
    self.operators = missionaries_operators
    self.goal_test = missionaries_goal_test

  def successor_function(self, node):
    successors = []
    for i in self.operators:
      result_node = []
      #If boat was initially on the wrong side
      if node.state[2] == 1:
        #Apply the operator
        result_node.append(node.state[0] - i[0])
        result_node.append(node.state[1] - i[1])
        #Set the boat to be on the right side
        result_node.append(0)
      #If boat was initially on the right side
      elif node.state[2] == 0:
        #Apply the operator
        result_node.append(node.state[0] + i[0])
        result_node.append(node.state[1] + i[1])
        #Set the boat to be on the wrong side
        result_node.append(1)

      #Filter out non valid actions
      #First remove all actions where we have more than 3 cannibals or missionaries, also cannot be less than 0
      if(result_node[0] <= 3 and result_node[1] <= 3 and result_node[0] >= 0 and result_node[1] >= 0):
        #Number of Cannibals [1] should be not exceed the number of missionaries [0]
        if(result_node[0] >= result_node[1] or result_node[0] == 0):
          if (result_node[0] == 1 and result_node[1] == 0) or (result_node[0] == 2 and result_node[1] == 1) or (result_node[0] == 2 and result_node[1] == 0):
            #Do Nothing since these states will result in leaving cannibals exceeding missionarie on other side
            pass
          else:
            #Legal action
            pair = (result_node, i)
            successors.append(pair)
    return successors
  
  #Cost with each move is 1 so path cost is parent cost + 1
  def path_cost_function(self, node):
    extra_cost = 1
    return extra_cost + node.parent_node.path_cost

  #This heuristic describes the number of people on the left side assuming that one person has to come back in the boat to the starting side. In other words, it assumes that going back and fourth only one person at most is transfered to the right side.
  def trips_with_return(self, node):
    return node.state[0] + node.state[1] - 1
  
  #This heuristic doesn't take into consideration one cannibal/missionary coming back to the starting side and divides the number of Cannibals and Missionaries on the left side by the boat capacity which is 2 to determine the number of trips
  def trips_without_return(self, node):
    return (node.state[0] + node.state[1])/2

