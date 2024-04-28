# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# AtCoder Beginner Contest 350（Promotion of AtCoderJobs）
# https://atcoder.jp/contests/abc350

# -----------------------------
# A Past ABCs

# s = input()
# num = int(s[3:])
# ans = 'Yes' if num > 0 and num < 350 and num != 316 else 'No'
# print(ans)


# -----------------------------
# B Dentist Aoki

# n, q = map(int, input().split())
# t_l = list(map(int, input().split()))
# teeth = [1]*n
# for t in t_l:
#     teeth[t-1] = (teeth[t-1]+1) % 2
# print(sum(teeth))


# -----------------------------
# C Sort

# n = int(input())
# a_l = list(map(int, input().split()))
# ans = []
# flag = False
# while not flag:
#     for i, a in enumerate(a_l):
#         if (i+1) != a:
#             a_l[i] = a_l[a-1]
#             a_l[a-1] = a
#             if (i+1) <= a:
#                 ans.append([i+1, a])
#             else:
#                 ans.append([a, i+1])
#     flag = True
#     for i, a in enumerate(a_l):
#         if (i+1) != a:
#             flag = False
#             break

# print(len(ans))
# if len(ans) != 0:
#     for ans_ in ans:
#         print(*ans_)

# -----------------------------
# D New Friends

# TLE
# n, m = map(int, input().split())
# a_l = []
# b_l = []
# friends_l = [[] for _ in range(n+1)]
# for i in range(m):
#     a, b = map(int, input().split())
#     a_l.append(a)
#     b_l.append(b)
#     friends_l[a].append(b)
#     friends_l[b].append(a)

# count = 0
# update = set(range(1, n+1))
# while len(update) != 0:
#     update_new = set()
#     for y in range(1, n+1):
#         if y not in update:
#             continue
#         y_friends = sorted(friends_l[y])
#         for i in range(len(y_friends)):
#             for j in range(i+1, len(y_friends)):
#                 x = y_friends[i]
#                 z = y_friends[j]
#                 if z not in friends_l[x]:
#                     friends_l[x].append(z)
#                     friends_l[z].append(x)
#                     update_new.add(x)
#                     update_new.add(y)
#                     count += 1
#     update = update_new
# print(count)


# GPT4 TLE ------------
# from collections import defaultdict


# def max_operations(n, friendships):
#     # 友達関係を表すグラフを構築
#     graph = defaultdict(set)
#     graph_sub = defaultdict(set)
#     for a, b in friendships:
#         graph[a].add(b)
#         graph[b].add(a)
#         graph_sub[min(a, b)].add(max(a, b))

#     operations = 0

#     update = True
#     while update:
#         update = False
#         # すべてのユーザに対して操作可能な組み合わせを検証
#         for y in range(1, n+1):
#             # 友達リストからXとZのペアを選ぶ
#             friends = sorted(graph[y])  # ソートして小さい方をX、大きい方をZとする
#             for i in range(len(friends)):
#                 x = friends[i]
#                 for j in range(i+1, len(friends)):
#                     z = friends[j]
#                     # XとZが友達でないか確認
#                     if z not in graph[x]:
#                         operations += 1
#                         graph[x].add(z)
#                         graph[z].add(x)
#                         update = True

#     return operations


# n, m = map(int, input().split())
# friendships = []
# for i in range(m):
#     a, b = map(int, input().split())
#     friendships.append((a, b))
# print(max_operations(n, friendships))

# Koki Amakawa ---------------
# from collections import defaultdict, deque


# def add_edge(graph, u, v):
#     graph[u].append(v)
#     graph[v].append(u)


# def bfs_component(graph, start, visited):
#     queue = deque([start])
#     component = []
#     visited[start] = True
#     while queue:
#         node = queue.popleft()
#         component.append(node)
#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 queue.append(neighbor)
#     return component


# def connected_components(graph):
#     visited = {node: False for node in graph}
#     components = []
#     for node in graph:
#         if not visited[node]:
#             components.append(bfs_component(graph, node, visited))
#     return components


# n, m = map(int, input().split())
# graph = defaultdict(list)
# for i in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# groups = connected_components(graph)
# ans = 0
# for group in groups:
#     ans += (len(group)*(len(group)-1))//2
# ans -= m
# print(ans)


# -----------------------------
# E

# n, a, x, y = map(int, input().split())


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
