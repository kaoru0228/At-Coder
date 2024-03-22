# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# HUAWEI Programming Contest 2024（AtCoder Beginner Contest 342）
# https://atcoder.jp/contests/abc342

# -----------------------------
# A Yay!
# s = input()
# ans = 1
# for i in range(len(s)):
#     if s[i+1] != s[ans-1]:
#         if i == 0 and s[i+1] == s[i+2]:
#             ans = 1
#             break
#         ans = i+2
#         break
# print(ans)

# -----------------------------
# B Which is ahead?

# n = int(input())
# p = list(map(int, input().split()))
# person = {}
# for i in range(len(p)):
#     person[p[i]] = i

# q = int(input())
# ans = []
# for i in range(q):
#     a, b = map(int, input().split())
#     if person[a] < person[b]:
#         ans.append(a)
#     else:
#         ans.append(b)
# for ans_ in ans:
#     print(ans_)

# -----------------------------
# C Many Replacement

# n = int(input())
# s = input()
# q = int(input())

# char_map = [set(chr(i + ord('a'))) for i in range(26)]
# for i in range(q):
#     c, d = input().split()
#     tmp = char_map[ord(c) - ord('a')]
#     # tmp.add(c)
#     char_map[ord(c) - ord('a')] = set()
#     char_map[ord(d) - ord('a')].update(tmp)

# result = ''
# for s_ in s:
#     for i, uni in enumerate(char_map):
#         if s_ in uni:
#             result = result+chr(ord('a')+i)
# print(result)


# -----------------------------
# D Square Pair   TEL
# import math

# n = int(input())
# a = list(map(int, input().split()))
# count = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         if i == j:
#             continue
#         tmp = math.sqrt(a[i]*a[j])
#         if tmp.is_integer():
#             count += 1
# print(count)


# 解答  TEL 11 WA 1
n = int(input())
a = list(map(int, input().split()))
count0 = 0
count = {}
for ai in a:
    if ai == 0:
        count0 += 1
        continue
    # sqrtはやめて，入力の最大値 2×10^5 の平方根をとする．
    for d in range(min(ai//2, 447), 0, -1):
        if ai % (d*d) == 0:
            if (ai//(d*d)) in count.keys():
                count[ai//(d*d)] += 1
            else:
                count[ai//(d*d)] = 1
            break

tmp = 1
for i in range(1, count0+1):
    tmp *= (n-i)
ans = tmp if count0 != 0 else 0

for x in count.values():
    if x != 0:
        tmp = (x*(x-1))//2
        ans += tmp
print(ans)

# -----------------------------
# E Last Train

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
