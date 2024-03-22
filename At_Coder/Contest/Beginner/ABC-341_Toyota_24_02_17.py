# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# トヨタ自動車プログラミングコンテスト2024#2（AtCoder Beginner Contest 341）
# https://atcoder.jp/contests/abc341

# -----------------------------
# A Print 341

# n = int(input())
# answer = '1'
# for i in range(n):
#     answer = answer + '01'
# print(answer)

# -----------------------------
# B Foreign Exchange

# n = int(input())
# a = list(map(int, input().split()))
# st = []
# for i in range(n-1):
#     s, t = map(int, input().split())
#     st.append([s, t])

#     a[i+1] += t*(a[i]//s)
# print(a[n-1])

# -----------------------------
# C  Takahashi Gets Lost   TEL ⇒ C++なら行けた
# ope = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # L, R, U, D
# h, w, n = map(int, input().split())
# t = input()
# s = []
# answer = []
# for i in range(h):
#     si = input()
#     s.append(si)
# for i in range(1, h-1):
#     for j in range(1, w-1):
#         if s[i][j] == '#':
#             continue
#         position = [i, j]
#         flag = 0
#         for t_ in t:
#             if t_ == 'L':
#                 position[0] += ope[0][0]
#                 position[1] += ope[0][1]
#             elif t_ == 'R':
#                 position[0] += ope[1][0]
#                 position[1] += ope[1][1]
#             elif t_ == 'U':
#                 position[0] += ope[2][0]
#                 position[1] += ope[2][1]
#             elif t_ == 'D':
#                 position[0] += ope[3][0]
#                 position[1] += ope[3][1]
#             if position[0] < 0 or position[0] >= h or position[1] < 0 or position[1] >= w or s[position[0]][position[1]] == '#':
#                 flag = 1
#                 break
#         if flag == 0:
#             answer.append(position)
# print(len(answer))

# GPT4 参照   TEL------------------------
# def count_possible_positions(H, W, S, T):
#     # 高橋君が不時着した可能性のあるマスの集合を初期化
#     possible_positions = set()
#     for i in range(1, H-1):
#         for j in range(1, W-1):
#             if S[i][j] == '.':
#                 possible_positions.add((i, j))

#     # 各移動に対して、可能なマスの位置を更新
#     post_position = possible_positions
#     for move in T:
#         new_positions = set()
#         for pos in post_position:
#             if move == 'L' and (pos[0], pos[1]-1) in possible_positions:
#                 new_positions.add((pos[0], pos[1]-1))
#             elif move == 'R' and (pos[0], pos[1]+1) in possible_positions:
#                 new_positions.add((pos[0], pos[1]+1))
#             elif move == 'U' and (pos[0]-1, pos[1]) in possible_positions:
#                 new_positions.add((pos[0]-1, pos[1]))
#             elif move == 'D' and (pos[0]+1, pos[1]) in possible_positions:
#                 new_positions.add((pos[0]+1, pos[1]))
#         post_position = new_positions

#         # 移動が不可能な場合は、その時点で探索を終了
#         if not post_position:
#             break

#     # 最終的な可能なマスの数を返す
#     return len(post_position)


# ope = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # L, R, U, D
# h, w, n = map(int, input().split())
# t = input()
# s = []
# answer = []
# for i in range(h):
#     si = input()
#     s.append(si)
# # 関数を実行して結果を得る
# answer = count_possible_positions(h, w, s, t)
# print(answer)


# -----------------------------
# D Only one of two   TEL

# n, m, k = map(int, input().split())
# count = 0
# a = 0
# while (count < k):
#     a += 1
#     check = 0
#     if a % n == 0:
#         check += 1
#     if a % m == 0:
#         check += 1
#     if check == 1:
#         count += 1
# print(a)

# GPT4 参照 最小公倍数，最大公約数の活用   TEL-------------------------
# from math import gcd


# def find_kth_number(N, M, K):
#     # 最大公約数 (GCD) を計算
#     lcm_gcd = gcd(N, M)

#     # 最小公倍数 (LCM) を計算
#     LCM = N * M // lcm_gcd

#     # 1周期あたりの対象となる数の総数を計算
#     count_per_period = LCM // N + LCM // M - 2

#     # K番目の数が全体の中でどの位置にあるかを計算
#     period = (K-1) // count_per_period
#     remainder = (K-1) % count_per_period + 1

#     # K番目の数を見つける
#     num_list = []
#     if N < M:
#         check = N
#         count_n = 2
#         count_m = 1
#     else:
#         check = M
#         count_n = 1
#         count_m = 2
#     for i in range(1, LCM + 1):
#         if (check % N == 0) ^ (check % M == 0):  # XOR: NかMのどちらか一方のみで割り切れる
#             num_list.append(check)
#             if len(num_list) == remainder:
#                 break
#         if count_n*N < count_m*M:
#             check = count_n*N
#             count_n += 1
#         else:
#             check = count_m*M
#             count_m += 1

#     # 実際のK番目の数を計算
#     kth_number = period * LCM + num_list[-1]
#     return kth_number


# n, m, k = map(int, input().split())
# answer = find_kth_number(n, m, k)
# print(answer)


# 解法(2分探索の利用)  AC------------------------------
# from math import gcd

# n, m, k = map(int, input().split())
# gcd = gcd(n, m)
# lcm = n * m // gcd
# l = 1
# r = 2*(10**18)
# while (l < r):
#     x = (l+r)//2
#     # print(f'({l}, {r}), {x}')
#     if (x//n + x//m - (2*(x//lcm))) >= k:
#         r = x
#     else:
#         l = x+1
# print(r)

# -----------------------------
# E Alternating String    WA_1, TEL_29, AC_2_12

# n, q = map(int, input().split())
# s = input()
# ans = []
# for i in range(q):
#     ope, l, r = map(int, input().split())
#     if ope == 1:
#         # maskを作成し，排他的論理和によりビット反転
#         mask = '0'*(l-1)
#         mask = mask+'1'*(r-l+1)
#         mask = mask+'0'*(n-r)
#         s = bin(int(s, 2) ^ int(mask, 2))[2:]
#         if len(s) != n:
#             s = '0'*(n-len(s))+s
#         # print(i, '... s:', s)
#     else:
#         s_ = s[l-1:r]
#         # print(i, '... s:', s)
#         # print('s_:', s_)
#         s_shift = int(s_, 2) >> 1
#         check = bin(int(s_, 2) ^ s_shift)[2:]
#         if check == '1'*len(check) or check == ('0'+'1'*(len(check)-1)):
#             ans.append('Yes')
#         else:
#             ans.append('No')
# for ans_ in ans:
#     print(ans_)


# 解答 ---------------------------
n, q = map(int, input().split())
s = input()
checker = []
ans = []
if len(s) == 1:
    for _ in range(q):
        ope, l, r = map(int, input().split())
        if ope == 2:
            ans.append('Yes')
else:
    for i in range(n-1):
        if s[i+1] == s[i]:
            checker.append(0)
        else:
            checker.append(1)

    for i in range(q):
        ope, l, r = map(int, input().split())
        if ope == 1:
            if l != 1:
                checker[l-2] = 1-checker[l-2]
            if r != n:
                checker[r-1] = 1-checker[r-1]
        else:
            if sum(checker[l-1:r-1]) == (r-l):
                ans.append('Yes')
            else:
                ans.append('No')
for ans_ in ans:
    print(ans_)

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
