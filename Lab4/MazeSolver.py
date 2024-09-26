"""
 File name: python_Lab1.py
    Author: Kenneth Tabilas 
    Date created: 09/25/2024
    Python Version: 3.6.9 
"""
from SearchStructures import Stack, Queue
from Maze import Maze

class MazeSolver:
    # Constructor
    # Inputs:
    #   maze: The maze to solve (Maze)
    #   searchStructure: The search structure class to use (Stack or Queue)
    def __init__(self, maze, searchStructure):
        self.maze = maze             # The maze to solve
        self.ss = searchStructure()  # Initialize a searchStructure object

    def tileIsVisitable(self, row:int, col:int) -> bool:
        # ~~~~~~~~
        # Write your tileIsVisitable() implementation here
         #Check if the coordinates are within the bonds of the maze 
        if row < 0 or row >= self.maze.num_rows or col < 0 or col >= self.maze.num_cols: 
           return False 
        tile = self.maze.contents[row][col]
        # This will chek if the tiles is not a wall and hasent been visited yet
        return not tile.isWall() and not tile.hasBeenVisited()
        # ~~~~~~~~

    def solve(self):
        # ~~~~~~~~
        # Write your solve() implementation 
        # Add the starting tile to the search 
        self.ss.add(self.maze.start)
        # While is being used to search is not empty 
        while not self.ss.isEmpty():
            current_tile = self.ss.remove()
            current_tile.visit()
            #This will check if the current tile is the goal 
            if current_tile == self.maze.goal:
                # Return goal tile if found 
                return current_tile
            # Get the neighobor of the current tile (N,S,E,W)
            row, col = current_tile.getRow(),current_tile.getCol()
            neighbors = [(row - 1, col),  # North
                        (row + 1, col),  # Sout
                        (row, col - 1),  # West
                         (row, col + 1)]  # East

            #For each neighbor, check if it id visitable
            for r, c in neighbors: 
                if self.tileIsVisitable(r, c):
                    neighbors_tile = self.maze.contents[r][c]
                    #Track the path 
                    neighbors_tile.setPrevious(current_tile) 
                    self.ss.add(neighbors_tile)
                    # No solution is found 
                    return None     
         # ~~~~~~~~
     # Add any other helper functions you might want here

    def getPath(self):
        # ~~~~~~~~
        # Write your getPath() implementation here
        path = []
        current = self.maze.goal 
        while current:
            path.append(current)
            # Follow the path backwards 
            current = current.getPrevious()
            # Reverse the path to get it from start to goal
        return path[::-1]
        # ~~~~~~~~

    # Print the maze with the path of the found solution
    # from Start to Goal. If there is no solution, just
    # print the original maze.
    def printSolution(self):
        # Get the solution for the maze from the maze itself
        solution = self.getPath()
        # A list of strings representing the maze
        output_string = self.maze.makeMazeBase()
        # For all of the tiles that are part of the path, 
        # mark it with a *
        for tile in solution:
            output_string[tile.getRow()][tile.getCol()] = '*'
        # Mark the start and goal tiles
        output_string[self.maze.start.getRow()][self.maze.start.getCol()] = 'S'
        output_string[self.maze.goal.getRow()][self.maze.goal.getCol()] = 'G'

        # Print the output string
        for row in output_string:
            print(row)

   

if __name__ == "__main__":
    # The maze to solve
    maze = Maze(["____",
                 "S##G",
                 "__#_",
                 "____"])
    # Initialize the MazeSolver to be solved with a Stack
    solver = MazeSolver(maze, Stack)
    # Solve the maze
    solver.solve()
    # Print the solution found
    solver.printSolution()