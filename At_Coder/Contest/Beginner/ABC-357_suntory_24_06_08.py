# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# サントリープログラミングコンテスト2024（AtCoder Beginner Contest 357）
# https://atcoder.jp/contests/abc357

# -----------------------------
# A Sanitize Hands

# n, m = map(int, input().split())
# h_l = list(map(int, input().split()))
# answer = n
# for i, h in enumerate(h_l):
#     if m >= h:
#         m -= h
#     else:
#         answer = i
#         break
# print(answer)


# -----------------------------
# B Uppercase and Lowercase

# s_l = input()
# l_count = 0
# s_count = 0
# for s in s_l:
#     if ord(s) >= ord('a') and ord(s) <= ord('z'):
#         s_count += 1
#     else:
#         l_count += 1
# ans = ''
# for s in s_l:
#     if s_count > l_count:
#         if ord(s) >= ord('a') and ord(s) <= ord('z'):
#             ans = ans+s
#         else:
#             ans = ans + chr(ord(s) - ord('A') + ord('a'))
#     else:
#         if ord(s) >= ord('a') and ord(s) <= ord('z'):
#             ans = ans + chr(ord(s) - ord('a') + ord('A'))
#         else:
#             ans = ans+s
# print(ans)

# -----------------------------
# C Sierpinski carpet

def generate_carpet(N):
    if N == 0:
        return ["#"]

    prev_carpet = generate_carpet(N - 1)
    size = len(prev_carpet)
    new_size = size * 3
    carpet = [["." for _ in range(new_size)] for _ in range(new_size)]

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue  # 中央は白
            for x in range(size):
                for y in range(size):
                    carpet[i * size + x][j * size + y] = prev_carpet[x][y]

    return ["".join(row) for row in carpet]


n = int(input())
carpet = generate_carpet(n)
for row in carpet:
    print(row)


# -----------------------------
# D 88888888

# def calculate_vn_modulo(n):
#     MOD = 998244353
#     n_str = str(n)
#     length = len(n_str)

#     result = 0
#     for _ in range(n):
#         result = (result * (10 ** length) + n) % MOD

#     return result


# n = int(input())
# result = calculate_vn_modulo(n)
# print(result)

# -----------------------------

# def calculate_vn_modulo(n):
#     MOD = 998244353
#     n_str = str(n)
#     length = len(n_str)

#     # power of 10 modulo MOD
#     power_10_len_mod = pow(10, length, MOD)

#     result = 0
#     for i in range(n):
#         result = (result * power_10_len_mod + n) % MOD

#     return result


# n = int(input())
# result = calculate_vn_modulo(n)
# print(result)

# おそらくオーバーフロー -----------------------------
# mod = 998244353
# n = int(input())
# k = len(str(n))  # 桁数
# ans = int(n*(10**(k*n)-1) / ((10**k)-1)) % mod
# print(ans)

# AC!!! -----------------------------

# def calculate_vn_modulo(n):
#     MOD = 998244353
#     n_str = str(n)
#     k = len(n_str)

#     # 10のべき乗を効率的に計算し、(10^k - 1) を計算する
#     power_10_k = pow(10, k, MOD)
#     power_10_k_n = pow(power_10_k, n, MOD)

#     # 幾何級数の和の計算 ( (10^k * n - 1) / (10^k - 1) )
#     numerator = (power_10_k_n - 1 + MOD) % MOD
#     denominator = (power_10_k - 1 + MOD) % MOD

#     # 分母の逆元を求める
#     denominator_inv = pow(denominator, MOD - 2, MOD)

#     # 最終的な答えを計算
#     result = (numerator * denominator_inv % MOD) * n % MOD

#     return result


# N = int(input())
# result = calculate_vn_modulo(N)
# print(result)


# -----------------------------
# E Reachability in Functional Graph

# # おそらく数値としては正しい。AC 17 TLE 14
# def find_reachable_pairs(N, a):
#     from collections import defaultdict

#     # グラフを作成
#     graph = defaultdict(list)
#     for i in range(1, N + 1):
#         graph[i].append(a[i - 1])

#     # 各頂点から到達可能な頂点のメモ
#     reachable_from = [None] * (N + 1)

#     # 深さ優先探索 (DFS) を用いて到達可能な頂点を探す関数
#     def dfs(start):
#         if reachable_from[start] is not None:
#             return reachable_from[start]

#         visited = [False] * (N + 1)
#         stack = [start]
#         reachable_nodes = set()
#         while stack:
#             node = stack.pop()
#             if not visited[node]:
#                 visited[node] = True
#                 reachable_nodes.add(node)
#                 for neighbor in graph[node]:
#                     if not visited[neighbor]:
#                         if reachable_from[neighbor] is not None:
#                             # すでに探索済みの頂点に到達した場合、その結果を再利用する
#                             reachable_nodes.update(reachable_from[neighbor])
#                         else:
#                             stack.append(neighbor)

#         # 探索結果をメモ
#         reachable_from[start] = reachable_nodes
#         return reachable_nodes

#     # 全ての頂点についてDFSを実行し、到達可能なペアの数を数える
#     total_reachable_pairs = 0
#     for i in range(1, N + 1):
#         reachable_nodes = dfs(i)
#         total_reachable_pairs += len(reachable_nodes)

#     return total_reachable_pairs


# # 入力例
# n = int(input())
# a = list(map(int, input().split()))

# # 結果を出力
# print(find_reachable_pairs(n, a))


# 蓮沼さん -----------------------------
def create_nested_list(n):
    return [[i] for i in range(1, n+1)]


n = int(input())
graph = list(map(int, input().split()))

# 関数呼び出しと結果表示
result = create_nested_list(n)

# graphのリストに格納されている数字をそれぞれの要素に格納
for i in range(n):
    if graph[i] not in result[i]:
        result[i].append(graph[i])

changed = True

# 追加操作
while changed:
    changed = False
    for i in range(n):
        for j in range(len(result[i])):
            index_to_check = result[i][j] - 1  # 0-based index
            if (index_to_check != i):
                for k in range(len(result[index_to_check])):
                    value_to_add = result[index_to_check][k]
                    if value_to_add not in result[i]:
                        result[i].append(value_to_add)
                        changed = True

total_elements = sum(len(sublist) for sublist in result)

# print(result)
print(total_elements)


# -----------------------------
# F Two Sequence Queries

# import sys
# input = sys.stdin.read
# data = input().split()

# MOD = 998244353

# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# queries = []
# for _ in range(Q):
#     query = list(map(int, input().split()))
#     q_type = query[0]
#     l = query[1]
#     r = query[2]

#     if q_type != 3:
#         v = query[3]
#         queries.append((q_type, l, r, v))
#     else:
#         queries.append((q_type, l, r))

# for query in queries:
#     q_type = query[0]
#     l = query[1]
#     r = query[2]

#     if q_type == 1:
#         v = query[3]
#         for i in range(l, r+1):
#             A[i] += v

#     elif q_type == 2:
#         v = query[3]
#         for i in range(l, r+1):
#             B[i] += v

#     elif q_type == 3:
#         result = 0
#         for i in range(l, r+1):
#             result += A[i] * B[i]
#             result %= MOD
#         print(result)


# -----------------------------
# G

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))
