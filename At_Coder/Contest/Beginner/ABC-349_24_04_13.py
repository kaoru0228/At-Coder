# n, x = map(int, input().split())
# list = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]

# -----------------------------
# A Zero Sum Game
# n = int(input())
# a = list(map(int, input().split()))
# ans = -1 * sum(a)
# print(ans)


# -----------------------------
# -----------------------------
# B Commencement
# s = input()
# check = [0]*26
# for s_ in s:
#     check[ord(s_) - ord('a')] += 1
# check_2 = [0]*(len(s)+1)
# for i in range(len(check)):
#     check_2[check[i]] += 1
# flag = True
# for i in range(len(check_2)):
#     if i==0:
#         continue
#     if check_2[i] == 0 or check_2[i] == 2:
#         continue
#     else:
#         flag = False
#         break
# ans = 'Yes' if flag else 'No'
# print(ans)


# -----------------------------
# -----------------------------
# C Airport Code
# s = input()
# t = input()
# dist = ord('a') - ord('A')
# # print(ord('a')) # 97
# # print(ord('A')) # 65
# check = 0
# flag = False
# for s_ in s:
#     if (ord(s_) - dist) == ord(t[check]):
#         check += 1
#         if (check == 2 and t[2] == 'X') or check == 3:
#             flag = True
#             break
# ans = 'Yes' if flag else 'No'
# print(ans)

# -----------------------------
# -----------------------------
# D Divide Interval
# def good_sequence_decomposition(L, R):
#     ranges = []
#     while L < R:
#         # 現在の L に対して可能な最大の2^iを見つける
#         i = 0
#         while (1 << (i + 1)) <= L:
#             i += 1

#         # 最大の 2^i で次の区間を作成
#         power = 1 << i
#         start = L
#         end = min(R, (L // power + 1) * power)

#         # 範囲の終端が R を超えないように調整
#         while end > R or L // power != (end - 1) // power:
#             i -= 1
#             power = 1 << i
#             end = min(R, (L // power + 1) * power)

#         ranges.append((start, end))
#         L = end

#     return ranges

# def split_good(l, r):
#     ranges = []
#     p = l
#     if l%2 == 1:
#         ranges.append((l, l+1))
#         p = l+1
#     while p <= r:
#         ranges.append((p, p + 2 ** ((r-p).bit_length() - 1)))
#         p += 2 ** ((r-p).bit_length() - 1)
#         if p == r:
#             break    
#     return ranges

# L, R = map(int, input().split())
# decomposition = good_sequence_decomposition(L, R)

# start, end = decomposition[0]
# if not (start & (start - 1)) == 0:
#     range_1 = split_good(start, end)
# else:
#     range_1 = []

# start, end = decomposition[-1]
# if not (end & (end - 1)) == 0:
#     range_last = split_good(start, end)
# else:
#     range_last = []


# n = len(decomposition)
# if len(range_1)!=0:
#     n += (len(range_1)-1)
# if len(range_last)!=0:
#     n += (len(range_last)-1)
# print(n)

# for start, end in range_1:
#     print(f"{start} {end}")

# for start, end in decomposition[1:len(decomposition)-1]:
#     print(f"{start} {end}")

# for start, end in range_last:
#     print(f"{start} {end}")


# 解答例
L, R = map(int, input().split())
ans = []
while L != R:
    i = 0
    while L % pow(2, i+1) == 0 and L+pow(2, i+1) <= R:
        i += 1
    ans.append([L, L+pow(2, i)])
    L += pow(2, i)
print(len(ans))
for l, r in ans:
    print(l, r)



# -----------------------------
# -----------------------------
# E Weighted Tic-Tac-Toe
# import sys

# def minimax(grid, score_t, score_a, depth, is_takahashi):
#     # 勝利条件のチェック
#     def check_win(color):
#         # 縦、横、斜めのチェック
#         for i in range(3):
#             if all(grid[i][j] == color for j in range(3)):
#                 return True
#             if all(grid[j][i] == color for j in range(3)):
#                 return True
#         if all(grid[i][i] == color for i in range(3)):
#             return True
#         if all(grid[i][2-i] == color for i in range(3)):
#             return True
#         return False

#     # 勝利を確認
#     if check_win('T'):
#         return float('inf')  # 高橋君の勝利
#     if check_win('A'):
#         return float('-inf')  # 青木君の勝利

#     # マスが全て埋まった場合、スコアによって勝者を判定
#     if depth == 9:
#         return score_t - score_a

#     # ミニマックスアルゴリズムの再帰部分
#     if is_takahashi:
#         best_value = float('-inf')
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] == 0:
#                     grid[i][j] = 'T'
#                     value = minimax(grid, score_t + A[i][j], score_a, depth + 1, False)
#                     best_value = max(best_value, value)
#                     grid[i][j] = 0
#         return best_value
#     else:
#         best_value = float('inf')
#         for i in range(3):
#             for j in range(3):
#                 if grid[i][j] == 0:
#                     grid[i][j] = 'A'
#                     value = minimax(grid, score_t, score_a + A[i][j], depth + 1, True)
#                     best_value = min(best_value, value)
#                     grid[i][j] = 0
#         return best_value

# # 入力を受け取る
# A = [list(map(int, input().split())) for _ in range(3)]
# grid = [[0]*3 for _ in range(3)]

# # 高橋君が最初に手を始める
# result = minimax(grid, 0, 0, 0, True)

# # 結果の出力
# print("Takahashi" if result > 0 else "Aoki" if result < 0 else "Draw")

# 解答例　------------------------------
# import sys

# input = sys.stdin.readline

# # 3つの数値を受け取り，全同じ色かつ白出ないならTrueを返す
# def check(colors):
#     return len(set(colors)) == 1 and colors[0] != -1


# def rec(turn):
#     # どちらかがラインを作った状態 ----------
#     # check row
#     for i in range(3):
#         if check([state[3 * i + j] for j in range(3)]):
#             return state[3 * i]
#     # check col
#     for j in range(3):
#         if check([state[3 * i + j] for i in range(3)]):
#             return state[j]
#     # check diag
#     if check([state[3 * i + i] for i in range(3)]):
#         return state[0]
#     if check([state[3 * i + 2 - i] for i in range(3)]):
#         return state[2]

    
#     # all painted (スコアによる決着) ----------
#     if -1 not in state:
#         score = [0] * 2
#         for i in range(3):
#             for j in range(3):
#                 score[state[3 * i + j]] += A[i][j]
#         return 0 if score[0] > score[1] else 1

#     # 再帰により状態を進める
#     for k in range(9):
#         if state[k] == -1:
#             state[k] = turn
#             if rec(turn ^ 1) == turn:
#                 state[k] = -1
#                 return turn
#             state[k] = -1
#     return turn ^ 1


# A = [list(map(int, input().split())) for _ in range(3)]
# state = [-1] * 9
# print(["Takahashi", "Aoki"][rec(0)])




# -----------------------------
# -----------------------------
# F 



# -----------------------------
# -----------------------------
# G