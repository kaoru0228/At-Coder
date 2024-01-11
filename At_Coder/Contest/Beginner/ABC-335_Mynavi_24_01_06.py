# n, q = map(int, input().split())
# n = int(input())
# s = list(map(int, input().split()))

# AtCoder Beginner Contest 335（Sponsored by Mynavi）
# https://atcoder.jp/contests/abc335

# -----------------------------
# A 202<s>3</s>

# s = input()
# s_ = s[:-1] + '4'
# print(s_)

# -----------------------------
# B Tetrahedral Number

# n = int(input())
# for x in range(n+1):
#     for y in range(n+1):
#         for z in range(n+1):
#             if (x+y+z) <= n:
#                 print((str(x) + ' ' + str(y) + ' ' + str(z)))


# -----------------------------
# C Loong Tracking

# n, q = map(int, input().split())
# ope = {'R': 1, 'L': -1, 'U': 1, 'D': -1}
# head_track = [(1, 0)]
# result = []
# count1 = 0
# count2 = 0
# for i in range(q):
#     q1, q2 = input().split()
#     q1 = int(q1)
#     if q1 == 1:
#         count1 += 1
#         if q2 == 'R' or q2 == 'L':
#             head_track.append(
#                 (head_track[count1-1][0] + ope[q2], head_track[count1-1][1]))
#         if q2 == 'U' or q2 == 'D':
#             head_track.append(
#                 (head_track[count1-1][0], head_track[count1-1][1] + ope[q2]))
#     if q1 == 2:
#         q2 = int(q2)
#         count2 += 1
#         if q2 <= (count1+1):
#             result.append(str(head_track[-1*q2][0]) +
#                           ' ' + str(head_track[-1*q2][1]))
#         else:
#             result.append(str(q2-count1) + ' ' + '0')

# for result_ in result:
#     print(result_)

# -----------------------------
# D Loong and Takahashi

# def fill_numbers(n):
#     # n x n のマトリックスを作成（初期値は0）
#     matrix = [[0 for _ in range(n)] for _ in range(n)]

#     # 開始位置と方向の設定
#     x, y = 0, 0
#     dx, dy = 0, 1

#     # 1からn*nまでの数をマトリックスに埋める
#     for i in range(1, n * n + 1):
#         if i == n*n:
#             matrix[x][y] = 'T'
#             continue
#         matrix[x][y] = i
#         # 次のマスが境界を超えるか、すでに数字が埋められている場合は方向を変える
#         if not (0 <= (x + dx) < n and 0 <= (y + dy) < n and matrix[x + dx][y + dy] == 0):
#             dx, dy = dy, -dx
#         x += dx
#         y += dy

#     return matrix


# n = int(input())
# matrix = fill_numbers(n)
# for row in matrix:
#     print(" ".join(map(str, row)))

# -----------------------------
# E Non-Decreasing Colorful Path

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# graph = {}
# for i in range(n):
#     graph[i+1] = []
# for i in range(m):
#     u, v = map(int, input().split())
#     graph[u].append(v)
#     graph[v].append(u)
# for i in range(n):
#     graph[i+1].sort()


# def dfs(graph, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return [path]
#     if start not in graph:
#         return []
#     paths = []
#     for node in graph[start]:
#         if node not in path:
#             newpaths = dfs(graph, node, end, path)
#             for newpath in newpaths:
#                 paths.append(newpath)
#     return paths


# # AからFへの全ての単純なパスを探索
# all_paths = dfs(graph, 1, n)
# result = []
# for path in all_paths:
#     flag = 0
#     print(path)
#     for i in range(len(path)):
#         if i != (len(path)-1):
#             if not path[i] <= path[i+1]:
#                 flag = 1
#                 break
#     if flag == 0:
#         result.append(len(set(path)))
# if len(result) > 0:
#     print(max(result))
# else:
#     print(0)

# ----------------

n, m = map(int, input().split())
a = list(map(int, input().split()))
graph = {}
for i in range(n):
    graph[i+1] = []
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n):
    graph[i+1].sort()
print(graph)


def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path and node >= path[-1]:  # 順序チェックを追加
            newpaths = dfs(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


# AからFへの全ての単純なパスを探索
all_paths = dfs(graph, 1, n)
result = [len(set(path)) for path in all_paths]

print(max(result, default=0))  # リストが空の場合のデフォルト値を設定

# -----------------------------
# F

# n, q = map(int, input().split())
# n = int(input())
# s = list(map(int, input().split()))


# -----------------------------
# G Discrete Logarithm Problems

# n, p = map(int, input().split())
# a = list(map(int, input().split()))
