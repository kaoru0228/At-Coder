# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# モノグサプログラミングコンテスト2024（AtCoder Beginner Contest 345）
# https://atcoder.jp/contests/abc345

# -----------------------------
# A Leftrightarrow

# s = input()
# if s[0] == '<' and s[-1] == '>' and all(element == '=' for element in s[1:-1]):
#     print('Yes')
# else:
#     print('No')

# -----------------------------
# B Integer Division Returns
# n = int(input())
# x = n/10
# print(x)
# if x == int(x) or x < 0:
#     x = int(x)
# elif x >= 0:
#     x = int(x)+1
# print(x)

# GPT -----------------
# from decimal import Decimal, getcontext
# from math import ceil

# x = Decimal(str(input()))

# ans = ceil(x / Decimal(10))

# print(ans)

# 解説の切り上げ演算 --------------------
# n = int(input())
# x = (n + (10 - 1))//10
# print(x)

# -----------------------------
# C One Time Swap
# s = input()
# count = [0]*26
# for s_ in s:
#     count[ord(s_) - ord('a')] += 1

# ans = 0
# for i in range(26):
#     for j in range(i+1, 26):
#         ans += (count[i]*count[j])

# check = 0
# for c in count:
#     if c > 1:
#         check = 1
# ans += check
# print(ans)

# -----------------------------
# D Tiling
# GPT4 WA 全てNoになる
# def can_place(board, h, w, tile, x, y):
#     for i in range(tile[0]):
#         for j in range(tile[1]):
#             if x+i >= h or y+j >= w or board[x+i][y+j]:
#                 return False
#     return True


# def place_tile(board, tile, x, y, value):
#     for i in range(tile[0]):
#         for j in range(tile[1]):
#             board[x+i][y+j] = value


# def backtrack(board, tiles, h, w, idx=0):
#     if idx == len(tiles):
#         return all(all(cell for cell in row) for row in board)

#     tile = tiles[idx]
#     for x in range(h):
#         for y in range(w):
#             for rot in [tile, (tile[1], tile[0])]:  # Try both rotations
#                 if can_place(board, h, w, rot, x, y):
#                     place_tile(board, rot, x, y, True)
#                     if backtrack(board, tiles, h, w, idx+1):
#                         return True
#                     place_tile(board, rot, x, y, False)
#     return False


# def solve(h, w, tiles):
#     board = [[False] * w for _ in range(h)]
#     if backtrack(board, tiles, h, w):
#         return "Yes"
#     else:
#         return "No"


# n, h, w = map(int, input().split())
# tiles = []
# for i in range(n):
#     a, b = map(int, input().split())
#     tiles.append((a, b))

# print(solve(h, w, tiles))

# 解答-----------------------------
# 入力：フラグ，座標
# def solve(unused, curi, curj):
#     if curi >= h:
#         global ans
#         ans = True
#         return

#     if curj >= w:
#         solve(unused, curi + 1, 0)
#         return

#     if c[curi][curj] >= 0:
#         solve(unused, curi, curj + 1)
#         return

#     for i in range(n):
#         if unused & (1 << i):
#             can_place = True
#             for ii in range(a[i]):
#                 for jj in range(b[i]):
#                     if 0 <= curi + ii < h and 0 <= curj + jj < w:
#                         if c[curi + ii][curj + jj] < 0:
#                             c[curi + ii][curj + jj] = i
#                         else:
#                             can_place = False
#                     else:
#                         can_place = False

#             if can_place:
#                 solve(unused ^ (1 << i), curi, curj)

#             for ii in range(a[i]):
#                 for jj in range(b[i]):
#                     if 0 <= curi + ii < h and 0 <= curj + jj < w:
#                         if c[curi + ii][curj + jj] == i:
#                             c[curi + ii][curj + jj] = -1

#             if a[i] != b[i]:  # Try with rotated tile
#                 for ii in range(b[i]):
#                     for jj in range(a[i]):
#                         if 0 <= curi + ii < h and 0 <= curj + jj < w:
#                             if c[curi + ii][curj + jj] < 0:
#                                 c[curi + ii][curj + jj] = i
#                             else:
#                                 can_place = False
#                         else:
#                             can_place = False

#                 if can_place:
#                     solve(unused ^ (1 << i), curi, curj)

#                 for ii in range(b[i]):
#                     for jj in range(a[i]):
#                         if 0 <= curi + ii < h and 0 <= curj + jj < w:
#                             if c[curi + ii][curj + jj] == i:
#                                 c[curi + ii][curj + jj] = -1


# n, h, w = map(int, input().split())
# a, b = [], []
# for _ in range(n):
#     ai, bi = map(int, input().split())
#     a.append(ai)
#     b.append(bi)

# c = [[-1 for _ in range(w)] for _ in range(h)]
# ans = False

# solve((1 << n) - 1, 0, 0)

# if ans:
#     print("Yes")
# else:
#     print("No")

# 解説 --------------------------------

# -----------------------------
# E Colorful Subsequence

n, k = map(int, input().split())
ball = []
value_sum = 0
for i in range(n):
    c, v = map(int, input().split())
    value_sum += v
    ball.append((c, v))

checks = []
check = [ball[0][0], 1]
for i in range(1, n):
    if check[0] == ball[i][0]:
        check[1] += 1
    else:
        checks.append(check)
        check = [ball[i][0], 1]
    if i == n-1:
        checks.append(check)

must = 0
score = 0
i = 0
rest = []
for check in checks:
    must += (check[1]-1)

    values = []
    for j in range(i, i+check[1]):
        values.append(ball[j][1])
        score += ball[j][1]
    score -= max(values)
    rest.append([check[0], max(values)])
    i += check[1]

print(value_sum-score)

if must > k:
    ans = -1
else:
    r = must - k
    dp = [[0]*len(rest) for _ in range(r)]
    for i in range(r):
        for j, c, v in enumerate(zip(rest)):
            if (j == 0 or rest[j-1][0] != c) and (j == (len(rest)-1) or rest[j+1][0] != c):
                dp[i][j] = v

# print(ans)

# 解説 --------------------------------


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
