from General import Node

#Closed list couldn't be implemented as a set for fast access as order doesn't matter to check repeated STATES (not nodes) because of python error 
closed_list = []
#Frontier implemented as list that will be manipulated as stack or queue depending on the strategy
frontier = []


#General search algorithm that is strategy independant
def general_search(problem, strategy, heuristic):
  expanded_cnt = 0
  in_closedlist_cnt = 0
  #Create and Insert Initial Node in the frontier according to strategy
  initial_node = problem.initial_state
  add_frontier(initial_node, strategy, heuristic, problem)
  #Continuously loop until you find solution set to limit
  limit = eval(input("Please set a limit for the search: "))
  keep_going = 'y'
  while(keep_going == 'y'):
    cnt = 0
    while(cnt <= limit):
      #If there is nothing left in the frontier we did not find a solution
      if frontier == []:
        print("No Solution.")
        return "failure"
      #Remove node from fringe to check if goal according to strategy
      n = remove_frontier(strategy)
      print("Our new popped node is: ", n.state)
      #Check if n is a goal state by seeing if it exists in the set goal_test that contain goal state(s)
      if n.state in problem.goal_test:
        print("""
        ----------------------
        """)
        print("We found a goal")
        print("To reach the goal we had to expand", expanded_cnt, "nodes")
        print("Before expanding the popped nodes we found ", in_closedlist_cnt, " already visited nodes" )
        return n
      #Check if n state was visited before if not then expand it
      if n.state in closed_list:
        print("Already Visited")
        in_closedlist_cnt += 1
        print("The number of loops so far is: ", in_closedlist_cnt)
      else:
        closed_list.append(n.state)
        expanded_cnt += 1
        print("The number of nodes expanded so far is: ", expanded_cnt)
        expand_node(n, problem, strategy, heuristic)
      cnt = cnt + 1
    
    keep_going = input("Do you want to keep going (y/n): ")
    if keep_going == 'n':
      #Report the search info and terminate the search
      print("Up to this point we had to expand", expanded_cnt, "nodes")
      print("Before expanding the popped nodes we found ", in_closedlist_cnt, " already visited nodes" )
      break
    #Give the possibility of changing the limit
    new_limit = input("Do you want to set a new limit? (y/n): ")
    if(new_limit == 'y'):
      limit = eval(input("Please set a limit for the search: "))
  
    

  
#Function that adds node to frontier according to strategy
def add_frontier(node, strategy, heuristic, problem):

  #DFS Uses Stack and BFS Uses Queue append for both to add
  if(strategy == 1 or strategy == 2):
    frontier.append(node)
  #Greedy Use priority queue based on heuristic value
  elif(strategy == 3):
    if frontier == []:
      frontier.append(node)
    else:
      cnt = 0
      while(cnt < len(frontier)):
        if heuristic == "misplaced_tiles":
          if(problem.misplaced_tiles(frontier[cnt]) < problem.misplaced_tiles(node)):
            break
          else:
            cnt = cnt + 1
        elif heuristic == "manhattan_distance":
          if(problem.manhattan_distance(frontier[cnt]) < problem.manhattan_distance(node)):
            break
          else:
            cnt = cnt + 1
        elif heuristic == "trips_with_return":
          if(problem.trips_with_return(frontier[cnt]) < problem.trips_with_return(node)):
            break
          else:
            cnt = cnt + 1
        elif heuristic == "trips_without_return":
          if(problem.trips_without_return(frontier[cnt]) < problem.trips_without_return(node)):
            break
          else:
            cnt = cnt + 1
        elif heuristic =="isolated_pegs":
          if(problem.isolated_pegs(frontier[cnt]) < problem.isolated_pegs(node)):
            break
          else:
            cnt = cnt + 1
        elif heuristic == "custom_heuristic":
          if(problem.custom_heuristic(frontier[cnt]) < problem.custom_heuristic(node)):
            break
          else:
            cnt = cnt + 1
      frontier.insert(cnt, node)
  #A* Use priority queue based on path cost + heuristic value
  elif(strategy == 4):
    if frontier == []:
      frontier.append(node)
    else:
      cnt = 0
      while(cnt < len(frontier)):
        if heuristic == "misplaced_tiles":
          if((frontier[cnt].path_cost + problem.misplaced_tiles(frontier[cnt])) < (node.path_cost + problem.misplaced_tiles(node))):
            break
          else:
            cnt = cnt + 1
        if heuristic == "manhattan_distance":
          if((frontier[cnt].path_cost + problem.manhattan_distance(frontier[cnt])) < (node.path_cost + problem.manhattan_distance(node))):
            break
          else:
            cnt = cnt + 1
        elif heuristic == "trips_with_return":
          if((frontier[cnt].path_cost + problem.trips_with_return(frontier[cnt])) < (node.path_cost + problem.trips_with_return(node))):
            break
          else:
            cnt = cnt + 1
        elif heuristic == "trips_without_return":
          if((frontier[cnt].path_cost + problem.trips_without_return(frontier[cnt])) < (node.path_cost + problem.trips_without_return(node))):
            break
          else:
            cnt = cnt + 1
        elif heuristic =="isolated_pegs":
            if((frontier[cnt].path_cost +  problem.isolated_pegs(frontier[cnt])) < (node.path_cost + problem.isolated_pegs(node))):
              break
            else:
             cnt = cnt + 1
        elif heuristic =="custom_heuristic":
            if((frontier[cnt].path_cost +  problem.custom_heuristic(frontier[cnt])) < (node.path_cost + problem.custom_heuristic(node))):
              break
            else:
             cnt = cnt + 1
      frontier.insert(cnt, node)
  

#Function that removes node from frontier according to strategy
def remove_frontier(strategy):
  #With DFS we pop from end (Stack)
  if(strategy == 1):
    return frontier.pop()
  #With BFS we pop from start (Queue)
  elif(strategy == 2):
    return frontier.pop(0)
  #With A* and Greedy we ordered in descending order and we pop node with lowest value
  elif(strategy == 3 or strategy ==4):
    return frontier.pop()

#Define expand_node function that expands node and puts successors in the frontier
def expand_node(node, problem, strategy, heuristic):
  #Get the possible (state, action) pairs resulting from applying the successor function on our node
  successor_list = problem.successor_function(node)
  for x in successor_list:
    print(x)
  #For each pair create a new node that will be added to the frontier
  for pair in successor_list:
    st = pair[0]
    act = pair[1]
    new_node = Node(st, node, act, node.depth + 1, 0)
    #Function path_cost_function adds edge cost to parent node cost
    new_node.path_cost = problem.path_cost_function(new_node)
    #Add new successor node to frontier according to strategy
    add_frontier(new_node, strategy, heuristic,problem)
  #Reporting how the frontier works to be able to assess heuristics
  print("Frontier after expansion is")
  for i in frontier:
    print(i.state)