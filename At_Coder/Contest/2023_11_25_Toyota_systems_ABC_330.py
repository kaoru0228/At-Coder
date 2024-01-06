# n = int(input())
# s = list(map(int, input().split()))

# トヨタシステムズプログラミングコンテスト2023(AtCoder Beginner Contest 330)
# https://atcoder.jp/contests/abc330

# -----------------------------
# A Counting Passes

# n, l = map(int, input().split())
# a = list(map(int, input().split()))
# result = 0
# for a_ in a:
#     if a_ >= l:
#         result += 1
# print(result)

# -----------------------------
# B Minimize Abs 1 TEL

# n, l, r = map(int, input().split())
# a = list(map(int, input().split()))
# result = []
# for a_ in a:
#     tmp = []
#     for i in range(l, r+1):
#         tmp.append(abs(a_-i))
#     if (min(tmp) + a_) >= l and (min(tmp)+a_) <= r:
#         ans = (min(tmp)+a_)
#     else:
#         ans = (-min(tmp)+a_)
#     result.append(ans)
# s_l = ''
# for i, s_ in enumerate(result):
#     s_l = s_l + str(s_)
#     if i != len(result):
#         s_l = s_l + ' '
# print(s_l)

# ----------------------------- TEL

# n, l, r = map(int, input().split())
# a = list(map(int, input().split()))
# lr = []
# for i in range(l, r+1):
#     lr.append(i)
# result = []
# for a_ in a:
#     x = a_
#     y = a_
#     while ((x not in lr) and (y not in lr)):
#         x += 1
#         y -= 1
#     if x in lr:
#         result.append(x)
#     else:
#         result.append(y)

# s_l = ''
# for i, s_ in enumerate(result):
#     s_l = s_l + str(s_)
#     if i != len(result):
#         s_l = s_l + ' '
# print(s_l)

# ----------------------------- TEL

# n, l, r = map(int, input().split())
# a = list(map(int, input().split()))
# result = ''
# for i, a_ in enumerate(a):
#     if a_ >= l and a_ <= r:
#         result = result + str(a_)
#     elif a_ < l:
#         result = result + str(l)
#     else:
#         result = result + str(r)
#     if i != len(a):
#         result = result + ' '

# print(result)

# 回答
# n, l, r = map(int, input().split())
# a = list(map(int, input().split()))
# result = []
# for i, a_ in enumerate(a):
#     result.append(min(max(l, a_), r))
# print(*result)


# -----------------------------
# C Minimize Abs 2　未解答

# d = int(input())


# -----------------------------
# D Counting Ls　未解答

# n = int(input())
# s_l = []
# for _ in range(n):
#     s_l.append(input())
# for _ in range(n):


# -----------------------------
# E Mex and Update TEL

# n, q = map(int, input().split())
# a_l = list(map(int, input().split()))
# i_l = []
# x_l = []
# for _ in range(q):
#     i, x = map(int, input().split())
#     i_l.append(i)
#     x_l.append(x)
# set_ = set(range(max(a_l)+2))

# for k in range(q):
#     a_l[i_l[k]-1] = x_l[k]
#     set_A = set(a_l)
#     print(min(set_ - set_A))


# -----------------------------
# F Minimize Bounding Square

# n, k = map(int, input().split())
# xy_l = [[], []]
# for _ in range(n):
#     x, y = map(int, input().split())
#     xy_l[0].append(x)
#     xy_l[1].append(y)

# now = [[], [], []]  # xかyか，minかmaxか, min_maxの値
# i = 0
# while True:
#     # print(i, xy_l)
#     width = max(xy_l[0]) - min(xy_l[0])
#     height = max(xy_l[1]) - min(xy_l[1])
#     if width == 0 and height == 0:
#         break
#     now[0] = 0 if (width >= height) else 1
#     now[1], now[2] = (1, min(xy_l[now[0]])) if (xy_l[now[0]].count(min(
#         xy_l[now[0]])) <= xy_l[now[0]].count(max(xy_l[now[0]]))) else (-1, max(xy_l[now[0]]))

#     if xy_l[now[0]].count(now[2]) > (k-i):
#         break
#     i += xy_l[now[0]].count(now[2])
#     xy_l[now[0]] = [x+now[1] if x == now[2] else x for x in xy_l[now[0]]]

#     if i > k:
#         break

# result = max(width, height)
# print(result)


# ---------- もう少し効率的に．（座標のリストをそのまま使用せず，x, yそれぞれの累積ヒストグラム的な表現を活用）

n, k = map(int, input().split())
lim = 10**9
x_l = set()
y_l = set()
x_hist = [0]*(lim+1)
y_hist = [0]*(lim+1)

# ヒストの作成
for _ in range(n):
    x, y = map(int, input().split())
    x_l.add(x)
    y_l.add(y)
    x_hist[x] += 1
    y_hist[y] += 1

x_l = list(x_l)
y_l = list(y_l)
# 累積ヒストへの変換．だだし，minからだけでなく，maxからも
cumulative_hist = [[[0]*(lim+1)]
                   for _ in range(4)]  # x_min, x_max, y_min, y_max
for i in range(lim+1):
    if i != 0:
        cumulative_hist[0][i] = cumulative_hist[0][i-1] + x_hist[i]
        cumulative_hist[1][i] = cumulative_hist[1][i-1] + x_hist[lim-i]
        cumulative_hist[2][i] = cumulative_hist[2][i-1] + y_hist[i]
        cumulative_hist[3][i] = cumulative_hist[3][i-1] + y_hist[lim-i]
diff = [0, 0, 0, 0]  # x, yそれぞれの縮めた数
did = 0  # 試行回数
# cumulative_hist の0~3を探索していき，数が少ない順に追加していく．
while did < k:
    long = 0 if (max(x_l) - min(x_l)) >= (max(y_l) - min(y_l)) else 1

# 一旦諦め．実現できそうだが，コードの作成に時間がかかりすぎ．

# -----------------------------
# G Inversion Squared
