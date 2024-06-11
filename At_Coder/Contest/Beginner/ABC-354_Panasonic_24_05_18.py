# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# パナソニックグループ プログラミングコンテスト2024（AtCoder Beginner Contest 354）
# https://atcoder.jp/contests/abc354

# -----------------------------
# A Exponential Plant

# h = int(input())
# k = 0
# i = 0
# while k <= h:
#     k += 2**i
#     i += 1
# print(i)

# -----------------------------
# B AtCoder Janken 2

# n = int(input())
# rate = 0
# names = []
# for i in range(n):
#     s, c = input().split()
#     names.append(s)
#     rate += int(c)
# sorted_names = sorted(names)
# print(sorted_names[rate % n])


# -----------------------------
# C AtCoder Magics

# n = int(input())
# cards = []
# for i in range(n):
#     a, c = map(int, input().split())
#     cards.append((a, c, i+1))
# cards.sort(key=lambda x: (-x[0], x[1]))
# remaining = []
# min_cost = float('inf')
# for strength, cost, idx in cards:
#     if cost < min_cost:
#         remaining.append(idx)
#         min_cost = cost
# remaining.sort()
# print(len(remaining))
# print(*remaining)


# -----------------------------
# D AtCoder Wallpaper AC!

# a, b, c, d = map(int, input().split())
# w = c - a
# h = d - b
# ans = 0
# ans += (w//4) * h * 2 * 2

# isBlack = a % 4
# for i in range(w % 4):
#     if isBlack in [0, 1]:
#         ans += (h//2) * 3
#     else:
#         ans += (h//2) * 1

#     if (h % 2) == 1:
#         if (isBlack % 4) == 0:
#             if (b % 2) == 0:
#                 ans += 2
#             else:
#                 ans += 1
#         elif (isBlack % 4) == 1:
#             if (b % 2) == 0:
#                 ans += 1
#             else:
#                 ans += 2
#         elif (isBlack % 4) == 2:
#             if (b % 2) == 0:
#                 ans += 0
#             else:
#                 ans += 1
#         else:
#             if (b % 2) == 0:
#                 ans += 1
#             else:
#                 ans += 0
#     isBlack = (isBlack+1) % 4
# print(ans)


# # 解答参照 -----------------------------
# # 以下のように、事前に2×4の最小長方形の黒マスをリストで管理するとよい。
# mass = [[2, 1, 0, 1], [1, 2, 1, 0]]
# # また、その各マス（計8つ）が、それぞれ何回現れるかをカウントするとコードが短く、簡潔になる。


# -----------------------------
# E Remove Pairs

from collections import defaultdict, Counter
n = int(input())
a_l = []
b_l = []
for i in range(n):
    a, b = map(int, input().split())
    a_l.append(a)
    b_l.append(b)


def game_winner(N, A, B):
    count_A = Counter(A)
    count_B = Counter(B)

    total_moves = 0
    paired = defaultdict(int)

    for a, b in zip(A, B):
        if a == b:
            paired[a] += 1
        else:
            paired[a] += 0.5
            paired[b] += 0.5

    for key in paired:
        total_moves += paired[key] // 1

    if total_moves % 2 == 0:
        return "Aoki"
    else:
        return "Takahashi"


print(game_winner(n, a_l, b_l))


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
