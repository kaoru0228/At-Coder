# n, q = map(int, input().split())
# n = int(input())
# s = list(map(int, input().split()))

# 大和証券プログラミングコンテスト2023（AtCoder Beginner Contest 331）
# https://atcoder.jp/contests/abc331

# -----------------------------
# A Tomorrow

# m, d = map(int, input().split())
# y_, m_, d_ = map(int, input().split())
# ans = [0]*3
# if m_ == m and d_ == d:
#     ans[0] = y_+1
#     ans[1] = 1
#     ans[2] = 1
# elif d_ == d:
#     ans[0] = y_
#     ans[1] = m_+1
#     ans[2] = 1
# else:
#     ans[0] = y_
#     ans[1] = m_
#     ans[2] = d_+1
# ans_ = (str(ans[0]) + ' ' + str(ans[1]) + ' ' + str(ans[2]))
# print(ans_)

# -----------------------------
# B Buy One Carton of Milk

#   6, 8, 12
# n, s, m, l = map(int, input().split())
# min_pay = ((n//6)+1)*s
# for i in range((n//6)+2):
#     for j in range(((n-i*6)//8)+2):
#         for k in range(((n-i*6-j*8)//12)+2):
#             if (6*i + 8*j + 12*k) >= n:
#                 pay = s*i + m*j + l*k
#                 if pay < min_pay:
#                     min_pay = pay
# print(min_pay)


# -----------------------------
# C Sum of Numbers Greater Than Me

# n = int(input())
# a_l = list(map(int, input().split()))
# sum_ = sum(a_l)
# ans_dict = {}
# a_sorted = sorted(a_l)
# check = a_sorted[0]
# count = 0
# for i, a in enumerate(a_sorted):
#     if check != a:
#         ans_dict[check] = sum_ - count
#         check = a
#     if i == (len(a_l)-1):
#         ans_dict[a] = 0
#     count += a
# ans = []
# for i in range(n):
#     ans.append(ans_dict[a_l[i]])
# print(*ans)

# -----------------------------
# D Tile Pattern  AC 1_4, WA 1_3, TEL 0_9

# n, q = map(int, input().split())
# p_ll = []
# query_ll = []
# black = 0
# for i in range(n):
#     p_ll.append(input())
#     for p in p_ll[i]:
#         if p == 'B':
#             black += 1
# result = []
# for _ in range(q):
#     query_l = list(map(int, input().split()))

#     height = query_l[2]-query_l[0] + 1
#     width = query_l[3]-query_l[1] + 1

#     count = 0
#     count += (width//n) * (height//n) * black
#     print('h, w, nn :', height, width, count)

#     count_1 = 0
#     count_2 = 0
#     for x in range(query_l[3] - (width % n - 1), query_l[3]+1):
#         for y in range(n):
#             if p_ll[x % n][y] == 'B':
#                 count_1 += 1
#         for y in range(query_l[2] - (height % n - 1), query_l[2]+1):
#             if p_ll[x % n][y % n] == 'B':
#                 count_2 += 1
#     count = count + count_1*(height//n) + count_2
#     print('right:', count_1*(height//n) + count_2)

#     count_1 = 0
#     for x in range(n):
#         for y in range(query_l[2] - (height % n - 1), query_l[2]+1):
#             if p_ll[x][y % n] == 'B':
#                 count_1 += 1
#     count += count_1 * (width//n)
#     print('under:', count_1 * (width//n))
#     print('result:', count)
#     result.append(count)

# for r in result:
#     print(r)

# 2024/03/21 解答参考  何か間違えている
def count_square(black, dp, x, y):
    w = x+1
    h = y+1
    w_count = w // n
    w_rest = w % n
    h_count = h // n
    h_rest = h % n

    a = black * w_count * h_count

    b = 0
    if w_rest != 0:
        b_rest = dp[n-1][w_rest-1]
        b = h_count * b_rest

    c = 0
    if h_rest != 0:
        c_rest = dp[h_rest-1][n-1]
        c = w_count * c_rest

    d = 0
    if w_rest != 0 and h_rest != 0:
        d = dp[h_rest-1][w_rest-1]

    count = a+b+c+d

    return count


n, q = map(int, input().split())
p_ll = []
query_ll = []
black = 0
dp = [[0]*n for _ in range(n)]
for i in range(n):
    p_ll.append(input())
    for j, p in enumerate(p_ll[i]):
        b_w = 1 if p == 'B' else 0
        black += b_w
        pre_i = dp[i-1][j] if i > 0 else 0
        pre_j = dp[i][j-1] if j > 0 else 0
        pre_ij = dp[i-1][j-1] if i > 0 and j > 0 else 0
        dp[i][j] = pre_i + pre_j - pre_ij + b_w

results = []
for _ in range(q):
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0:
        ans = count_square(black, dp, c, d)
    elif a == 0:
        ans = count_square(black, dp, c, d) - \
            count_square(black, dp, c, b-1)
    elif b == 0:
        ans = count_square(black, dp, c, d) - \
            count_square(black, dp, a-1, d)
    else:
        ans = count_square(black, dp, c, d) - count_square(black, dp, c, b-1) - \
            count_square(black, dp, a-1, d) + \
            count_square(black, dp, a-1, b-1)

    results.append(ans)
for res in results:
    print(res)
print(black)

# -----------------------------
# E Set Meal

# n, m, l = map(int, input().split())
# a_l = list(enumerate(list(map(int, input().split()))))
# b_l = list(enumerate(list(map(int, input().split()))))
# a_sorted = sorted(a_l, reverse=True, key=lambda x: x[1])
# b_sorted = sorted(b_l, reverse=True, key=lambda x: x[1])
# cd_l = []
# for _ in range(l):
#     cd = tuple(map(int, input().split()))  # タプルで管理
#     cd_l.append(cd)
# # print(cd_l)
# flag = 0
# for i in range(len(a_l)):
#     a_max = a_sorted[i]
#     for j in range(len(b_l)):
#         b_max = b_sorted[j]
#         if not (a_max[0]+1, b_max[0]+1) in cd_l:
#             a_standard = a_max[1]+b_max[1]
#             flag = 1
#             break
#     if flag == 1:
#         break

# flag = 0
# for i in range(len(b_l)):
#     b_max = b_sorted[i]
#     for j in range(len(a_l)):
#         a_max = a_sorted[j]
#         if not (a_max[0]+1, b_max[0]+1) in cd_l:
#             b_standard = a_max[1]+b_max[1]
#             flag = 1
#             break
#     if flag == 1:
#         break
# # print('a_standard:', (a_max[0]+1, b_max[0]+1), a_standard)
# # print('b_standard:', (a_max[0]+1, b_max[0]+1), b_standard)
# result = a_standard if a_standard >= b_standard else b_standard
# print(result)


# -----------------------------
# F

# n = int(input())
# s = list(map(int, input().split()))


# -----------------------------
# G

# n = int(input())
# s = list(map(int, input().split()))
