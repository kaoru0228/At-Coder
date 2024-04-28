# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# AtCoder Beginner Contest 347
# https://atcoder.jp/contests/abc347

# -----------------------------
# A Divisible

# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# ans = []
# for a_ in a:
#     if a_ % k == 0:
#         ans.append(a_//k)
# print(*ans)

# -----------------------------
# B Substring

# s = input()
# check = set()
# for i in range(len(s)):
#     for j in range(i+1, len(s)+1):
#         check.add(s[i:j])
# print(len(check))

# -----------------------------
# C Ideal Holidays
# 解説あり WA, TLE, MLE
# n, a, b = map(int, input().split())
# d_l = list(map(int, input().split()))
# week = [False]*(a+b)
# week_num = []
# for d in d_l:
#     if not week[d % (a+b)]:
#         week[d % (a+b)] = True
#         week_num.append(d % (a+b))

# week_num.sort()
# flag = 0
# if len(week_num) == 1:
#     flag = 1
# else:
#     for i in range(len(week_num)):
#         if (week_num[(i+1) % len(week_num)] - week_num[i] + (a+b)) % (a+b) > b:
#             flag = 1
#             break
# ans = 'Yes' if flag == 1 else 'No'
# print(ans)


# 解き直し AC なんでこっちがいけて上のがいけないのかわからん．weekという真偽値のリストを使うのやめただけ．
# n, a, b = map(int, input().split())
# d_l = list(map(int, input().split()))
# week_num = []
# for d in d_l:
#     week_num.append(d % (a+b))

# week_num = list(set(week_num))
# week_num.sort()
# flag = 0
# if len(week_num) == 1:
#     flag = 1
# else:
#     for i in range(len(week_num)):
#         if (week_num[(i+1) % len(week_num)] - week_num[i] + (a+b)) % (a+b) > b:
#             flag = 1
#             break
# ans = 'Yes' if flag == 1 else 'No'
# print(ans)


# -----------------------------
# D Popcount and XOR

# a, b, c = map(int, input().split())

# c_bi = bin(c)[2:]
# c_pop = c_bi.count('1')

# flag = False
# if a+b <= 60:
#     if abs(a-b) <= c_pop and c_pop <= a+b:
#         if c_pop % 2 == (a+b) % 2:
#             flag = True
# else:
#     if abs(a-b) <= c_pop and c_pop <= (120-(a+b)):
#         if c_pop % 2 == (120-a+b) % 2:
#             flag = True
# if flag:
#     x = '1'*a + '0'*(60-a)
#     if a+b <= 60:
#         over = ((a+b) - c_pop)//2
#     else:
#         over = ((120-(a+b)) - c_pop)//2

#     x = [0]*60
#     y = [0]*60
#     c_binary = '0'*(60-len(c_bi)) + c_bi
#     print(a, b, over)
#     for i, c in enumerate(c_binary):
#         if c == '1':
#             if a > 0:
#                 x[i] = '1'
#                 y[i] = '0'
#                 a -= 1
#             elif b > 0:
#                 x[i] = '0'
#                 y[i] = '1'
#                 b -= 1
#         else:
#             if over > 0:
#                 x[i] = '1'
#                 y[i] = '1'
#                 a -= 1
#                 b -= 1
#                 over -= 1
#     # print(a, b, over)
#     # print(x)
#     # print(y)

#     for i, c in enumerate(c_binary):
#         if x[i] != 0:
#             continue
#         if c == '0':
#             if a > 0 and b > 0:
#                 x[i] = '1'
#                 y[i] = '1'
#                 a -= 1
#                 b -= 1
#             else:
#                 x[i] = '0'
#                 y[i] = '0'
#     # print(x)
#     # print(y)
#     x_ans = ''
#     y_ans = ''
#     for i in range(60):
#         x_ans = x_ans + x[i]
#         y_ans = y_ans + y[i]

#     # print(x_ans)
#     # print(y_ans)
#     print(int(x_ans, 2), int(y_ans, 2))

# else:
#     print(-1)
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
