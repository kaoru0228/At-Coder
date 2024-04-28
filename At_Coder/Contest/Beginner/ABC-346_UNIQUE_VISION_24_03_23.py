# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# Contest名
# URL

# -----------------------------
# A Adjacent Product

# n = int(input())
# a_l = list(map(int, input().split()))
# b = []
# for i in range(len(a_l)-1):
#     b.append(a_l[i]*a_l[i+1])
# print(*b)


# -----------------------------
# B Piano
# w, b = map(int, input().split())
# dp = [[0]*12 for _ in range(12)]
# piano = 'wbwbwwbwbwbw'
# for i in range(12):
#     w_i = 0
#     b_i = 0
#     for j in range(12):
#         if piano[(i+j) % 12] == 'w':
#             w_i += 1
#         else:
#             b_i += 1
#         dp[i][j] = (w_i, b_i)

# num = (w+b) // 12
# w = w - 7*num
# b = b - 5*num

# flag = False
# for dp_ in dp:
#     if flag:
#         break
#     for w_check, b_check in dp_:
#         if w_check == w and b_check == b:
#             flag = True
#             break
# ans = 'Yes' if flag else 'No'
# print(ans)

# -----------------------------
# C Σ

# n, k = map(int, input().split())
# a_l = list(map(int, input().split()))
# check = set()
# for a in a_l:
#     if a <= k:
#         check.add(a)
# ans = (k*(k+1)//2) - sum(list(check))
# print(ans)


# -----------------------------
# D Gomamayo Sequence  TLE
# n = int(input())
# s = input()
# c_l = list(map(int, input().split()))
# sum_c = sum(c_l)

# dp = [[float('inf')]*n for _ in range(n-1)]
# res = []

# for i in range(n-1):
#     dp[i][0] = 0
#     pre = s[0]
#     for j in range(n):
#         if j == (i+1):
#             if s[j] == pre:
#                 dp[i][j] = dp[i][j-1]
#             else:
#                 dp[i][j] = dp[i][j-1] + c_l[j]
#         else:
#             if j != 0:
#                 if s[j] == pre:
#                     dp[i][j] = dp[i][j-1] + c_l[j]
#                 else:
#                     dp[i][j] = dp[i][j-1]
#                 pre = str(int(pre) ^ 1)
#     res.append(min(dp[i][-1], sum_c - dp[i][-1]))
# print(min(res))

# 解説あり ok!! 惜しかった．．．--------------------
# dp_l0[i] は s[0]~s[i]，までが 01010... となる最小コスト
# dp_l1[i] は s[0]~s[i]，までが 10101... となる最小コスト
# dp_r0[i] は s[-1]~s[i+1]，までが ...01010 となる最小コスト
# dp_r1[i] は s[-1]~s[i+1]，までが ...10101 となる最小コスト
# これらを利用すれば O(2N)で解ける．
# n = int(input())
# s = input()
# c_l = list(map(int, input().split()))
# sum_c = sum(c_l)
# dp_l0 = [0]*n
# dp_l1 = [0]*n
# dp_r0 = [0]*n
# dp_r1 = [0]*n
# for i in range(n):
#     c0 = str(i % 2)
#     c1 = str((i+1) % 2)

#     if s[i] != c0:
#         dp_l0[i] = dp_l0[i-1]+c_l[i] if i != 0 else c_l[i]
#     else:
#         dp_l0[i] = dp_l0[i-1] if i != 0 else 0

#     # if s[i] != c1:
#     #     dp_l1[i] = dp_l1[i-1]+c_l[i] if i != 0 else c_l[i]
#     # else:
#     #     dp_l1[i] = dp_l1[i-1] if i != 0 else 0

#     j = -1*(i+1)
#     if s[j] != c0:
#         dp_r0[j] = dp_r0[j+1]+c_l[j] if i != -1 else c_l[j]
#     else:
#         dp_r0[j] = dp_r0[j+1] if j != -1 else 0

#     if s[j] != c1:
#         dp_r1[j] = dp_r1[j+1]+c_l[j] if j != -1 else c_l[j]
#     else:
#         dp_r1[j] = dp_r1[j+1] if j != -1 else 0

# min_ans = float('inf')
# for i in range(n-1):
#     if n % 2 == 1:
#         cost = dp_l0[i]+dp_r1[i+1]
#     else:
#         cost = dp_l0[i]+dp_r0[i+1]
#     min_ans = min(min_ans, min(cost, sum_c-cost))
# print(min_ans)


# -----------------------------
# E Paint
# 解説あり RE
h, w, m = map(int, input().split())
query = []
for i in range(m):
    t, a, x = map(int, input().split())
    query.append((i, t, a, x))

count = [0]*2*(10**5)
check_w = [False]*h
check_h = [False]*w

rw = h
rh = w
k = 0
for i in range(1, m+1):
    _, t, a, x = query[-1*i]
    a -= 1
    if t == 1:
        if check_w[a]:
            continue
        k += 1 if count[x] == 0 and rh > 0 else 0
        rw -= 1 if rw > 0 else 0
        count[x] += rh
        check_w[a] = True
    else:
        if check_h[a]:
            continue
        k += 1 if count[x] == 0 and rw > 0 else 0
        rh -= 1 if rh > 0 else 0
        count[x] += rw
        check_h[a] = True

k += 1 if count[0] == 0 and rw*rh > 0 else 0
count[0] += rw*rh

print(k)
for i, c in enumerate(count):
    if c > 0:
        print(i, c)


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
