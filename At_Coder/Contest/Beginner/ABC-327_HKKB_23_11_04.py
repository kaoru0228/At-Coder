# n, x = map(int, input().split())
# list = list(map(int, input().split()))

# https://atcoder.jp/contests/abc327
# HHKBプログラミングコンテスト2023(AtCoder Beginner Contest 327)

# -----------------------------
# A ab

# n = int(input())
# s = input()
# result = 'No'
# for i, s_ in enumerate(s):
#     if i != (len(s)-1):
#         if (s_ == 'a' and s[i+1] == 'b') or (s_ == 'b' and s[i+1] == 'a'):
#             result = 'Yes'
#             break
# print(result)


# -----------------------------
# -----------------------------
# B A^A

# 最大値の確認
# k = 1
# while k**k < 10**18:
#     k += 1
# print(k, ':', k**k) # 16 : 18446744073709551616

# # 本題
# b = int(input())
# result = -1
# for i in range(1, 16+1):
#     if i**i == b:
#         result = i
#         break
# print(result)


# -----------------------------
# -----------------------------
# C Number Place

# a_l = []
# for i in range(9):
#     a = list(map(int, input().split()))
#     a_l.append(a)
# check = [set() for _ in range(27)]
# # check_l = [[] for _ in range(27)]
# for i in range(9):
#     for k in range(9): # row
#         check[k].add(a_l[k][i])
#     for k in range(9): # colmn
#         check[k+9].add(a_l[i][k])
#     for k in range(9): # cell
#         check[k+18].add(a_l[((k//3)*3)+(i//3)][((k%3)*3)+(i%3)])
 
# result = 'Yes'
# for i in range(27):
#     # print(i, ' : ', check[i])
#     if len(check[i]) != 9:
#         result = 'No'
#         break
# print(result)

# -----------------------------
# -----------------------------
# D Good Tuple Problem

# これでは，相互作用が認識できていない．つまり，abともに-1だった時に0, 1のどちらをabのどちらに入れるかで結果が変わってしまう．
# n, m = map(int, input().split())
# a_l = list(map(int, input().split()))
# b_l = list(map(int, input().split()))
# x = [-1]*n
# result = 'Yes'
# for i in range(m):
#     print(i+1, ':', x)
#     if a_l[i] == b_l[i]:
#         result = 'No'
#         break
#     elif x[a_l[i]-1] == -1 and x[b_l[i]-1] == -1:
#         x[a_l[i]-1] = 0
#         x[b_l[i]-1] = 1
#     elif x[a_l[i]-1] == -1 or x[b_l[i]-1] == -1:
#         if x[a_l[i]-1] == -1:
#             x[a_l[i]-1] = 1 - x[b_l[i]-1]
#         else:
#             x[b_l[i]-1] = 1 - x[a_l[i]-1]
#     elif x[a_l[i]-1] + x[b_l[i]-1] == 1:
#         continue
#     else:
#         result = 'No'
#         print(i+1, ':', a_l[i], b_l[i])
#         break
# print(result)
# print(x)

# 解説　2部グラフを用いて考える．N個の頂点に対して，a[i], b[i]を辺で結んでいき，最終的に辺で結ばれた頂点が異なる値となれば良い．
# 深さ優先探索

def dfs(c, t, result, x, relat): #cは現在の未探索頂点，tは現在の頂点に与えるグループ名，xはグループ名を記録するリスト，relatは連結を表すリスト
    x[c] = t
    for d in relat[c]:
        if x[d] == -1:
            dfs(d, 1-t, result, x, relat)
        elif x[d] == t:
            result[0] = 'No'

n, m = map(int, input().split())
a_l = list(map(int, input().split()))
b_l = list(map(int, input().split()))
x = [-1]*n
relat = [[] for _ in range(n)]

for i in range(m):
    relat[a_l[i]-1].append(b_l[i]-1)
    relat[b_l[i]-1].append(a_l[i]-1)

result = ['Yes']
for i in range(n):
    if x[i] == -1:
        dfs(i, 0, result, x, relat)
    if result[0] == 'No':
        break
print(result[0])



# -----------------------------
# -----------------------------
# E 


# -----------------------------
# -----------------------------
# F 



# -----------------------------
# -----------------------------
# G