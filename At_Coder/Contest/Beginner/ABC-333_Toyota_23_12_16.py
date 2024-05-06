# n = int(input())
# s = list(map(int, input().split()))
# n, s = map(int, input().split())


# トヨタ自動車プログラミングコンテスト2023#8（AtCoder Beginner Contest 333）
# https://atcoder.jp/contests/abc333


# -----------------------------
# A Three Threes

# n = int(input())
# answer = ''
# for _ in range(n):
#     answer += str(n)
# print(answer)

# -----------------------------
# B Pentagon

# s_l = str(input())
# t_l = str(input())
# penta = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
# a = abs(penta[s_l[0]] - penta[s_l[1]])
# b = abs(penta[t_l[0]] - penta[t_l[1]])
# if a == b or (a+b) == 5:
#     result = 'Yes'
# else:
#     result = 'No'
# print(result)


# -----------------------------
# C Repunit Trio
# n = int(input())
# search = [1, [1, 1, 1]]


# for文で一覧を求めた後，sortedする方法
# n = int(input())
# repunits = [int('1' * i) for i in range(1, 13)]
# sums = set()
# for i in repunits:
#     for j in repunits:
#         for k in repunits:
#             sums.add(i + j + k)
# sorted = sorted(list(sums))
# ans = sorted[n - 1] if n - 1 < len(sorted) else None
# print(ans)

# -----------------------------
# D Erase Leaves


# -----------------------------
# E Takahashi Quest
'''
桁和は1ずつ増える
ただし繰上りが起きたとき8減少する
繰上りは 10^位 回に1回起こる
'''

n = int(input())
t_l = []
x_l = []
monster = [0]*n
potion_sum = [0]*n
potion_now = [0]*n
monster_turn = [[] for _ in range(n)]
portion_turn = [[] for _ in range(n)]
ans = 0
for i in range(n):
    t, x = map(int, input().split())
    x -= 1
    t_l.append(t)
    x_l.append(x)
    if ans == -1:
        continue
    else:
        if t == 1:
            potion_now[x] += 1
            potion_sum[x] += 1
            portion_turn[x].append(i)
        else:
            monster[x] += 1
            monster_turn[x].append(i)
            if potion_now[x] < 1:
                ans = -1
            else:
                potion_now[x] -= 1

if ans == -1:
    print(ans)
else:
    choice = []
    have = 0
    k_max = 0
    potion_extra = [a - b for a, b in zip(potion_sum, monster)]  # 余剰
    for i in range(n):
        if t_l[i] == 1:
            if potion_extra[x_l[i]] > 0:  # 拾わない
                potion_extra[x_l[i]] -= 1
                choice.append(0)
            else:  # 拾う
                have += 1
                choice.append(1)
        else:
            if have > k_max:
                k_max = have
            have -= 1

    print(k_max)
    print(*choice)
    # print('clear')


# -----------------------------
# F


# -----------------------------
# G
