# n = int(input())
# s = list(map(int, input().split()))

# -----------------------------
# A Distinct Strings

# s = input()
# s_list = []
# count_l = []

# for s_ in s:
#     s_list.append(s_)


# for s_1 in s_list:
#     count = 0
#     for s_2 in s_list:
#         if s_2 == s_1:
#             count += 1
#     count_l.append(count)

# result = 1
# for i in range(max(count_l)):
#     result = result*(i+1)
# result = int(6/result)
# print(result)


# -----------------------------
# B Adjacent Squares

# hw = list(map(int, input().split()))
# rc = list(map(int, input().split()))

# if hw[0] == 1 or hw[1] == 1:
#     if hw[0] == 1 and hw[1] == 1:
#         result = 0
#     elif (rc[0] == 1 and rc[1] == 1) or (rc[0] == 1 and rc[1] == hw[1]) or (rc[0] == hw[0] and rc[1] == 1):
#         result = 1
#     else:
#         result = 2

# else:
#     if ((rc[0] == 1) or (rc[0] == hw[0])) and ((rc[1] == 1) or (rc[1] == hw[1])):
#         result = 2
#     elif ((rc[0] == 1) or (rc[0] == hw[0])) or ((rc[1] == 1) or (rc[1] == hw[1])):
#         result = 3
#     else:
#         result = 4
# print(result)


# -----------------------------
# C Chessboard
# s_ll = []
# for _ in range(8):
#     s_tmp = input()
#     s_l = []
#     for s in s_tmp:
#         s_l.append(s)
#     s_ll.append(s_l)
# for i, s_l in enumerate(s_ll):
#     for j, s in enumerate(s_l):
#         if s == '*':
#             position = [i, j]
# pos_row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# pos_col = [1, 2, 3, 4, 5, 6, 7, 8]
# result_row = pos_row[position[1]]
# result_col = str(pos_col[7-position[0]])

# print(result_row + result_col)


# -----------------------------
# D Sandwich Number　（エラー１つにより時間切れ．文字をintにしようとするのがダメだった．解決済み）

# s = input()
# s_l = []
# for s_ in s:
#     s_l.append(s_)
# if len(s_l) != 8:
#     result = 'No'
# else:
#     number = s_l[1]+s_l[2]+s_l[3]+s_l[4]+s_l[5]+s_l[6]
#     if number.isdigit():
#         number = int(number)
#     if isinstance(number, int) and (ord(s_l[0]) >= 65 and ord(s_l[0]) <= 90) and (ord(s_l[7]) >= 65 and ord(s_l[7]) <= 90) and (number >= 100000) and (number <= 999999):
#         result = 'Yes'
#     else:
#         result = 'No'
# print(result)

# test ----------
# print('A : 65', ord('A'))
# print('Z : 90', ord('Z'))
# print('1 : 49', ord('1'))
# print('2 : 50', ord('2'))
# print(type('1'))
# print(int('1'+'23'))
# print(type(int('1'+'2')))


# -----------------------------
# E Final Day

p_l = []
result = []
n_k = list(map(int, input().split()))
for _ in range(n_k[0]):
    p_l.append(sum(list(map(int, input().split()))))

p_sorted = sorted(p_l, reverse=True)
goal = p_sorted[n_k[1]-1]

for i in range(n_k[0]):
    if (goal - p_l[i]) <= 300:
        result.append('Yes')
    else:
        result.append('No')
for s in result:
    print(s)
