# n, x = map(int, input().split())
# list = list(map(int, input().split()))


# Ｓｋｙ株式会社プログラミングコンテスト2023（AtCoder Beginner Contest 329）
# https://atcoder.jp/contests/abc329


# -----------------------------
# -----------------------------
# A Spread

# s = input()
# s_l = ''
# for i, s_ in enumerate(s):
#     s_l = s_l + s_
#     if i != len(s):
#         s_l = s_l + ' '
# print(s_l)


# -----------------------------
# -----------------------------
# B Next

# n = int(input())
# a_l = set(map(int, input().split()))
# max_ = max(a_l)
# a_l.discard(max_)
# print(max(a_l))

# -----------------------------
# -----------------------------
# C Count xxx  AC 16/20, TLE 3/20, MLE 1/20

# n = int(input())
# s = input()
# result = {s[0]}
# check = 1
# for i in range(1, len(s)):
#     if s[i] == s[i-1]:
#         check += 1
#         if not s[i]*check in result:
#             result.add(s[i]*check)
#     else:
#         check = 1
#         if not s[i] in result:
#             result.add(s[i])
# print(len(result))
# # print(result)

# 解答：やはり探索していては実行時間超過となる．
# 　　　よって，a~zの26文字に対して，各々が最大で何回ずつ連続するかを調べ，その回数をもとに解を導出する．
# n = int(input())
# s = input()
# counts = [0]*26
# counts[ord(s[0])-ord('a')] = 1
# count = 1
# for i in range(len(s)-1):
#     if s[i] == s[i+1]:
#         count += 1
#         if (i == len(s)-2) and counts[ord(s[i])-ord('a')] < count:
#             counts[ord(s[i])-ord('a')] = count
#     else:
#         if counts[ord(s[i])-ord('a')] < count:
#             counts[ord(s[i])-ord('a')] = count
#         count = 1
#         if (i == len(s)-2) and counts[ord(s[i+1])-ord('a')] == 0:
#             counts[ord(s[i+1])-ord('a')] = 1

# print(sum(counts))
# # print(counts)

# -----------------------------
# -----------------------------
# D Election Quick Report

# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# vote = [0]*n
# for i in range(m):
#     vote[a[i]-1] += 1
#     if i == 0:
#         print(a[i])
#         past = a[i]
#     else:
#         if vote[past-1] > vote[a[i]-1]:
#             print(past)
#         elif vote[past-1] == vote[a[i]-1]:
#             if past < a[i]:
#                 print(past)
#             else:
#                 print(a[i])
#                 past = a[i]
#         elif vote[past-1] < vote[a[i]-1]:
#             print(a[i])
#             past = a[i]


# -----------------------------
# -----------------------------
# E Stamp

# n, m = map(int, input().split())
# s = input()
# t = input()
# hash_tag = '#'*n


# -----------------------------
# -----------------------------
# F Colored Ball  AC 34/44, TLE 10/44
# n, q = map(int, input().split())
# box = list(map(set, input().split()))
# query = []
# for _ in range(q):
#     query.append(list(map(int, input().split())))

# for que in query:
#     box[que[1]-1] = box[que[1]-1].union(box[que[0]-1])
#     box[que[0]-1].clear()
#     print(len(box[que[1]-1]))

# -----------------------------
# -----------------------------
# G
