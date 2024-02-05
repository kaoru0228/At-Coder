'''
スタックを利用して，再帰を使わずに深さ優先探索(DFS)を実装する．
スタックはLIFO(Last-In-First-Out)の原理で動作し，最後に追加された要素が最初に取り出される．
これにより，現在のブランチを可能な限り深く探索し，目的のノードが見つからない場合には直前の分岐点まで戻る(バックトラックする)ことができる．
'''


def dfs_iterative(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右, 下, 左, 上
    stack = [(start[0], start[1])]  # スタックに始点を追加

    while stack:
        x, y = stack.pop()  # スタックからノードを取り出す

        if (x, y) == goal:
            return "Path found!"  # ゴールに到達

        if not visited[x][y]:
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 0:
                    stack.append((nx, ny))  # 隣接ノードをスタックに追加

    return "Path not found."  # ゴールに到達不可能


# 0 は空きマス、1 は障害物
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)  # 始点
goal = (2, 4)   # 終点

print(dfs_iterative(grid, start, goal))  # 結果を出力
