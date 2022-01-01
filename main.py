from General import Node
from GeneralSearch import general_search
from EightPuzzle import EightPuzzle
from PegSolitaire import PegSolitaire
from Missionaries import MissionariesAndCannibals

#Menu prompting the user to select a puzzle
def menu1():
  print("""
  1- Peg Solitaire
  2- 8-Puzzle
  3- Missionaries and Cannibals
  """)

#Menu prompting the user to select a search strategy
def menu2():
  print("""
  1- Depth-First
  2- Breadth-First
  3- Greedy-Best First
  4- A*
  """)

#Menu prompting the user to select a heuristic for 8-puzzle
def eightpuzzle_menu ():
  print("Select a heuristic")
  print("""
  1- Displaced Tiles
  2- Manhattan Distance
  3- Custom
  """)

#Menu prompting the user to select a heuristic for Missionaries and Cannibals
def missionaries_menu ():
  print("Select a heuristic")
  print("""
  1- Trips with return
  2- Trips without return
  """)

#Used to print peg solitaire state in a cute way
def print_peg (state):
  print("-------------------------")
  for i in range(len(state)):
    if state[i] == 0:
      print("    ", end = '')
    elif state[i] == 1:
      print(" O  ", end='')
    else:
      print(" *  ", end='')
    if i%7 == 6:
      print("\n")
    
  print("-------------------------")

#Used to print eight puzzle state in a cute way
def print_eightpuzzle(state):
  print("----------")
  for i in range (len(state)):
    print(state[i], "  ", end='')
    if i == 2 or i == 5 or i == 8:
      print("\n")
  print("----------")
#------------------------------------------------------
#DEFAULT PARAMETERS
#Initially 3 cannibals and 3 missionaries are on the wrong side and  the boat is also on the wrong side
missionaries_initial_state = Node([3, 3, 1], None, None, 0, 0)
missionaries_operators = {
  (2, 0, 1),
  (0, 1, 1),
  (1, 0, 1),
  (0, 2, 1),
  (1, 1, 1)
}
missionaries_goal_test = [[0, 0, 0]]

#------------------------------------------------------

#For, the 8-puzzle, We can have multiple initial states therefore we will prompt the user for input
def eightpuzzle_initial_input():
    eightpuzzle_initial_state = []
    print("Input values from 1-8 and a space for the blank for start state")
    for i in range(0,9):
      x = input("enter value :")
      eightpuzzle_initial_state.append(x)
    return eightpuzzle_initial_state

#The goal test can also vary in terms of the position of the blank, so we prompt the user for it too
def eightpuzzle_goal_input():
  eightpuzzle_goal = []
  print("Input values from 1-8 and a space for the blank for goal state")
  for i in range(0,9):
      x = input("Enter value :")
      eightpuzzle_goal.append(x)  
  return eightpuzzle_goal

#Blank can move up down right left
eightpuzzle_operators = {
  "u",
  "d",
  "r",
  "l"
}

#--------------------------------------------------
#Peg Solitaire
#DEFAULT PARAMETERS
#0 is for unused 1 for peg and 2 for empty space

#We can have multiple initial states therefore we will prompt the user for input
def peg_initial_input():
    peg_initial_state = []
    print("""
    Input 49 values as follows:
    --> Enter 1 for Peg
    --> Enter 2 for Hole
    --> Enter 0 for invalid positions that should not be used

    For instance the goal position is represented as follows: 
    [
      0, 0, 2, 2, 2, 0, 0,
      0, 0, 2, 2, 2, 0, 0,
      2, 2, 2, 2, 2, 2, 2,
      2, 2, 2, 1, 2, 2, 2,
      2, 2, 2, 2, 2, 2, 2,
      0, 0, 2, 2, 2, 0, 0,
      0, 0, 2, 2, 2, 0, 0
    ]

    Please proceed at inputting an initial state: 

    """)
    for i in range(0,49):
      x = eval(input("enter value :"))
      peg_initial_state.append(x)
    return peg_initial_state

#You can comment this initial state and uncomment the following one to actually get a solution in short time

