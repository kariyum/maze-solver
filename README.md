# Maze_solver
## Maze generation
Starts by generating a **random** maze assuring that it does not contain any closed areas using depth first algorithm. By closed areas I mean, every node is reachable by any other node. Depth first algorithm coupled with random choice of the next node made sure that the maze generated is random.

## Path finding: 
To find the path between two assinged nodes, two approaches were considered. A blind approach vs a heuristic approach, just to emphasize the use of heuritics. The algorithm starts from an assigned node then begins the search. 
### First blind approach
This approach prioritizes left -> forward -> right -> backward. Notice here the terms used, left forward right backward not north and so on. It is because the algorithm takes into account the direction that it is facing.
### Second heuristic approach
Best first approach is implemented this time. It computes the flying distance between its current position and the goal position.  