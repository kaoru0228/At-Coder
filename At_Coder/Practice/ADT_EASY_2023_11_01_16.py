# A World Cup

# y = int(input())
# next = y + (4-(y+2) % 4) % 4
# print(next)


# -----------------------------
# B Find Takahashi

# n = int(input())
# heights = list(map(int, input().split()))
# max = heights[0]
# max_i = 1
# for i, h in enumerate(heights):
#     if h > max:
#         max = h
#         max_i = i+1
# print(max_i)


# -----------------------------
# C Trimmed Mean

# n = int(input())
# points = list(map(int, input().split()))
# points.sort()
# result = 0
# for i in range(3*n):
#     result += points[i+n]
# result = result/(3*n)
# print(result)


# -----------------------------
# D Roulette

# n = int(input())
# c_l = []
# a_ll = []
# pre_results = []
# results = []
# for _ in range(n):
#     c_l.append(int(input()))
#     a_ll.append(list(map(int, input().split())))
# x = int(input())

# num = []
# for i, a_l in enumerate(a_ll):
#     for a in a_l:
#         if a == x:
#             pre_results.append(i+1)
#             num.append(len(a_l))

# for i, k in enumerate(num):
#     if k == min(num):
#         results.append(pre_results[i])


# print(len(results))
# result_ = ' '.join(str(result) for result in results)
# print(result_)

# -----------------------------
# E abc285_brutmhyhiizp
# ※アルファベットは26種
# ord()で，ASCIIコードを取得

q_num_s = input()

q_num_i = 0
if len(q_num_s) != 1:
    for i in range(1, len(q_num_s)):
        q_num_i += 26**i

for i, t in enumerate(q_num_s):
    q_num_i += ((ord(t) - ord('A')) * 26 ** (len(q_num_s) - (i+1)))
q_num_i += 1
print(q_num_i)
