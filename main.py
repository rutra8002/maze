from pathfinder import find_path
from labyrinth_generator import labyrinth

maze = labyrinth(int(input()))
print(f"Maze: {maze}")
print(f"Path: {find_path(maze)}")
