from ctypes.wintypes import tagRECT
from time import sleep
from xml.dom.pulldom import START_DOCUMENT

from sympy import false, true
from classes import *
import threading

# TO DO:
    # heuristic approach : Chooses the least difference in coordinates
    # let's say you're at (x, y) and your goal is (v, w)
    # your next move will be based on min(v-x + w-y)

def left_search(m, starting_cell, goal_cell):
    m.left_firstSearchV2(starting_cell[0], starting_cell[1], goal_cell[0], goal_cell[1], printstack=0)

def heuristic_search(m, starting_cell, goal_cell):
    m.heuristic_search(starting_cell[0], starting_cell[1], goal_cell[0], goal_cell[1])
if __name__ == '__main__':
    os.system('cls||clear')
    simulation = 0
    m = Maze(17,13)
    m.constructMazeV3()
    if (not simulation):
        # --- start here ---
        m.graphicMazeV2()
        starting_cell = (0, 0)
        goal_cell = (6, 6)
        # Left first search
        printPos(1, 1, Fore.BLUE + "Path"+ Fore.RED + Fore.WHITE + " searching algorithms using different heuristics.")
        drawAt(goal_cell[0], goal_cell[1])
        left_steps = m.left_firstSearchV2(starting_cell[0], starting_cell[1], goal_cell[0], goal_cell[1], printstack=0)
        m.graphicMazeV2(1)
        # Heuristic approach
        drawAt(goal_cell[0], goal_cell[1], translated=1)
        h_steps = m.heuristic_search(starting_cell[0], starting_cell[1], goal_cell[0], goal_cell[1])
        # --- end here ---
    else:
        # --- stats ---
        left_steps = 0
        h_steps = 0

        left_wins = 0
        h_wins = 0

        steps_diff = 0
        total_left_steps = 0
        random.seed(time.time())
        for i in range(10000):
            printPos(1,1, Fore.WHITE)
            m = Maze(17,13)
            m.constructMazeV3()
            starting_cell=(int(random.random() * m.sy), int(random.random() * m.sx))
            goal_cell = (int(random.random() * m.sy), int(random.random() * m.sx))
            # m.graphicMazeV2()

            # Left first search
            printPos(1, 1, Fore.BLUE + "Path"+ Fore.RED + Fore.WHITE + " searching algorithms using different heuristics.")
            left_steps += m.left_firstSearchV2(starting_cell[0], starting_cell[1], goal_cell[0], goal_cell[1], printstack=0, simulation=1)
            # drawAt(goal_cell[0], goal_cell[1])
            # m.graphicMazeV2(1)
            # Heuristic approach
            h_steps += m.heuristic_search(starting_cell[0], starting_cell[1], goal_cell[0], goal_cell[1], simulation=1)
            # drawAt(goal_cell[0], goal_cell[1], translated=1)
            os.system('cls||clear')
            printPos(31,1,"Number of iterations= "+ Fore.BLUE + str(i) + '\n')
            if (left_steps > h_steps ) : left_wins+=1
            else : h_wins +=1
            p = int(h_wins/(h_wins + left_wins) *10000)/100
            printPos(32, 1, Fore.RED + "Heuristic approach wins " + Fore.BLUE + str(p) + Fore.RED +" % of the time.")
            steps_diff += left_steps - h_steps
            total_left_steps += left_steps
            try : 
                a = int((steps_diff / total_left_steps)*10000)/100
                printPos(33, 1, "Heuristic approach covers " + Fore.BLUE + str(a) + Fore.RED + " % less steps")
            except:
                pass
            left_steps=0
            h_steps=0
            

        # print(left_steps)
        # print(h_steps)
        # print(left_steps / h_steps)
        
        # --- end stats ---

    # Threading
    # left_search_thread = threading.Thread(target=left_search, args=(m, starting_cell, goal_cell))
    # heuristic_thread = threading.Thread(target=heuristic_search, args=(m, starting_cell, goal_cell))

    # left_search_thread.start()
    # heuristic_thread.start()
    input()