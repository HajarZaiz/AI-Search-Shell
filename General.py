#Node Representation
class Node:

  #Constructor
  def __init__(self, state, parent_node, operator, depth, path_cost):
    self.state = state
    self.parent_node = parent_node
    self.operator = operator
    self.depth = depth
    self.path_cost = path_cost

  

#Problem Formulation
class General_problem:

  #Constructor
  def __init__(self, initial_state, operators, goal_test):
    self.initial_state = initial_state
    self.operator = operators  #List of available operators
    self.goal_test = goal_test
    self.path_cost = 0 #initial path cost always 0

  #Define General Successor Function that takes a node and returns (state, action) pairs possible resulting
  def successor_function(self, node):
    successors = [];
    return successors
  
  #Define General Cost Function that whenever we expand a node it updates its cost by adding the edge cost
  def path_cost_function(self, node):
    extra_cost = 0
    #Given a file name such us pathcosts
    text_name = input("Please Enter your file name: ")
    text_name = text_name +".txt"
    f = open(text_name, 'r')
    for i in f:
      #for each line in the file
      line = i.split()
      #read the distance between the node and its parent node line[2]
      if (line[0] == node.parent_node.state and line[1] == node.state) or (line[1] == node.parent_node.state and line[0] == node.state):
        extra_cost = int(line[2])
        break
    #add the cost of getting to that state from the previous state to the total path cost leading to the parent node
    return extra_cost + node.parent_node.path_cost
