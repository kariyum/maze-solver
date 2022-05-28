import random
from random import shuffle, randrange
import sys
from tracemalloc import start
from colorama import Fore, Back, Style
from colorama import init
import os
import time
SPEED = 0.1

clear = lambda: os.system('cls')
init()

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.up = 1 # UP
        self.right = 1 # UP
        self.down = 1 # UP
        self.left = 1 # UP
        self.visited = 0
        self.weight = 1
    
    def __str__(self):
        # ch = "(" + str(self.x) + ", " + str(self.y) + ")" + " Up: " + str(self.up) + " Right: " + str(self.right) + " Down: " + str(self.down) + " Left: " + str(self.left) + " Visited: " + str(self.visited)
        ch = "(" + str(self.x) + ", " + str(self.y) + ")" 
        return ch

class Maze:
    def __init__(self, sx, sy):
        self.sx = sx
        self.sy = sy
        self.map = [ [Cell(i,j) for j in range(sx)] for i in range(sy) ]
        self.occupation = [ [self.map[i][j].visited for j in range(self.sx)] for i in range(self.sy)]
    def __str__(self):
        print("Maze: ")
        ch = ""
        for i in range(self.sy):
            for j in range(self.sx):
                ch = ch + "(" + str(i)+", "+ str(j)+") "
            ch = ch + '\n'
        return ch
    def visitedCells(self):
        self.occupation = [ [self.map[i][j].visited for j in range(self.sx)] for i in range(self.sy)]
        print("Visited cells:")
        ch = ""
        for row in self.occupation:
            for cell in row:
                ch = ch + str(cell) + " "
            ch = ch + '\n'
        return ch
    def constructMaze(self, seed=0):
        if (seed != 0):
            random.seed(seed)
        # Select a randomly not visited cell
        x1 = int(random.random() * self.sx)
        y1 = int(random.random() * self.sy)
        # ----> cell = self.map[x1][y1]

        # Select a randomly not visited cell
        x2 = int(random.random() * self.sx)
        y2 = int(random.random() * self.sy)
        # ----> cell = self.map[x2][y2]

        # Trace a path between the chosen cells from C1 to C2
        # Each time choose a direction and move one step until C2
        # Constraint 0<= x < sx AND 0<= y < sy
        print("Starting points: ")
        print(self.map[x1][y1])
        print(self.map[x2][y2])
        # print(x1==x2 and y1==y2)
        print("Path hunting !")
        while not (x1==x2 and y1==y2):
            if (True):
                if ( x1 < x2 ):
                    self.map[x1][y1].down = 0 # Right wall down WRONG! 
                    self.map[x1+1][y1].up = 0 # Left wall down
                    self.map[x1][y1].visited = 1
                    self.map[x1+1][y1].visited = 1
                    x1+=1
                elif ( x1 > x2):
                    self.map[x1][y1].up = 0 # Left wall down
                    self.map[x1-1][y1].down = 0 # Right wall down
                    self.map[x1][y1].visited = 1
                    self.map[x1-1][y1].visited = 1
                    x1-=1
                elif ( y1 < y2):
                    self.map[x1][y1].right = 0 # Lower wall down
                    self.map[x1][y1+1].left = 0 # Upper wall down
                    self.map[x1][y1].visited = 1
                    self.map[x1][y1+1].visited = 1
                    y1+=1
                elif ( y1 > y2):
                    self.map[x1][y1].left = 0 # Upper wall down
                    self.map[x1][y1-1].right = 0 # Lower wall down
                    self.map[x1][y1].visited = 1
                    self.map[x1][y1-1].visited = 1
                    y1-=1
            
    def countWallsDown(self, i, j):
        return 4 - (self.map[i][j].up + self.map[i][j].down + self.map[i][j].right + self.map[i][j].left)
    def graphicMaze(self):
        
        # Print upper walls first
        # --> Left Space Right walls
        # --> Lower walls
        # Repeat.
        for row in self.map:
            upper_string = ""
            middle_string = ""
            lower_string = ""
            for cell in row:
                # Upper walls
                if (cell.up == 1):
                    upper_string += '+---+ '
                else:
                    upper_string += '+   + '
                
                # Middle walls
                if (cell.left == 1):
                    middle_string += '|   '
                    if (cell.right == 1):
                        middle_string += '| '
                    else:
                        middle_string+= '  ' 
                else:
                    middle_string += '    '
                    if (cell.right == 1):
                        middle_string += '| '
                    else:
                        middle_string += '  '
                # Lower walls
                if (cell.down == 1):
                    lower_string += '+---+ '
                else:
                    lower_string += '+   + ' #contour

            print(upper_string)
            print(middle_string)
            print(lower_string)
    def graphicMazeV2(self, translated = 0):
        print('\n')
        for row,i in zip(self.map, range(len(self.map))):
            upper_string = ""
            middle_string = ""
            lower_string = ""
            for cell,j in zip(row,range(len(row))):
                # Upper walls
                if (cell.up == 1):
                    upper_string += '+---'
                else:
                    upper_string += '+   '
                if (j == len(row)-1):
                    upper_string += '+'
                # Middle walls
                if (cell.left == 1):
                    if (cell.visited) : 
                        middle_string += '|   '
                    else:
                        middle_string += '|   '
                    if (cell.right == 1 and j==len(row)-1):
                        middle_string += '|'
                    else:
                        middle_string+= '' 
                else:
                    if (cell.visited) :
                        middle_string += '   '
                    else:
                        middle_string += '   '
                    if (cell.right == 1 and j==len(row)-1):
                        middle_string += ' |'
                    else:
                        middle_string += ' '
                # Lower walls
                if (cell.down == 1):
                    lower_string += '+---'
                else:
                    lower_string += '+   ' #contour
                if (j==len(row)-1):
                    lower_string+= '+'
            if (not translated):
                print(upper_string)
                print(middle_string)
                if (i == len(self.map)-1):
                    print(lower_string)
            else:
                printPos(i*2+3, 80, Fore.WHITE + upper_string)
                printPos(i*2+4, 80, Fore.WHITE + middle_string)
                if (i == len(self.map)-1):
                    printPos(i*2+5, 80, Fore.WHITE + lower_string)
    def constructMazeV2(self):
        # Iterate on all cells and choose some walls to break
        for row,i in zip(self.map, range(len(self.map))):
            for cell,j in zip(row, range(len(row))):
                d = int(random.random() * 4)
                # d=0 -> top
                # d=1 -> right
                # d=2 -> bottom
                # d=3 -> left
                if (d==0):
                    if (cell.x != 0 and self.countWallsDown(i,j)<3 and self.countWallsDown(i-1,j)<3):
                        # Remove upper wall for this cell and lower wall for the upper one
                        self.map[i][j].up = 0
                        self.map[i-1][j].down = 0
                        # self.map[i][j].visited = 1
                        # self.map[i-1][j].visited = 1
                elif (d==1 and self.countWallsDown(i,j)<3):
                    if (cell.y != len(row)-1):
                        if (self.countWallsDown(i,j+1)<3):
                            cell.right = 0  
                            self.map[i][j+1].left = 0
                            # cell.visited = 1
                            # self.map[i][j+1].visited = 1
                elif (d==2):
                    if (cell.x != len(self.map)-1):
                        cell.down = 0
                        self.map[i+1][j].up = 0
                elif (d==3):
                    if (cell.y != 0):
                        cell.left = 0
                        self.map[i][j-1].right = 0
    def constructMazeV3(self):
        w = self.sx
        h = self.sy
        visited = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
        ver = [["|   "] * w + ['|'] for _ in range(h)] + [[]]
        hor = [["+---"] * w + ['+'] for _ in range(h + 1)]
    
        def walk(x, y):
            visited[y][x] = 1 # self.map[y][x].visited = 1
            # self.map[y][x].visited = 1
            operations_possibles = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(operations_possibles)
            for (xx, yy) in operations_possibles:
                if visited[yy][xx]: continue
                if xx == x: # Same column --> remove wall between two lines
                    hor[max(y, yy)][x] = "+   "
                    # My changes
                    if (yy>=0):
                        if (y>yy): # Going down
                            self.map[y][x].up = 0
                            self.map[yy][x].down = 0
                        else:
                            self.map[yy][x].up = 0
                            self.map[y][x].down = 0
                    else:
                        continue
                if yy == y: 
                    ver[y][max(x, xx)] = "    "
                    # My changes
                    if (xx>=0):
                        if (x>xx): # Going left
                            self.map[y][x].left = 0
                            self.map[y][xx].right = 0
                        else:
                            self.map[y][xx].left = 0
                            self.map[y][x].right = 0
                    else:
                        continue
                walk(xx, yy)
        walk(randrange(w), randrange(h))
    
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return s
    def left_firstSearch(self):
        # Parcours de labyrinth gauche au début
        # Mouvement possible: top (x+1, y), right (x, y+1), down (x+1, y), left (x-1, y)
        stack = list()
        lookingAt = 1 # 0 Nord, 1 East, 2 South, 3 West
        # Priority : LEFT STRAIGHT RIGHT BACK
        dict = {
            0 : [ (-1, 0), (0, 1), (1, 0), (0, -1)], # straight, right, back, left 
            1 : [ (0, 1), (1, 0), (0, -1), (-1, 0) ],
            2 : [ (1, 0), (0, -1), (-1, 0), (0, 1)],
            3  : [(0,-1), (-1, 0), (0, 1), (1, 0)]
        }

        def walk(x, y, lookingAt):
            # Try left
            drawAt(x, y)
            xx = x + dict[lookingAt][0][0] # set -1 for left
            yy = y + dict[lookingAt][0][1]
            if (yy==y): # Same column 
                if (lookingAt == 1):
                    # going up
                    if (self.map[xx][y].down==0 and self.map[x][y].up==0 ):
                        drawAt(xx, yy, 0)
                        lookingAt = 0
                        printPos(22, 1, "")
                        print(self.map[xx][y])
                        print(self.map[x][y])
                elif (lookingAt == 3):
                    # going down
                    if (self.map[xx][y].up ==0 and self.map[x][y].down ==0):
                        drawAt(xx, yy, 2)
            elif (xx==x):
                if (lookingAt == 0):
                    if (self.map[x][yy].right==0 and self.map[x][y].left==0 ):
                        drawAt(xx, yy, 3)
                        lookingAt = 0
                        printPos(22, 1, "")
                        print(self.map[x][yy])
                        print(self.map[x][y])
                elif (lookingAt == 2 or lookingAt==1):
                    if (self.map[x][y].right==0 and self.map[x][yy].left==0 ):
                        drawAt(xx, yy, 1)
                        lookingAt = 0
                        printPos(22, 1, "")
                        print(self.map[x][yy])
                        print(self.map[x][y])
            # Try straight
        walk(2,2, lookingAt)

    def canWalk(self, from_line, from_column, to_line, to_column):
        if (from_line == to_line): # Same line, going either left or right
            if (from_column < to_column): # Going right
                return (self.map[from_line][from_column].right == 0 and self.map[to_line][to_column].left == 0)
            elif (from_column > to_column): # Going left
                return (self.map[from_line][from_column].left == 0 and self.map[to_line][to_column].right == 0)
        elif (from_column == to_column): # Going up or down
            if (from_line < to_line): # Going down
                return (self.map[from_line][from_column].down == 0 and self.map[to_line][to_column].up == 0)
            elif (from_line > to_line): # Going up
                return (self.map[from_line][from_column].up == 0 and self.map[to_line][to_column].down == 0)
        return 0
    def inMaze(self, x, y):
        lines = (x < self.sy and x >= 0)
        columns = (y < self.sx and y >= 0)
        return (lines and columns)
    def left_firstSearchV2(self, x, y, v, w, printstack = 0, simulation = 0):
        # Parcours de labyrinth gauche au début
        # Mouvement possible: top (x+1, y), right (x, y+1), down (x+1, y), left (x-1, y)
        lookingAt = 1 # 0 Nord, 1 East, 2 South, 3 West
        self.stack = list()
        self.done = 0
        self.steps=0
        def walk(from_line, from_column, to_line, to_column, lookingAt):
            self.stack.append(self.map[from_line][from_column])
            if (printstack): printStack(self.stack)
            dict = [
                [ (-1, 0), (0, 1), (1, 0), (0, -1)], # straight, right, back, left 
                [ (0, 1), (1, 0), (0, -1), (-1, 0)],
                [ (1, 0), (0, -1), (-1, 0), (0, 1)],
                [ (0, -1), (-1, 0), (0, 1), (1, 0)]
            ]
            if (from_line == to_line and from_column == to_column):
                if (not simulation) : printPath(self.stack)
                printPos(30,1, "It took: " + str(int((time.time() - t1)*1000)) + " ms.")
                printPos(30,1, "It took: " + str(self.steps) + " steps.")
                self.done = 1
                return 
            time.sleep(SPEED)
            # drawAt(from_line, from_column)
            # printPos(22,1, "Looking at: " + str(lookingAt) + '\n')
            # Go left
            next_line = from_line + dict[lookingAt][-1][0]
            next_column = from_column + dict[lookingAt][-1][1]

            if (self.inMaze(next_line, next_column)):
                if (self.canWalk(from_line, from_column, next_line, next_column)):
                    if (self.map[next_line][next_column].visited == 1): 
                        return
                    lookingAt -=1
                    if lookingAt < 0 : lookingAt+=4
                    if (not simulation) : walkTo(from_line, from_column, next_line, next_column)
                    # from_line = next_line
                    # from_column = next_column
                    # self.map[next_line][next_column].visited = 1
                    self.steps+=1
                    walk(next_line, next_column, to_line, to_column, lookingAt)
                    lookingAt +=1
                    lookingAt %=4
            if (self.done): return

            # Go straight
            next_line = from_line + dict[lookingAt][0][0]
            next_column = from_column + dict[lookingAt][0][1]
            if (self.inMaze(next_line, next_column)):
                if (self.canWalk(from_line, from_column, next_line, next_column)):
                    if (self.map[next_line][next_column].visited == 1): 
                        return
                    # no changes to lookingAt variable
                    if (not simulation) : walkTo(from_line, from_column, next_line, next_column)
                    # self.map[next_line][next_column].visited = 1
                    # from_line = next_line
                    # from_column = next_column
                    self.steps += 1
                    walk(next_line, next_column, to_line, to_column, lookingAt)
                    
            if (self.done): return

            # Go right
            next_line = from_line + dict[lookingAt][1][0]
            next_column = from_column + dict[lookingAt][1][1]
            if (self.inMaze(next_line, next_column)):
                if (self.canWalk(from_line, from_column, next_line, next_column)):
                    if (self.map[next_line][next_column].visited == 1): 
                        return
                    lookingAt += 1
                    lookingAt = lookingAt%4
                    if (not simulation) : walkTo(from_line, from_column, next_line, next_column)
                    # self.map[next_line][next_column].visited = 1
                    # from_line = next_line
                    # from_column = next_column
                    self.steps+=1
                    walk(next_line, next_column, to_line, to_column, lookingAt)
                    lookingAt -=1
            if (self.done): return
            if (printstack): printStack(self.stack)
            self.stack.pop()
            return 1 # Go back
        starting_position = (x, y)
        goal_position = (v, w)
        drawAt(starting_position[0], starting_position[1])
        printPos(2, 1, Fore.GREEN + "Prioritizing LEFT --> FORWARD --> RIGHT --> BACKWARDS" )
        t1 = time.time()
        walk(starting_position[0], starting_position[1], goal_position[0], goal_position[1], lookingAt)
        return int(self.steps)
    def heuristic_search(self, x, y, v, w, simulation=0):
        steps = 0
        starting_position = (x, y)
        goal_position = (v, w)
        drawAt(starting_position[0], starting_position[1], translated=1)
        printPos(2, 80, Fore.GREEN + "Heuristic: Chooses the minimum flight distance between the current and goal cell.")
        next_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        possible_moves = list()
        path = list()
        def f(start, end):
            a = abs(start[0]-end[0])
            b = abs(start[1]-end[1])
            return a + b
        def sort(list):
            for i in range(len(list)):
                for j in range(len(list)):
                    if list[i][0] > list[j][0]:
                        list[i], list[j] = list[j], list[i]
        t1 = time.time()
        while (starting_position[0]!= goal_position[0] or starting_position[1] != goal_position[1]):
            time.sleep(SPEED)
            for move in next_moves:
                next_line = starting_position[0] + move[0]
                next_column = starting_position[1] + move[1]
                if (self.inMaze(next_line, next_column)):
                    if (self.map[next_line][next_column].visited == 0):
                        if (self.canWalk(starting_position[0], starting_position[1], next_line, next_column)):
                            next_position = (next_line, next_column)
                            possible_moves.append( (f(next_position, goal_position), starting_position, move) )
            if (len(possible_moves)== 0): return steps
            sort(possible_moves)
            themove = possible_moves[-1][-1]
            position = possible_moves[-1][1]
            next_line = position[0] + themove[0]
            next_column = position[1] + themove[1]
            self.map[next_line][next_column].visited = 1
            path.append(self.map[next_line][next_column])
            possible_moves.pop()
            # possible_moves = list()
            if (not simulation): walkTo(position[0], position[1], next_line, next_column, translated=1)
            steps+=1
            starting_position = (next_line, next_column)
        if (not simulation): printPath(self.stack, translated=1)
        printPos(30, 80, "It took: " + str(steps) + " steps.")
        return int(steps)

