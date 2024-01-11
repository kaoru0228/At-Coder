# トヨタ自動車プログラミングコンテスト2023#7(AtCoder Beginner Contest 328)
# https://atcoder.jp/contests/abc328


# -----------------------------
# -----------------------------
# A Not Too Hard

# n, x = map(int, input().split())
# s_l = list(map(int, input().split()))
# result = 0
# for s in s_l:
#     if s<=x:
#         result += s
# print(result)


# -----------------------------
# -----------------------------
# B 11-11

# n = int(input())
# d_l = list(map(int, input().split()))
# result = 0
# for i in range(1, n+1):
#     i_str = str(i)
#     if len(i_str)>1:
#         if not all(char == i_str[0] for char in i_str):
#             continue
#     for j in range(1, d_l[i-1]+1):
#         j_str = str(j)
#         if not all(char == i_str[0] for char in j_str):
#             continue
#         else:
#             result += 1
# print(result)
# # 解説による補足：月日を連結した文字列を作成し，それを集合に変換すれば，ぞろ目の時のみ集合の要素数が１となる．


# # 解説：setの利用で使用されている文字列の種類数をチェック ------
# n = int(input())
# d_l = list(map(int, input().split()))
# result = 0
# for i in range(1, 10):
#     if i < n and i < d_l[i-1]:
#         result += 1
#     if i < n and i*11 < d_l[i-1]:
#         result += 1
#     if i*11 < n and i < d_l[i*11-1]:
#         result += 1
#     if i*11 < n and int(str(i)+str(i)) < d_l[i*11-1]:
#         result += 1
# print(result)


# -----------------------------
# -----------------------------
# C Consecutive  TLE

# def find(s):
#     answer = 0
#     for i in range(len(s)-1):
#         if s[i] == s[i+1]:
#             answer += 1
#     return answer

# n, q = map(int, input().split())
# s = input()
# l_l = []
# r_l = []
# for _ in range(q):
#     k = list(map(int, input().split()))
#     l_l.append(k[0])
#     r_l.append(k[1])

# for i in range(q):
#     s_now = s[l_l[i]-1:r_l[i]]
#     print(find(s_now))


# re-test(解説と同じ考え)：質問のたびに探索するのは，O(q*N)かかってしまう．
# よって，予め答えを作成しておいて，最後に質問から参照する．
# n, q = map(int, input().split())
# s = input()
# l_l = []
# r_l = []
# for _ in range(q):
#     k = list(map(int, input().split()))
#     l_l.append(k[0])
#     r_l.append(k[1])
# answer = [0] # 長さが n で，i番目の要素には 1~i までの文字列に含まれる連続文字の数が格納．※answer[0]は0
# count = 0
# for i in range(n-1):
#     if s[i] == s[i+1]:
#         count += 1
#     answer.append(count)
# for i in range(q):
#     print(answer[r_l[i]-1]-answer[l_l[i]-1])
# print(answer)


# -----------------------------
# -----------------------------
# D Take ABC  TLE

# s = input()
# while('ABC' in s):
#     for i in range(len(s)-2):
#         if (s[i] == 'A') and (s[i+1] == 'B') and (s[i+2] == 'C'):
#             if len(s)>(i+2):
#                 s = s[:i] + s[i+3:]
#                 break
#             else:
#                 s = s[:i]
#                 break
# print(s)


# # 解説：連続するABC以外の文字を新たな文字列に追加していく．
# #      元の文字列に対するABCの探索と削除ではO(N²)となり実行時間エラーしてしまう．--------
# s = input()
# result = ''
# for s_ in s:
#     result = result + s_
#     if len(result)>=3 and result[-3:]=='ABC':
#         result = result[:-3]
# print(result)


# -----------------------------
# -----------------------------
# E Modulo MST
n, m, k = map(int, input().split())
u_l = []
v_l = []
w_l = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    u_l.append(tmp[0])
    v_l.append(tmp[1])
    w_l.append(tmp[2])

w_idx = list(enumerate(w_l))
w_sorted = sorted(w_idx, key=lambda x: x[1])

select = []
union = [-1]*n
count = 0
union_count = 1

while (len(select) != (n-1)):
    u_uni = union[u_l[w_sorted[count][0]]-1]
    v_uni = union[v_l[w_sorted[count][0]]-1]
    if ((u_uni == -1) and (v_uni == -1)):
        union[u_l[w_sorted[count][0]]-1] = union_count
        union[v_l[w_sorted[count][0]]-1] = union_count
        select.append(w_sorted[count])
        union_count += 1

    elif (u_uni == -1):
        union[u_l[w_sorted[count][0]]-1] = v_uni
        select.append(w_sorted[count])

    elif (v_uni == -1):
        union[v_l[w_sorted[count][0]]-1] = u_uni
        select.append(w_sorted[count])

    elif (u_uni != v_uni):
        union = [u_uni if (value == v_uni) else value for value in union]
        select.append(w_sorted[count])

    count += 1

result = 0
for i in range(len(select)):
    result += select[i][1]
print(result % k)


# -----------------------------
# -----------------------------
# F


# -----------------------------
# -----------------------------
# G
