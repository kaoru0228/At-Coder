# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# トヨタ自動車プログラミングコンテスト2024 #7（AtCoder Beginner Contest 362）
# https://atcoder.jp/contests/abc362

# -----------------------------
# A Buy a Pen

# r, g, b = map(int, input().split())
# c = input()

# if c == 'Red':
#     answer = min(g, b)
# elif c == 'Green':
#     answer = min(r, b)
# else:
#     answer = min(r, g)
# print(answer)

# -----------------------------
# B Right Triangle

# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())

# a = (x1-x2)**2 + (y1-y2)**2
# b = (x2-x3)**2 + (y2-y3)**2
# c = (x3-x1)**2 + (y3-y1)**2

# flag = False
# if a + b == c:
#     flag = True
# elif b + c == a:
#     flag = True
# elif c + a == b:
#     flag = True

# if flag:
#     print('Yes')
# else:
#     print('No')


# -----------------------------
# C Sum = 0

# n = int(input())
# l_l = []
# r_l = []
# x_l = []

# l_sum = 0
# r_sum = 0
# for i in range(n):
#     l, r = map(int, input().split())
#     l_sum += l
#     r_sum += r
#     l_l.append(l)
#     r_l.append(r)

# current_sum = 0
# if l_sum <= 0 and r_sum >= 0:

#     for l, r in zip(l_l, r_l):
#         if current_sum + l <= 0 <= current_sum + r:
#             x_i = -current_sum
#         elif current_sum + r < 0:
#             x_i = r
#         else:
#             x_i = l
#         x_l.append(x_i)
#         current_sum += x_i

#     print('Yes')
#     print(*x_l)
# else:
#     print('No')
# print(current_sum)
# print(l_sum, r_sum)

# ごり押し -----------------------------

# n = int(input())
# l_l = []
# r_l = []
# x_l = [0]*n
# check = [0]*n

# plus_l = []
# minus_l = []
# zero_l = []

# p_sum = 0
# m_sum = 0

# for i in range(n):
#     l, r = map(int, input().split())
#     l_l.append(l)
#     r_l.append(r)

#     if l > 0:
#         check[i] = 1
#         x_l[i] = l
#         p_sum += l
#         plus_l.append((i, l, r))

#     elif r < 0:
#         check[i] = 2
#         x_l[i] = r
#         m_sum += r
#         minus_l.append((i, l, r))

#     else:  # 区間に0を含む
#         zero_l.append((i, l, r))


# current_sum = 0
# if sum(l_l) <= 0 and sum(r_l) >= 0:

#     if abs(p_sum) >= abs(m_sum):
#         current_sum = p_sum + m_sum
#         for i, l, r in minus_l:
#             if r-l < current_sum:
#                 x_l[i] = l
#                 current_sum -= r-l
#             elif r-l >= current_sum:
#                 x_l[i] = r - current_sum
#                 current_sum = 0

#             if current_sum == 0:
#                 break

#     elif abs(p_sum) < abs(m_sum):
#         current_sum = p_sum + m_sum
#         for i, l, r in plus_l:
#             if r-l < abs(current_sum):
#                 x_l[i] = r
#                 current_sum += r-l
#             elif r-l >= abs(current_sum):
#                 x_l[i] = l + abs(current_sum)
#                 current_sum = 0

#             if current_sum == 0:
#                 break

#     for i, l, r in zero_l:
#         if current_sum > 0:
#             if abs(l) < current_sum:
#                 x_l[i] = l
#                 current_sum += l
#             elif abs(l) >= current_sum:
#                 x_l[i] = current_sum*(-1)
#                 current_sum = 0
#         else:  # current_sum < 0
#             if abs(r) < abs(current_sum):
#                 x_l[i] = r
#                 current_sum += r
#             elif abs(r) >= abs(current_sum):
#                 x_l[i] = current_sum*(-1)
#                 current_sum = 0

#         if current_sum == 0:
#             break

#     print('Yes')
#     print(*x_l)
# else:
#     print('No')


# -----------------------------
# D　Shortest Path 3

# import heapq


# def dijkstra(N, M, A, edges):
#     # グラフの構築
#     graph = [[] for _ in range(N + 1)]
#     for U, V, B in edges:
#         graph[U].append((V, B))
#         graph[V].append((U, B))

#     # 始点1からの最短距離
#     dist = [float('inf')] * (N + 1)
#     dist[1] = A[0]  # 始点の重みを初期化

#     # 優先度付きキュー
#     pq = [(A[0], 1)]  # (距離, 頂点)

#     while pq:
#         current_dist, u = heapq.heappop(pq)

#         # 現在の距離が既存の距離よりも大きい場合は無視
#         if current_dist > dist[u]:
#             continue

