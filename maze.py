import random
import time
import os


# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to generate a random maze
def generate_maze(size):
    maze = [['#' for _ in range(size)] for _ in range(size)]
    start = (random.randint(0, size-1), random.randint(0, size-1))
    maze[start[0]][start[1]] = 'S'
    stack = [start]

    while stack:
        x, y = stack[-1]
        neighbors = []

        if x > 1 and maze[x-2][y] == '#':
            neighbors.append((x-2, y))
        if x < size-2 and maze[x+2][y] == '#':
            neighbors.append((x+2, y))
        if y > 1 and maze[x][y-2] == '#':
            neighbors.append((x, y-2))
        if y < size-2 and maze[x][y+2] == '#':
            neighbors.append((x, y+2))

        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[nx][ny] = ' '
            maze[(x+nx)//2][(y+ny)//2] = ' '
            stack.append((nx, ny))
        else:
            stack.pop()

    maze[random.randint(0, size-1)][random.randint(0, size-1)] = 'E'
    return maze

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(' '.join(row))

# Function to find the fastest path from S to E using BFS
def find_path(maze, start):
    queue = [(start, [])]
    visited = set()

    while queue:
        current, path = queue.pop(0)
        x, y = current

        if maze[x][y] == 'E':
            return path

        if current not in visited:
            visited.add(current)

            if x > 0 and maze[x-1][y] != '#' and (x-1, y) not in visited:
                queue.append(((x-1, y), path + [(x-1, y)]))
            if x < len(maze)-1 and maze[x+1][y] != '#' and (x+1, y) not in visited:
                queue.append(((x+1, y), path + [(x+1, y)]))
            if y > 0 and maze[x][y-1] != '#' and (x, y-1) not in visited:
                queue.append(((x, y-1), path + [(x, y-1)]))
            if y < len(maze)-1 and maze[x][y+1] != '#' and (x, y+1) not in visited:
                queue.append(((x, y+1), path + [(x, y+1)]))

# Function to move S through the maze
def move_s(maze, path):
    moves = 0
    for step in path:
        x, y = step
        maze[x][y] = 'S'
        clear_screen()
        print_maze(maze)
        time.sleep(0.5)
        maze[x][y] = ' '
        moves += 1
    return moves

# Main function
def main():
    size = int(input("Enter the size of the maze: "))
    if size <= 1:
      print("Choose a size above 1.")
      return
      
    maze = generate_maze(size)
    start = None

    for i in range(size):
        for j in range(size):
            if maze[i][j] == 'S':
                start = (i, j)
                break

    path = find_path(maze, start)
    moves = move_s(maze, path)
    print("Number of moves made by 'S' to reach 'E':", moves)

if __name__ == "__main__":
    main()