#The last peg should end up in the center position that is empty at the start of the game.
peg_goal_test = [[
  0, 0, 2, 2, 2, 0, 0,
  0, 0, 2, 2, 2, 0, 0,
  2, 2, 2, 2, 2, 2, 2,
  2, 2, 2, 1, 2, 2, 2,
  2, 2, 2, 2, 2, 2, 2,
  0, 0, 2, 2, 2, 0, 0,
  0, 0, 2, 2, 2, 0, 0
]]


#Each peg can jump over left right up down
peg_operators = {
  "ju",
  "jd",
  "jr",
  "jl"
}
#------------------------------------------------------
#GETTING INPUT FROM THE USER

#Keep promting the user if they give you an invalid puzzle number
choice1 = 0
while(choice1 != 1 and choice1 != 2 and choice1!= 3):
  menu1()
  choice1 = eval(input("Please Select A Puzzle: "));


#Keep promting the user if they give you an invalid puzzle number
choice2 = 0
while(choice2 != 1 and choice2 != 2 and choice2!= 3 and choice2 != 4):
  menu2()
  choice2 = eval(input("Please Select A Search Strategy: "));

#Organizing code
if choice1 == 3:
  testm = MissionariesAndCannibals(missionaries_goal_test, missionaries_initial_state, missionaries_operators)
  if choice2 == 1:
    solution = general_search(testm, 1, "None")
  elif choice2 == 2:
    solution = general_search(testm, 2, "None")
  elif choice2 == 3:
    missionaries_menu()
    heuristic = eval(input("Choose a heuristic:"))
    if heuristic == 1:
      solution = general_search(testm, 3, "trips_with_return")
    elif heuristic == 2:
      solution = general_search(testm, 3, "trips_without_return")
  elif choice2 == 4:
    missionaries_menu()
    heuristic = eval(input("Choose a heuristic:"))
    if heuristic == 1:
      solution = general_search(testm, 4, "trips_with_return")
    elif heuristic == 2:
      solution = general_search(testm, 4, "trips_without_return")
elif choice1 == 2:
  eighpuzzle_initial_state = Node(eightpuzzle_initial_input(), None, None, 0, 0)
  eightpuzzle_goal_test = [eightpuzzle_goal_input()]
  testm = EightPuzzle(eightpuzzle_goal_test, eighpuzzle_initial_state, eightpuzzle_operators)
  if choice2 == 1:
    solution = general_search(testm, 1, "None")
  elif choice2 == 2:
    solution = general_search(testm, 2, "None")
  elif choice2 == 3:
    eightpuzzle_menu()
    heuristic = eval(input("Choose a heuristic:"))
    if heuristic == 1:
      solution = general_search(testm, 3, "misplaced_tiles")
    elif heuristic == 2:
      solution = general_search(testm, 3, "manhattan_distance")
    elif heuristic == 3:
      solution = general_search(testm, 3, "custom_heuristic")
  elif choice2 == 4:
    eightpuzzle_menu()
    heuristic = eval(input("Choose a heuristic:"))
    if heuristic == 1:
      solution = general_search(testm, 4, "misplaced_tiles")
    elif heuristic == 2:
      solution = general_search(testm, 4, "manhattan_distance")
    elif heuristic == 3:
      solution = general_search(testm, 4, "custom_heuristic")
elif choice1 == 1:
  peg_initial_state = Node(peg_initial_input(), None, None, 0, 0)
  testm = PegSolitaire(peg_goal_test, peg_initial_state, peg_operators)
  if choice2 == 1:
    solution = general_search(testm, 1, "None")
  elif choice2 == 2:
    solution = general_search(testm, 2, "None")
  elif choice2==3:
    solution = general_search(testm, 3, "isolated_pegs")
  elif choice2==4:
    solution = general_search(testm, 4, "isolated_pegs")


#Printing the solution:
if solution:
  i = solution
  if i != "failure":
    path = []
    while(i != testm.initial_state):
      path.append(i)
      i = i.parent_node
    path.append(i)
    print("The cost of the solution is", solution.path_cost)
    print("The path to the solution is: ")
    if choice1 == 1:
      for j in range(len(path)-1, -1,-1):
        print_peg(path[j].state)
    elif choice1 == 2:
      for j in range(len(path)-1, -1,-1):
        print_eightpuzzle(path[j].state)
    elif choice1 == 3:
      for j in range (len(path)-1, -1, -1):
        print(path[j].state)


else:
  print("Search process was terminated")

    






