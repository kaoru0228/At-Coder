# n = int(input())
# s = list(map(int, input().split()))

# -----------------------------
# A chukodai

# s = input()
# ab = list(map(int, input().split()))
# s_l = []
# for s_ in s:
#     s_l.append(s_)
# result = []
# for i, s_ in enumerate(s_l):
#     if (i+1) == ab[0]:
#         result.append(s_l[ab[1]-1])
#     elif (i+1) == ab[1]:
#         result.append(s_l[ab[0]-1])
#     else:
#         result.append(s_)
# result_s = result[0]
# for i in range(1, len(result)):
#     result_s = result_s + result[i]
# print(result_s)


# -----------------------------
# B T-shirt

# abcx = list(map(int, input().split()))
# if abcx[3] <= abcx[0]:
#     result = 1  # 1.0
# elif (abcx[3] > abcx[0]) and (abcx[3] <= abcx[1]):
#     result = abcx[2] / (abcx[1] - abcx[0])
# else:
#     result = 0
# print(result)


# -----------------------------
# C Same Name

# n = int(input())
# st_l = []
# flag = False
# for _ in range(n):
#     st_l.append(list(map(str, input().split())))
# for i, st1 in enumerate(st_l):
#     for j, st2 in enumerate(st_l):
#         if (i < j) and (st1 == st2):
#             flag = True
#             break
# if flag:
#     print('Yes')
# else:
#     print('No')

# 集合の利用 -------------------
# n = int(input())
# s_ll = list((input()) for i in range(n))
# s_ll_u = set(s_ll)
# if len(s_ll) == len(s_ll_u):
#     print('No')
# else:
#     print('Yes')

# -----------------------------
# D Counting Arrays 実行時間制限オーバー(実行時間：2.2s/制限：2s)

# n = int(input())
# l_ll = []
# same_ll = []
# for _ in range(n):
#     l_ll.append(list(map(int, input().split())))

# for i in range(len(l_ll)):
#     same_l = [i]
#     for j in range((i+1), len(l_ll)):
#         if l_ll[i] == l_ll[j]:
#             same_l.append(j)
#     same_ll.append(same_l)

# count = 0
# for same_ in same_ll:
#     if len(same_) == 1:
#         count += 1
# print(count)

# 回答--------------------
# setは集合表現で，重複する値を持たない．
# N = int(input())
# print(len(set(input() for i in range(N))))

# -----------------------------
# E Monotonically Increasing

# nm = list(map(int, input().split()))
# for i in range(nm[1]-(nm[0]-1)):


# 回答 --------------------

def dfs(A):
    if len(A) == N:
        print(*A)
        return
    if len(A) == 0:
        start = 1
    else:
        start = A[-1]+1
    for i in range(start, M+1):
        dfs(A+[i])


N, M = map(int, input().split())
dfs([])
