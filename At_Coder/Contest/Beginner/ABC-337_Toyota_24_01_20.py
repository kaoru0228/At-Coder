# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))

# トヨタ自動車プログラミングコンテスト2024#1（AtCoder Beginner Contest 337）
# https://atcoder.jp/contests/abc337

# -----------------------------
# A Scoreboard

# n = int(input())
# a = 0
# b = 0
# for _ in range(n):
#     x, y = map(int, input().split())
#     a += x
#     b += y
# if a > b:
#     winner = 'Takahashi'
# elif a == b:
#     winner = 'Draw'
# else:
#     winner = 'Aoki'
# print(winner)

# -----------------------------
# B Extended ABC

# s = input()
# result = 'Yes'
# count = 0
# for i, s_ in enumerate(s):
#     if i == 0:
#         pre = s_
#         count += 1
#         continue
#     else:
#         if (pre == 'A') or (pre == 'B' and s_ != 'A') or (pre == 'C' and s_ == 'C'):
#             pre = s_

#         else:
#             result = 'No'
#             break
# print(result)


# ------------------
# s = input()
# if not s:  # 空文字列のチェック
#     result = "Yes"
# else:
#     # A の連続を確認
#     i = 0
#     while i < len(s) and s[i] == 'A':
#         i += 1

#     # B の連続を確認
#     while i < len(s) and s[i] == 'B':
#         i += 1

#     # C の連続を確認
#     while i < len(s) and s[i] == 'C':
#         i += 1

#     # 全ての文字をチェックしたか確認
#     result = "Yes" if i == len(s) else "No"

# print(result)


# -----------------------------
# C Lining Up 2

# n = int(input())
# a = list(map(int, input().split()))

# n = len(a)
# result = []
# position = {}

# for i in range(n):
#     position[a[i]] = i+1
# result.append(position[-1])
# for i in range(n-1):
#     result.append(position[result[i]])
# print(*result)


# -----------------------------
# D Cheating Gomoku Narabe  TEL

# h, w, k = map(int, input().split())
# grid = []
# for i in range(h):
#     s = input()
#     grid.append(s)

# min_ops = float('inf')

# for i in range(h):
#     for j in range(w):
#         # 横方向のチェック
#         if j + k <= w:
#             count_p = 0
#             flag = 0
#             for x in range(j, j + k):
#                 if grid[i][x] == '.':
#                     count_p += 1
#                 elif grid[i][x] == 'x':
#                     flag = 1
#                     break
#             if flag == 0:
#                 min_ops = min(count_p, min_ops)

#         # 縦方向のチェック
#         elif i + k <= h:
#             count_p = 0
#             flag = 0
#             for x in range(i, i + k):
#                 if grid[x][j] == '.':
#                     count_p += 1
#                 elif grid[x][j] == 'x':
#                     flag = 1
#                     break
#             if flag == 0:
#                 min_ops = min(count_p, min_ops)
# result = min_ops if min_ops != float('inf') else -1
# print(result)


# --------------------------------
# def min_operations_to_make_o_sequence(h, w, k, grid):
#     # 前計算：各行と列の'o'の数を計算
#     row_os = [[0 for _ in range(w)] for _ in range(h)]
#     col_os = [[0 for _ in range(h)] for _ in range(w)]

#     # 各行について'o'の数を計算
#     for i in range(h):
#         count = 0
#         for j in range(w):
#             if grid[i][j] == 'o':
#                 count += 1
#             row_os[i][j] = count

#     # 各列について'o'の数を計算
#     for j in range(w):
#         count = 0
#         for i in range(h):
#             if grid[i][j] == 'o':
#                 count += 1
#             col_os[j][i] = count

#     min_ops = float('inf')

#     # 横方向のチェック
#     for i in range(h):
#         for j in range(w - k + 1):
#             if 'x' not in grid[i][j:j + k]:  # 'x'が含まれていないウィンドウのみチェック
#                 count_o = row_os[i][j + k - 1]
#                 count_o -= row_os[i][j - 1] if j > 0 else 0
#                 count_dot = k - count_o
#                 min_ops = min(min_ops, count_dot)

#     # 縦方向のチェック
#     for j in range(w):
#         for i in range(h - k + 1):
#             if 'x' not in [grid[x][j] for x in range(i, i + k)]:  # 'x'が含まれていないウィンドウのみチェック
#                 count_o = col_os[j][i + k - 1]
#                 count_o -= col_os[j][i - 1] if i > 0 else 0
#                 count_dot = k - count_o
#                 min_ops = min(min_ops, count_dot)

#     return min_ops if min_ops != float('inf') else -1

# h, w, k = map(int, input().split())
# grid = []
# for i in range(h):
#     s = input()
#     grid.append(s)

# print(min_operations_to_make_o_sequence(h, w, k, grid))


# -----------------------------
# E

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))


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