#         for v, weight in graph[u]:
#             distance = current_dist + weight + A[v - 1]  # Aは0-indexed
#             if distance < dist[v]:
#                 dist[v] = distance
#                 heapq.heappush(pq, (distance, v))

#     # 各頂点への最短距離を返す
#     return dist


# def main():
#     n, m = map(int, input().split())
#     a_l = list(map(int, input().split()))

#     edges = []
#     for i in range(m):
#         u, v, b = map(int, input().split())
#         edges.append((u, v, b))

#     # ダイクストラ法の実行
#     dist = dijkstra(n, m, a_l, edges)

#     # 結果を出力
#     result = [str(dist[i]) for i in range(2, n + 1)]
#     print(' '.join(result))


# if __name__ == "__main__":
#     main()


# -----------------------------
# E Count Arithmetic Subsequences 無理！

# MOD = 998244353


# # def is_eqdiff(list):
# #     if len(list) <= 2:
# #         return True
# #     d = list[1] - list[0]
# #     for i in range(2, len(list)):
# #         if (list[i] - list[i-1]) == d:
# #             continue
# #         else:
# #             return False


# def count_subsequences(N, A):
#     dp = [[0] * N for _ in range(N)]
#     result = [0] * N

#     for i in range(N):
#         dp[i][0] = 1
#         result[0] += 1

#     for length in range(1, N):
#         for i in range(N):
#             for j in range(i):
#                 if (A[i] - A[j]) % MOD == length:
#                     dp[i][length] += dp[j][length - 1]
#                     dp[i][length] %= MOD
#             result[length] += dp[i][length]
#             result[length] %= MOD

#     return result


# # 入力の読み込み
# n = int(input())
# a_l = list(map(int, input().split()))

# # 結果の計算
# result = count_subsequences(n, a_l)

# # 結果の出力
# print(" ".join(map(str, result)))


# 解答見た上で　DPによる解法（O(n^4)）あとちょっとがうまくいかない -----------------------------
# ポイント：初項と第2項が決まると、交差が確定する！！！

# mod = 998244353

# n = int(input())
# a_l = list(map(int, input().split()))

# # dp[i][j][l] Aiは初項、Ajは第2項、lは初項、第2項をAi, Ajとする等差数列において長さlとなるものの個数。
# # ※　第2項までで公差が決まる = 第3項以降は同じ数字となる！
# dp = [[[[0, {}] for _ in range(n+1)] for _ in range(n)] for _ in range(n)]

# for i in range(n):
#     for j in range(i+1, n):
#         for l in range(2, n+1):
#             if l == 2:
#                 dp[i][j][l][0] += 1
#             elif l == 3:
#                 d = a_l[j] - a_l[i]  # 公差
#                 for k in range(j+1, n):
#                     if a_l[k] == (a_l[i] + d*(l-1)):  # 第l項が見つかった場合
#                         dp[i][j][l][0] += 1
#                         dp[i][j][l][1][str(k)] = 1
#             # lが4以上の場合
#             elif l > 3:
#                 d = a_l[j] - a_l[i]  # 公差
#                 cnt = 0  # 一つ長さの短い数列の個数
#                 for k in range(j+1, n):
#                     if a_l[k] == (a_l[i] + d*(l-2)):  # 1つ前の項が見つかった場合
#                         cnt += dp[i][j][l-1][1][str(k)]
#                     elif a_l[k] == (a_l[i] + d*(l-1)):  # 第l項が見つかった場合
#                         dp[i][j][l][0] = (dp[i][j][l][0] + cnt) % mod
#                         dp[i][j][l][1][str(k)] = cnt

# # 長さ1の数列はn個ある
# ans = [n]
# for l in range(2, n+1):
#     tmp = 0
#     for i in range(n):
#         for j in range(n):
#             tmp += dp[i][j][l][0]
#     ans.append(tmp % mod)

# print(*ans)
# # print(dp)


# 模範解答 -----------------------------

mod = 998244353

N = int(input())
A = list(map(int, input().split()))
dp = [[[0] * (N + 1) for _ in range(N)] for _ in range(N)]

for i in range(N)[::-1]:  # (n-1)から0まで、逆順
    for j in range(i + 1, N):
        dp[i][j][2] += 1
        for l in range(2, N - i):
            for k in range(j + 1, N):
                if A[k] - A[j] != A[j] - A[i]:
                    continue
                dp[i][j][l + 1] = (dp[i][j][l + 1] + dp[j][k][l]) % mod
ans = [0] * (N + 1)
ans[1] = N
for i in range(N):
    for j in range(N):
        for l in range(2, N - i + 1):
            ans[l] = (ans[l] + dp[i][j][l]) % mod
print(*ans[1:])

# -----------------------------
# F

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))


# -----------------------------
# G
