# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))

# AtCoder Beginner Contest 338
# https://atcoder.jp/contests/abc338


# バーチャル参加(後日受験)
# -----------------------------
# A Capitalized?

# s = input()
# result = 'Yes'
# for i, s_ in enumerate(s):
#     if i == 0:
#         if ord(s_) >= ord('A') and ord(s_) <= ord('Z'):
#             continue
#         else:
#             result = 'No'
#             break
#     else:
#         if ord(s_) >= ord('a') and ord(s_) <= ord('z'):
#             continue
#         else:
#             result = 'No'
#             break
# print(result)

# -----------------------------
# B Frequency

# s = input()
# count = [0]*26
# for s_ in s:
#     count[ord(s_)-ord('a')] += 1
# frequency = max(count)
# for i, k in enumerate(count):
#     if k == frequency:
#         print(chr(ord('a')+i))
#         break


# -----------------------------
# C Leftover Recipes

# n = int(input())
# q = list(map(int, input().split()))
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# for i in range(n):
#     if a[i] != 0:
#         a_max = q[i]//a[i]
#         break
# for i in range(n):
#     if a[i] != 0:
#         a_max = min(a_max, q[i]//a[i])

# result = 0
# for a_num in range(a_max+1):
#     for i in range(n):
#         if b[i] != 0:
#             b_max = q[i]//b[i]
#             break
#     for i in range(n):
#         if b[i] != 0:
#             q_rest = q[i]-a[i]*a_num
#             b_max = min(b_max, q_rest//b[i])
#     result = max(result, a_num+b_max)
# print(result)

# -----------------------------
# D Island Tour

# TEL ----------
# n, m = map(int, input().split())
# x = list(map(int, input().split()))
# result = (n-1)*m
# for broken in range(1, n+1):  # 壊す橋を全探索
#     count = 0
#     for i, now in enumerate(x):
#         if i == 0:
#             pre = now
#         else:
#             if min(pre, now) <= broken and max(pre, now) > broken:
#                 count += abs(abs(now-pre)-n)
#             else:
#                 count += abs(now-pre)
#             pre = now
#     # print(broken, count)
#     result = min(result, count)
# print(result)

# TEL ⇒ 差分配列の利用により解決 ----------
# n, m = map(int, input().split())
# x = list(map(int, input().split()))
# broken = [0]*n  # 差分配列で管理
# count = 0
# for i, now in enumerate(x):
#     if i == 0:
#         pre = now
#     else:
#         l = min(abs(now-pre), abs(abs(now-pre)-n))
#         count += l
#         diff = abs(abs(abs(now-pre)-n) - abs(now-pre))
#         if l == abs(now-pre):
#             broken[min(pre, now)-1] += diff
#             broken[max(pre, now)-1] -= diff
#             # for k in range(min(pre, now),  max(pre, now)):
#             #     broken[k-1] += abs(abs(now-pre)-n) - abs(now-pre)
#         elif l == abs(abs(now-pre)-n):
#             broken[0] += diff
#             broken[min(pre, now)-1] -= diff
#             broken[max(pre, now)-1] += diff
#             # for k in range(1, min(pre, now)):
#             #     broken[k-1] += abs(now-pre) - abs(abs(now-pre)-n)
#             # for k in range(max(pre, now), n+1):
#             #     broken[k-1] += abs(now-pre) - abs(abs(now-pre)-n)
#         pre = now
# broken_ = [0]*n
# for i, b in enumerate(broken):
#     if i == 0:
#         broken_[i] = b
#     else:
#         broken_[i] = broken_[i-1]+b
# result = count+min(broken_)
# # result = count + min(broken)
# print(result)

# -----------------------------
# E Chords

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
