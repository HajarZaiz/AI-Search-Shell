from General import General_problem

class EightPuzzle(General_problem):

  #Constructor
  def __init__(self, eightpuzzle_goal_test, eighpuzzle_initial_state, eightpuzzle_operators):
    self.initial_state = eighpuzzle_initial_state
    self.operators = eightpuzzle_operators
    self.goal_test = eightpuzzle_goal_test

  def successor_function(self, node):
    successors = []
    #for each operator
    for i in self.operators:
      #Make copy of the node state
      result_node = node.state[:]
      #If the operator moves the blank up
      if i == "u":
        #Get index of blank
        index_blank = result_node.index(" ")
        #When up move is valid the blank should not be in the first row
        if index_blank != 0 and index_blank != 1 and index_blank != 2:
          #Get index of element on top
          index_swap = index_blank - 3
          #Swap
          temp = result_node[index_blank]
          result_node[index_blank] = result_node[index_swap]
          result_node[index_swap] = temp
          #Return as successor
          pair = (result_node, i)
          successors.append(pair)
      #If the operator moves the blank down
      elif i == "d":
        #Get index of blank
        index_blank = result_node.index(" ")
        #When down move is valid the blank should not be in the last row
        if index_blank != 6 and index_blank != 7 and index_blank != 8:
          #Get index of element at bottom
          index_swap = index_blank + 3
          #Swap
          temp = result_node[index_blank]
          result_node[index_blank] = result_node[index_swap]
          result_node[index_swap] = temp
          #Return as successor
          pair = (result_node, i)
          successors.append(pair)
      #If the operator moves the blank right
      elif i == "r":
        #Get index of blank
        index_blank = result_node.index(" ")
        #When right move is valid the blank should not be in the last column
        if index_blank != 2 and index_blank != 5 and index_blank != 8:
          #Get index of element at bottom
          index_swap = index_blank + 1
          #Swap
          temp = result_node[index_blank]
          result_node[index_blank] = result_node[index_swap]
          result_node[index_swap] = temp
          #Return as successor
          pair = (result_node, i)
          successors.append(pair)
      #If the operator moves the blank left
      elif i == "l":
        #Get index of blank
        index_blank = node.state.index(" ")
        #When left move is valid the blank should not be in the first column
        if index_blank != 0 and index_blank != 3 and index_blank != 6:
          #Get index of element at bottom
          index_swap = index_blank - 1
          #Swap
          temp = result_node[index_blank]
          result_node[index_blank] = result_node[index_swap]
          result_node[index_swap] = temp
          #Return as successor
          pair = (result_node, i)
          successors.append(pair)
    return successors

  #Cost with each move is 1 so path cost is parent cost + 1
  def path_cost_function(self, node):
    extra_cost = 1
    return extra_cost + node.parent_node.path_cost

  #Heuristic that returns the number of misplaced tiles in a given configuration
  def misplaced_tiles(self,node):
      misplaced = 0
      for j in range(0, 9):
        #We should not count if the blank is in a misplaced position
        if node.state[j] == " " and self.goal_test[0][j] != " ":
          pass
        elif node.state[j] != " " and self.goal_test[0][j] == " ":
          pass
        #Add one if tile is in wrong position
        elif node.state[j] != self.goal_test[0][j]:
          misplaced = misplaced + 1
        
      return misplaced

  #Heuristic that returns the sum of horizontal + vertical distances from the accurate position for each tile
  def manhattan_distance(self, node):
    sum = 0
    for i in range(0, 9):
      g = self.goal_test[0][i]
      idx_t = node.state.index(g)
      #How vertically far
      y = abs(idx_t//3 - i//3)
      #How horizontally far
      x = abs(idx_t%3 - i%3)
      sum += x+y
    return sum

  #This heuristic in addition to the manhattan distance takes into consideration the tiles that should be moved out of the way to remove conflicts(more explanation in the documentation)
  def custom_heuristic(self, node):
    #this function returns the number of tiles that must be removed from a list (row,column) to remove all conflicts
    def count (state_list, goal_list, lc):
      #for each element in state_list(a row or a column of the puzzle), cn keeps track of the number of conflicts it has
      cn = [0, 0, 0]
      #first we check if the element is in the same line(row/column) as its goal state
      for i in state_list:
        if i in goal_list and i!= " ":
          for j in state_list:
            if j in goal_list and j!= " ":
              #Should only proceed to check conflict with tiles different than the current one
              if i!=j:
                # Tj and Ti are in conflict if Ti should move right to meet its goal state and Tj is at its right. And Tj should move left to reach its goal state
                if goal_list.index(i) > goal_list.index(j) and state_list.index(i)<state_list.index(j):
                  cn[state_list.index(i)] += 1
                # Tj and Ti are in conflict also if the situation is opposite to the previous one (Ti should go left and tj should go right)
                if goal_list.index(i) < goal_list.index(j) and state_list.index(i)>state_list.index(j):
                  cn[state_list.index(i)] += 1 
      #at this stage we have achieved to count number of conflicts of each elemnt on the list  
      #we stop only if no conflicts are left
      #lc is the number of tiles to be removed (we multiply it by two bcz removing a tile will add two steps one to remove it, and one to be added to its manhattan distance since we made it further from its goal state by one step)
      if max(cn) == 0:
        return lc * 2
      #if there are conflicts we remove the tile with the maximum numb of conflicts
      #To remove a tile of the way we just replace it with a value out of range(0-8), we update number of tiles to be removed by one, and we call the function again until no conflicts are left   
      else:
        state_list[cn.index(max(cn))] = 19
        lc += 1
        return count(state_list, goal_list, lc)
    

    # The function custom_heuristic:
    LC=0
    #Counting number of tiles that must be removed from each row
    # we just iterate over all rows and call function count on each one
    for i in range(0, 7, 3):
      row = [node.state[i], node.state[i+1], node.state[i+2]]
      goal_row = [self.goal_test[0][i], self.goal_test[0][i+1], self.goal_test[0][i+2]]
      LC += count(row, goal_row, 0)
    #Counting number of tiles that must be removed from each column
     # we just iterate over all columns and call function count on each one
    for j in range(0,3):
      col = [node.state[j], node.state[j+3], node.state[j+6]]
      goal_col = [self.goal_test[0][j], self.goal_test[0][j+3], self.goal_test[0][j+6]] 
      LC += count(col, goal_col, 0)
  
  
    return LC + self.manhattan_distance(node)







  
  