# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# AtCoder Beginner Contest 363
# https://atcoder.jp/contests/abc363

# -----------------------------
# A Piling Up

# r = input()
# if len(r) > 2:
#     r = int(r[1:])
# else:
#     r = int(r)
# ans = 100-r
# print(ans)

# -----------------------------
# B Japanese Cursed Doll

# n, t, p = map(int, input().split())
# l_l = list(map(int, input().split()))

# sorted_l = sorted(l_l, reverse=True)

# least = sorted_l[p-1]

# if least >= t:
#     ans = 0
# else:
#     ans = t - least

# print(ans)


# -----------------------------
# C Avoid K Palindrome 2

# n, k = map(int, input().split())
# s = list(map(int, input().split()))

# GPT 全探索　（10! = 3628800） -----------------------------
# TLE, C++なら行けた

# import itertools


# def is_palindrome(s):
#     return s == s[::-1]


# def count_valid_permutations(N, K, S):
#     permutations = set(itertools.permutations(S))
#     count = 0

#     for perm in permutations:
#         valid = True
#         for i in range(N - K + 1):
#             if is_palindrome(perm[i:i + K]):
#                 valid = False
#                 break
#         if valid:
#             count += 1

#     return count


# N, K = map(int, input().split())
# S = input().strip()

# print(count_valid_permutations(N, K, S))


# -----------------------------
# D Palindromic Number
# 自力、ギリギリ間に合った
# 桁の繰り上がりに注意

# n = int(input())

# if n <= 10:
#     ans = str(n-1)

# elif n <= 19:
#     ans = str(n-10)*2

# else:
#     dp = [0, 9, 9]
#     i = 2
#     count = 19
#     while (count < n):
#         i += 1
#         x = dp[i-2]*10
#         dp.append(x)
#         count += x

#     dp[1] = 10
#     digit = i
#     num = dp[-1]

#     # digit桁における何番目か
#     n_dig = n - (count - dp[-1])

#     # 目的の数字まであと何個か
#     rest = n_dig

#     digit_l = []
#     for i in range(digit//2):
#         if i == 0:
#             num //= 9
#             dig_i = ((rest-1) // num) + 1
#             rest -= (dig_i-1) * num
#         else:
#             num //= 10
#             dig_i = ((rest-1) // num)
#             rest -= dig_i * num

#         digit_l.append(dig_i)

#     if (digit % 2) == 1:
#         dig_i = rest-1
#         digit_l.append(dig_i)

#     ans = ''
#     for d in digit_l:
#         ans += str(d)

#     for i, d in enumerate(reversed(digit_l)):
#         if (digit % 2 == 1) and i == 0:
#             continue
#         ans += str(d)

# print(ans)
# # print(digit_l)

# -----------------------------
# E Sinking Land

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
