
maze = [
    ['S', 0, 1],
    [1, 0, 1],
    [0, 0, 'E']
]

queue = [(0, 0)]
visited = []

while queue:
    x, y = queue.pop(0)

    if maze[x][y] == 'E':
        print("Exit Found!")
        break

    if (x, y) not in visited:
        visited.append((x, y))

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:
                if maze[nx][ny] != 1 and (nx, ny) not in visited:
                    queue.append((nx, ny))
else:
    print("Exit Not Found")
