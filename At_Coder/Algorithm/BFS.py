from collections import deque


def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[start[0]][start[1]] = True
    queue = deque([(start, 0)])  # (position, distance)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右, 下, 左, 上
    count = 0  # 訪問回数のカウント用

    while queue:
        (x, y), dist = queue.popleft()  # 一番左のに訪問座標を取得
        count += 1
        print(f'\nvisiting ({x}, {y})')

        if (x, y) == goal:  # ゴールに到達
            return dist, count

        for dx, dy in directions:  # 各方向（右下上左）に進める
            nx, ny = x + dx, y + dy

            # 進めた座標がグリッドの範囲内かつ未訪問かつ障害物がない
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True  # 訪問済みにして
                queue.append(((nx, ny), dist + 1))  # キューに追加(右に追加)
                print(queue)

    return -1, count  # ゴールに到達不可能


# 0 は空きマス、1 は障害物
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)  # 始点
goal = (2, 4)   # 終点

print(bfs(grid, start, goal))  # 結果を出力
