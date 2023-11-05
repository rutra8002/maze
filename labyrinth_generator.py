import random

def labyrinth(n):
    global rows
    global columns
    rows = n
    columns = n
    current_row = 1
    current_column = 0

    stack = []
    stack.append([current_row, current_column])

    Maze = making_Outline(rows, columns)

    Maze[current_row][current_column] = 2
    while current_row != rows - 1 and current_column != columns - 1:
        direction = Where_to_go(current_row, current_column, Maze)

        if direction < 5:
            current_row, current_column = moving(direction, current_row, current_column, Maze)
            stack.append([current_row, current_column])

            Maze[current_row][current_column] = 2
        elif direction == 5:
            Maze[current_row][current_column] = 5
            (current_row, current_column) = stack.pop()

    Tf = [True, False, True]
    for i in range(0, rows):
        for j in range(0, columns):
            if Maze[i][j] == 5 or Maze[i][j] == 0:
                Maze[i][j] = Tf[random.randint(0, 2)]

    for i in range(0, rows):
        for j in range(0, columns):
            if Maze[i][j] == 2:
                Maze[i][j] = False

    for i in range(0, rows):
        for j in range(0, columns):
            if Maze[i][j] == 1:
                Maze[i][j] = True

    return Maze

    # for i in range(0, len(Maze)):
    # print(Maze[i])


def generate_empty(rows, columns):
    matrix = [[0 for c in range(columns)] for r in range(rows)]
    return matrix


def buildTopWall(matrix, rows, columns):
    for column in range(columns):
        matrix[0][column] = 1


def buildLeftWall(matrix, rows, columns):
    for row in range(rows):
        matrix[row][0] = 1
    matrix[1][0] = 0


def buildRightWall(matrix, rows, columns):
    for row in range(rows):
        matrix[row][columns - 1] = 1
    matrix[row - 1][columns - 1] = 0


def buildBottomWall(matrix, rows, columns):
    for column in range(columns):
        matrix[rows - 1][column] = 1


def making_Outline(rows, columns):
    maze = generate_empty(rows, columns)
    buildTopWall(maze, rows, columns)
    buildBottomWall(maze, rows, columns)
    buildLeftWall(maze, rows, columns)
    buildRightWall(maze, rows, columns)
    return maze


def Where_to_go(current_row, current_column, Maze):
    list = []
    if current_column < columns - 1 and Maze[current_row][current_column + 1] == 0:
        right = 1
        list.append(right)
    if current_column > 0 and Maze[current_row][current_column - 1] == 0:
        left = 2
        list.append(left)
    if Maze[current_row - 1][current_column] == 0:
        up = 3
        list.append(up)
    if Maze[current_row + 1][current_column] == 0:
        down = 4
        list.append(down)

    if len(list) != 0:
        choice = list[(random.randint(0, len(list) - 1))]

        return choice
    else:
        return 5


def moving(direction, current_row, current_column, Maze):
    if direction == 1:
        current_column += 1
        Maze[current_row][current_column] = 2

    if direction == 2:
        current_column -= 1
        Maze[current_row][current_column] = 2

    if direction == 3:
        current_row -= 1
        Maze[current_row][current_column] = 2

    if direction == 4:
        current_row += 1
        Maze[current_row][current_column] = 2

    return (current_row, current_column)

