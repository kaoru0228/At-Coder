# n, x = map(int, input().split())
# list = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# x = int(input())

# 日本レジストリサービス（JPRS）プログラミングコンテスト2024（AtCoder Beginner Contest 339）
# https://atcoder.jp/contests/abc339

# -----------------------------
# A TLD
# s = input()
# for i, s_ in enumerate(s):
#     if s[-1*(i+1)]=='.':
#         point = -1*(i+1)
#         break
# ans=''
# for i in range(point+1, 0):
#     ans = ans + s[i]
# print(ans)


# -----------------------------
# -----------------------------
# B Langton's Takahashi
# h, w, n = map(int, input().split())
# vect = [0, -1] # 上右下左 = 1 2 3 4
# pos = [0, 0]
# grid = [['.' for _ in range(w)] for _ in range(h)]
# for i in  range(n):
#     if grid[pos[1]][pos[0]]=='.':
#         grid[pos[1]][pos[0]]='#'
#         vect = [-1*vect[1], vect[0]]
#         pos[0]=(pos[0]+vect[0])%w
#         pos[1]=(pos[1]+vect[1])%h


#     elif grid[pos[1]][pos[0]]=='#':
#         grid[pos[1]][pos[0]]='.'
#         vect = [vect[1], -1*vect[0]]
#         pos[0]=(pos[0]+vect[0])%w
#         pos[1]=(pos[1]+vect[1])%h

# for row in grid:
#     print(''.join(row))


# -----------------------------
# -----------------------------
# C Perfect Bus
# n = int(input())
# a = list(map(int, input().split()))
# init_check = 0
# now = 0
# for i in  range(n):
#     now += a[i]
#     init_check=min(init_check, now)
# print(now-init_check)


# -----------------------------
# -----------------------------
# D Synchronized Players
# N = int(input())
# s_l = []
# for i in range(N):
#     s = input()
#     s_l.append(s)

# from collections import deque

# def min_moves_to_meet(N, grid):
#     # 方向ベクトル (上, 下, 左, 右)
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     # プレイヤーの初期位置を探す
#     players = []
#     for i in range(N):
#         for j in range(N):
#             if grid[i][j] == 'P':
#                 players.append((i, j))
#                 if len(players) == 2:
#                     break

#     # BFSのためのキューを初期化
#     queue = deque([(players[0], players[1], 0)])  # ((p1_row, p1_col), (p2_row, p2_col), moves)
#     visited = set((players[0], players[1]))

#     # BFS開始
#     while queue:
#         (p1, p2, moves) = queue.popleft()
#         if p1 == p2:  # 2人のプレイヤーが同じマスに到達
#             return moves

#         for d in directions:
#             # 各プレイヤーに対して移動
#             new_p1 = (p1[0] + d[0], p1[1] + d[1])
#             new_p2 = (p2[0] + d[0], p2[1] + d[1])

#             # 移動先がグリッド内で空きマスであるか確認
#             if not (0 <= new_p1[0] < N and 0 <= new_p1[1] < N and grid[new_p1[0]][new_p1[1]] != '#'):
#                 new_p1 = p1  # 移動できない場合、位置を保持
#             if not (0 <= new_p2[0] < N and 0 <= new_p2[1] < N and grid[new_p2[0]][new_p2[1]] != '#'):
#                 new_p2 = p2  # 移動できない場合、位置を保持

#             # 未訪問の位置の場合はキューに追加
#             if (new_p1, new_p2) not in visited:
#                 visited.add((new_p1, new_p2))
#                 queue.append((new_p1, new_p2, moves + 1))

#     return -1  # 2人のプレイヤーが同じマスに到達することができない場合

# print(min_moves_to_meet(N, s_l))  # 結果を出力


# -----------------------------
# -----------------------------
# E Smooth Subsequence
n, d = map(int, input().split())
a = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if abs(a[i] - a[j]) <= d:
            dp[i] = max(dp[i], dp[j] + 1)
result = max(dp)

print(result)

# -----------------------------
# -----------------------------
# F


# -----------------------------
# -----------------------------
# G