def printStack(listValues):
    nb_lines_print = 19
    nb_line_clear = 22
    starting_position = 2
    column_start_index = 80
    listValues = list(reversed(listValues))
    for i in range(starting_position, nb_line_clear):
        printPos(i, column_start_index, "                                                          ")
    printPos(starting_position,column_start_index, Fore.RED + str(len(listValues)) + " nodes in the stack.")
    for value,i in zip(listValues, range(0,len(listValues))):
        printPos(i+starting_position+1 - nb_lines_print*(i//nb_lines_print), column_start_index + 9*(i//nb_lines_print), Fore.WHITE + str(value))

def printPath(listValues, translated=0):
    for i in range(len(listValues)-1):
        walkTo(listValues[i].x, listValues[i].y, listValues[i+1].x, listValues[i+1].y, color=1, translated=translated)

def walkTo(from_line, from_column, to_line, to_column, color=0, translated=0):
    if (from_line == to_line):
        if (from_column < to_column):
            drawAt(to_line, to_column, 1, color, translated) # Going right
        elif (from_column > to_column ):
            drawAt(to_line, to_column, 3, color, translated) # Going left
    elif (from_column == to_column):
        if (from_line < to_line): # Going up
            drawAt(to_line, to_column, 0, color, translated) 
        elif (from_line > to_line): # Going down
            drawAt(to_line, to_column, 2, color, translated) 
    pass

def printPos(x, y, text_to_print):   #Function that let us print in desired Position
    sys.stdout.write("\x1b[%d;%df%s" % (x, y, Fore.RED + text_to_print))
    sys.stdout.flush()
def drawAt(line, column, from_direction=4, color=0, translated=0):
    line, column = toXY(line, column)
    line+=2 # used to translate the whole maze once in the bottom direction
    if (translated):
        column+=79
    if (color==0):
        if (from_direction == 0): # Coming from the top
            printPos(line-1, column, Fore.RED + 'v')
            printPos(line, column, Fore.RED + 'v')
        if (from_direction == 1): # Going right coming from the left
            printPos(line, column-3, Fore.RED + ' ')
            printPos(line, column-2, Fore.RED + '>')
            printPos(line, column-1, Fore.RED + ' ')
            printPos(line, column, Fore.RED + '>')
        if (from_direction == 2): # Coming from the bottom
            printPos(line+1, column, Fore.RED + '^')
            printPos(line, column, Fore.RED + '^')
        if (from_direction == 3) : # Coming from the right
            printPos(line, column+3, Fore.RED + ' ')
            printPos(line, column+2, Fore.RED + '<')
            printPos(line, column+1, Fore.RED + ' ')
            printPos(line, column, Fore.RED + '<')
        if (from_direction == 4):
            printPos(line, column, Fore.BLUE + 'x')
            pass
    elif (color==1):
        if (from_direction == 0): # Coming from the top
            printPos(line-1, column, Fore.BLUE + 'v')
            printPos(line, column, Fore.BLUE + 'v')
        if (from_direction == 1): # Going right coming from the left
            printPos(line, column-3, Fore.BLUE + ' ')
            printPos(line, column-2, Fore.BLUE + '>')
            printPos(line, column-1, Fore.BLUE + ' ')
            printPos(line, column, Fore.BLUE + '>')
        if (from_direction == 2): # Coming from the bottom
            printPos(line+1, column, Fore.BLUE + '^')
            printPos(line, column, Fore.BLUE + '^')
        if (from_direction == 3) : # Coming from the right
            printPos(line, column+3, Fore.BLUE + ' ')
            printPos(line, column+2, Fore.BLUE + '<')
            printPos(line, column+1, Fore.BLUE + ' ')
            printPos(line, column, Fore.BLUE + '<')
        if (from_direction == 4):
            printPos(line, column, Fore.BLUE + 'x')
            pass
def toXY(i, j): # i line of the cell / j column of cell
    return (i*2+2, j*4+3)