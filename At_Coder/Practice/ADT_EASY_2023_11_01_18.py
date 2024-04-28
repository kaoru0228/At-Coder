# A Middle Letter

# s = input()
# print(s[(len(s)+1)//2-1])


# -----------------------------
# B Find Multiple

# x_l = list(map(int, input().split()))
# result = -1
# for i in range(1000//x_l[2]):
#     d = x_l[2]*(i+1)
#     if d >= x_l[0] and d <= x_l[1]:
#         result = d
#         break
# print(result)


# -----------------------------
# C KEYENCE building  1/10エラーにより0点 （修正完了　removeが悪さしてた）
# S = 4ab + 3a + 3b ※ a, bは自然数

n = int(input())
s_l = list(map(int, input().split()))
s_ok = []

for a in range((1000//7)+1):
    for b in range((1000//7)+1):
        for s in s_l:
            if (4*(a+1)*(b+1) + 3*(a+1) + 3*(b+1)) == s:
                s_ok.append(s)
for ok in s_ok:
    if ok in s_l:
        s_l.remove(ok)
print(len(s_l))


# -----------------------------
# D Tournament Result

# n = int(input())
# a_l = []
# a_ll = []
# result = 'correct'
# for _ in range(n):
#     a_l.append(input())
# for a in a_l:
#     test_l = []
#     for s in a:
#         test_l.append(s)
#     a_ll.append(test_l)

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         elif (a_ll[i][j] == 'W' and a_ll[j][i] == 'L') or (a_ll[i][j] == 'L' and a_ll[j][i] == 'W') or (a_ll[i][j] == 'D' and a_ll[j][i] == 'D'):
#             continue
#         else:
#             result = 'incorrect'
#             break
# print(result)


# -----------------------------
# E Secret Number
# def fac(n):
#     result = 1
#     for i in range(n):
#         result = result*(i+1)
#     return result


# def conv(n, r):
#     if n < r:
#         ncr = 0
#     else:
#         ncr = fac(n)//(fac(n-r)*fac(r))
#     return ncr


# ss = input()
# o = []
# x = []
# unknown = []
# for i, s in enumerate(ss):
#     if s == 'o':
#         o.append(i)
#     elif s == 'x':
#         x.append(i)
#     else:
#         unknown.append(i)

# if len(x) == 10 or len(o) > 4:
#     result = 0
# elif len(o) == 4:
#     result = 24
# elif len(o) == 3:
#     result = len(unknown)*24 + 36
# elif len(o) == 2:
#     result = 14 + 36*len(unknown) + 24*conv(len(unknown), 2)
# elif len(o) == 1:
#     result = 1 + 14*len(unknown) + 36*conv(len(unknown), 2
#                                            ) + 24*conv(len(unknown), 3)
# elif len(o) == 0:
#     result = len(unknown) + 14*conv(len(unknown), 2) + 36 * \
#         conv(len(unknown), 3) + 24*conv(len(unknown), 4)
# print(result)
