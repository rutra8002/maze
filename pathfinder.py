def find_path(maze):
    start = (1, 0)
    finish = (len(maze) - 2, len(maze[0]) - 1)
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    path = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

    queue = [(start, [])]

    while queue:
        (x, y), steps = queue.pop(0)

        if (x, y) == finish:
            for step in steps:
                path[step[0]][step[1]] = True
            path[x][y] = True
            return path

        if not visited[x][y]:
            visited[x][y] = True

        square_left = (x - 1, y)
        square_right = (x + 1, y)
        square_above = (x, y + 1)
        square_below = (x, y - 1)

        neighbors = [square_left, square_above, square_right, square_below]

        for neighbor in neighbors:
            nx, ny = neighbor
            if not visited[nx][ny] and not maze[nx][ny]:
                queue.append((neighbor, steps + [(x, y)]))


