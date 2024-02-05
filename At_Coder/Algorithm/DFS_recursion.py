def dfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右, 下, 左, 上
    found = False

    def explore(x, y):
        nonlocal found
        if (x, y) == goal:
            found = True
            return True  # ゴールに到達

        visited[x][y] = True
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 0:
                if explore(nx, ny):  # 再帰的に探索
                    return True
        return False

    # 始点から探索を開始
    if explore(start[0], start[1]):
        return "Path found!"
    else:
        return "Path not found."


# 0 は空きマス、1 は障害物
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)  # 始点
goal = (2, 4)   # 終点

print(dfs(grid, start, goal))  # 結果を出力
