# n = int(input())
# n, x = map(int, input().split())
# list = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]

# -----------------------------
# A AtCoder Line

# n, x, y, z = map(int, input().split())
# ans = 'No'
# if x <= z and y >= z:
#     ans = 'Yes'
# if y <= z and x >= z:
#     ans = 'Yes'
# print(ans)

# -----------------------------
# -----------------------------
# B Typing
# s = input()
# t = input()
# ans = []
# count = 0
# i = 0
# while count<len(s):
#     if t[i]==s[count]:
#         ans.append(i+1)
#         count+=1
#     i+=1
# print(*ans)


# -----------------------------
# -----------------------------
# C Standing On The Shoulders
# n = int(input())
# max_diff = 0
# ans = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     ans += a
#     max_diff = max(max_diff, b - a)
# ans += max_diff
# print(ans)


# -----------------------------
# -----------------------------
# D Permutation Subsequence
# def find_min_span(P, K):
#     indexed_P = sorted((value, index) for index, value in enumerate(P))
#     min_span = float('inf')

#     # スライディングウィンドウで連続するK個の要素を確認
#     for i in range(len(P) - K + 1):
#         indices = [idx for _, idx in indexed_P[i:i+K]]
#         span = max(indices) - min(indices)
#         if span < min_span:
#             min_span = span
#     return min_span

# n, k = map(int, input().split())
# p_l = list(map(int, input().split()))
# print(find_min_span(p_l, k))


# 改良版 pythonでは2/28がTLE，C++なら通った．
# def find_min_span(P, K):
#     indexed_P = sorted((value, index) for index, value in enumerate(P))
#     min_span = float('inf')

#     indices = {idx for _, idx in indexed_P[0:K]}
#     now_min = min(indices)
#     now_max = max(indices)
#     min_span = now_max - now_min

#     for i in range(1, len(P) - K + 1):
#         _, delete = indexed_P[i-1]
#         _, add = indexed_P[i+k-1]
#         indices.remove(delete)
#         indices.add(add)
#         if delete == now_min:
#             now_min = min(indices)
#         elif delete == now_max:
#             now_max = max(indices)
#         if add < now_min:
#             now_min=add
#         elif add > now_max:
#             now_max=add
#         span = now_max - now_min
#         min_span = min(min_span, span)
#     return min_span

# n, k = map(int, input().split())
# p_l = list(map(int, input().split()))
# print(find_min_span(p_l, k))

# -----------------------------
# -----------------------------
# E Clique Connect
n = int(input())
n, x = map(int, input().split())
s = list(map(int, input().split()))



# -----------------------------
# -----------------------------
# F 



# -----------------------------
# -----------------------------
# G