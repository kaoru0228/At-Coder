# n, q = map(int, input().split())
# n = int(input())
# s = list(map(int, input().split()))


# AtCoder Beginner Contest 332
# https://atcoder.jp/contests/abc332


# -----------------------------
# A Online Shopping

# n, s, k = map(int, input().split())
# p_l = []
# q_l = []
# payment = 0
# for _ in range(n):
#     p, q = map(int, input().split())
#     payment += p*q
# if payment < s:
#     payment += k
# print(payment)


# -----------------------------
# B Glass and Mug

# k, g, m = map(int, input().split())
# glass = 0
# mag = 0
# for i in range(k):
#     if glass == g:
#         glass = 0
#     elif mag == 0:
#         mag = m
#     else:
#         if mag <= (g - glass):
#             glass += mag
#             mag = 0
#         else:
#             mag -= (g - glass)
#             glass = g
# result = [glass, mag]
# print(*result)


# -----------------------------
# C T-shirts

# n, m = map(int, input().split())
# s_l = input()
# count = []
# count_1 = 0
# count_2 = 0
# max_2 = 0
# max_days = 0
# for i, s in enumerate(s_l):
#     s = int(s)
#     if s == 1:
#         count_1 += 1
#     elif s == 2:
#         count_2 += 1
#     if s == 0 or i == (len(s_l)-1):
#         if (count_1 + count_2) > max_days:
#             max_days = count_1 + count_2
#         if count_2 > max_2:
#             max_2 = count_2
#         count_1 = 0
#         count_2 = 0

# if max_2 == 0 and m >= max_days:
#     result = 0
# elif max_2 > 0 and (m+max_2) >= max_days:
#     result = max_2
# else:
#     result = max_2 + (max_days - max_2 - m)
# print(result)

# # 回答 -----------
# # result = max(max_2, max_days-m)
# # print(result)

# -----------------------------
# D Swapping Puzzle

# h, w = map(int, input().split())
# for i in range(h):
#     a_l = list(map(int, input().split()))
# for i in range(h):
#     b_l = list(map(int, input().split()))

# 回答 -----------
# 転倒値を利用，現在の状態を行・列それぞれ順列で表現．
# from itertools import permutations # 順列を打ち出すライブラリ．
# def count_inversions(arr):
#     inv_count = 0
#     n = len(arr)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if arr[i] > arr[j]:
#                 inv_count += 1
#     return inv_count


# def main():
#     h, w = map(int, input().split())
#     a = [list(map(int, input().split())) for _ in range(h)]
#     b = [list(map(int, input().split())) for _ in range(h)]

#     ans = float('inf')
#     for p in permutations(range(1, h + 1)):
#         for q in permutations(range(1, w + 1)):
#             match = True
#             for i in range(h):
#                 for j in range(w):
#                     if a[p[i]-1][q[j]-1] != b[i][j]:
#                         match = False
#                         break
#                 if not match:
#                     break

#             if not match:
#                 continue

#             pinv = count_inversions(p)
#             qinv = count_inversions(q)
#             ans = min(ans, pinv + qinv)

#     if ans == float('inf'):
#         print(-1)
#     else:
#         print(ans)
# if __name__ == "__main__":
#     main()


# 回答２　幅優先探索
from collections import deque
from copy import deepcopy


def to_tuple(a):
    return tuple(tuple(r) for r in a)


H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

d = {to_tuple(A): 0}
q = deque([A])
while len(q) > 0:
    a = q.popleft()
    for i in range(H - 1):
        b = deepcopy(a)
        b[i], b[i + 1] = b[i + 1], b[i]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            q.append(b)
    for j in range(W - 1):
        b = deepcopy(a)
        for i in range(H):
            b[i][j], b[i][j + 1] = b[i][j + 1], b[i][j]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            q.append(b)
print(d[to_tuple(B)] if to_tuple(B) in d else -1)


# -----------------------------
# E Lucky bag

# n, d = map(int, input().split())
# w = list(map(int, input().split()))
# w.sort(reverse=True)
# bag = [[] for _ in range(d)]
# #  重い順に，とりあえず一つずつ重りを入れる
# for i in range(d):
#     bag[i] = w[0]
#     w.remove(w[0])
# # for i in range(len(w)):
# ave_2 = 0
# for b in bag:
#     ave_2 += b**2
# reslut = (ave_2/len(bag)) - ((sum(bag)/len(bag))**2)
# print(reslut)


# -----------------------------
# F

# n, q = map(int, input().split())
# n = int(input())
# s = list(map(int, input().split()))


# -----------------------------
# G

# n, q = map(int, input().split())
# n = int(input())
# s = list(map(int, input().split()))
