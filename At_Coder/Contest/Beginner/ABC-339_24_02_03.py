# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))

# Contest名
# URL

# -----------------------------
# A

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))

# -----------------------------
# B

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))

# -----------------------------
# C

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))


# -----------------------------
# D

from collections import deque


def min_moves_to_meet(N, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # プレイヤーの初期位置を探す
    players = [(i, j) for i in range(N) for j in range(N) if grid[i][j] == 'P']
    if len(players) < 2:
        return -1

    # BFSのためのキューと訪問済みセット
    queue = deque([(players[0], players[1], 0)])
    visited = set(["{}_{}_{}_{}".format(*players[0], *players[1])])

    # BFS開始
    while queue:
        (p1, p2, moves) = queue.popleft()
        if p1 == p2:  # 2人のプレイヤーが同じマスに到達
            return moves

        for d in directions:
            new_p1 = (p1[0] + d[0], p1[1] + d[1])
            new_p2 = (p2[0] + d[0], p2[1] + d[1])

            if not (0 <= new_p1[0] < N and 0 <= new_p1[1] < N and grid[new_p1[0]][new_p1[1]] != '#'):
                new_p1 = p1
            if not (0 <= new_p2[0] < N and 0 <= new_p2[1] < N and grid[new_p2[0]][new_p2[1]] != '#'):
                new_p2 = p2

            state = "{}_{}_{}_{}".format(*new_p1, *new_p2)
            if state not in visited:
                visited.add(state)
                queue.append((new_p1, new_p2, moves + 1))

    return -1  # 2人のプレイヤーが同じマスに到達することができない場合


n = int(input())
grid = []
for _ in range(n):
    s = input()
    grid.append(s)

print(min_moves_to_meet(n, grid))  # 結果を出力


# -----------------------------
# E

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))


# -----------------------------
# F

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))


# -----------------------------
# G

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))
