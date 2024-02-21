# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# 鹿島建設プログラミングコンテスト2024（AtCoder Beginner Contest 340）
# https://atcoder.jp/contests/abc340

# -----------------------------
# A Arithmetic Progression
# a, b, d = map(int, input().split())
# i = a
# ans = [a]
# while (i != b):
#     i += d
#     ans.append(i)

# print(*ans)

# -----------------------------
# B Append
# q = int(input())
# l = []
# ans = []
# for i in range(q):
#     q1, q2 = map(int, input().split())
#     if q1 == 1:
#         l.append(q2)
#     else:
#         ans.append(l[-1*q2])
# for a in ans:
#     print(a)

# -----------------------------
# C Divide and Divide  TEL ⇒ メモ化再帰により効率化
# n = int(input())
# memo = {}
# def calc(N):  # 再帰で解く
#     if N == 1:
#         return 0
#     else:
#         if N in memo:
#             return memo[N]
#         else:
#             memo[N] = N + calc(N // 2) + calc((N + 1) // 2)
#             return memo[N]
# print(calc(n))


# -----------------------------
# D Super Takahashi Bros.
# import heapq
# n = int(input())
# a_l = []
# b_l = []
# x_l = []
# # グラフの構築 リストのリスト．
# # graph[i] = [(cost, next_stage), ...]
# graph = [[] for _ in range(n + 1)]
# for i in range(n-1):
#     a, b, x = map(int, input().split())
#     a_l.append(a)
#     b_l.append(b)
#     x_l.append(x)
#     graph[i+1].append((a, i + 2))  # A行動
#     graph[i+1].append((b, x))  # B行動

# # ダイクストラ法で最短経路を探索


# def dijkstra(start):
#     # dp[i]はステージiに達するための最短時間
#     dp = [float('inf')] * (n + 1)  # 各頂点への最短コストを保持するリスト
#     dp[start] = 0
#     queue = [(0, start)]  # (cost, stage)

#     while queue:
#         current_cost, current_stage = heapq.heappop(queue)
#         # なくてもよいが，若干時短．
#         if dp[current_stage] < current_cost:
#             continue

#         for cost, next_stage in graph[current_stage]:
#             if dp[next_stage] > current_cost + cost:  # 現在記憶しているコストよりも新たな経路のコストが小さい場合
#                 dp[next_stage] = current_cost + cost  # 更新
#                 # コストが更新されたため，頂点を経由する経路は再調査の必要あり．よってキューに追加．
#                 heapq.heappush(queue, (dp[next_stage], next_stage))

#     return dp


# dp = dijkstra(1)
# # print(dp)
# print(dp[n])

# -----------------------------
# E Mancala 2
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i, bi in enumerate(b):
    num = a[bi]
    a[bi] = 0
    every = num//n
    part = num % n
    for j in range(n):
        if part > 0:
            a[(bi+part) % n] += 1
            part -= 1
        a[j] += every
print(*a)

# --------------------
# def distribute_balls(N, M, A, B):
#     # 箱ごとのボールの数を格納するリスト
#     boxes = A[:]
#     diff = []
#     for i in range(len(boxes)):
#         if i == 0:
#             diff.append(boxes[i])
#         else:
#             diff.append(boxes[i]-boxes[i-1])
#     print(diff)

#     for i in range(M):
#         # 箱Biからボールを全て取り出す
#         balls = boxes[B[i]]
#         boxes[B[i]] = 0  # 箱を空にする

#         # ボールを移動させる 2周以上する場合の考慮が必要
#         # C = 1
#         # start_box = (B[i] + C) % N
#         # last_box = (B[i] + C - 1 + balls) % N
#         # C = C + balls - 1
#         # if start_box <= last_box:
#         #     diff[start_box] += 1
#         #     diff[last_box+1] -= 1
#         # else:

#         for j in range(balls):
#             C = j + 1  # Cの値を増やす
#             next_box = (B[i] + C) % N  # 次の箱の番号を計算
#             boxes[next_box] += 1  # ボールを入れる

#     return boxes


# # 各箱に入っているボールの個数を求める
# final_balls = distribute_balls(n, m, a, b)
# print(*final_balls)


# -----------------------------
# F S = 1

# X, Y = map(int, input().split())


# def find_triangle_vertices(X, Y):
#     # 与えられた X, Y に対して、条件を満たす A, B を見つける
#     # |X*B - Y*A| = 2 の条件から A または B を選んで解を求める

#     # A を 0 として解を求める場合
#     A = 0
#     if X != 0 and (2 % X) == 0:
#         B = 2 // X
#         return A, B

#     # B を 0 として解を求める場合
#     B = 0
#     if Y != 0 and (2 % Y) == 0:
#         A = 2 // Y
#         return A, B

#     # A = 1 の場合、B を求める
#     A = 1
#     if X != 0 and ((2 + Y) % X) == 0:
#         B = (2 + Y) // X
#         if abs(A) <= 10**18 and abs(B) <= 10**18:
#             return A, B

#     # B = 1 の場合、A を求める
#     B = 1
#     if Y != 0 and ((2 + X) % Y) == 0:
#         A = (2 + X) // Y
#         if abs(A) <= 10**18 and abs(B) <= 10**18:
#             return A, B

#     # 条件を満たす A, B が見つからない場合
#     return (-1)


# ans = find_triangle_vertices(X, Y)
# if ans == -1:
#     print(ans)
# else:
#     print(*ans)


# -----------------------------
# G

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))
