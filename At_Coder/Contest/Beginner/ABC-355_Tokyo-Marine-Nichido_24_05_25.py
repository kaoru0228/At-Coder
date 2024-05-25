# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# 東京海上日動プログラミングコンテスト2024（AtCoder Beginner Contest 355）
# https://atcoder.jp/contests/abc355

# -----------------------------
# A Who Ate the Cake?

# a, b = map(int, input().split())
# if a == b:
#     ans = -1
# else:
#     for i in range(1, 4):
#         if a == i:
#             continue
#         elif b == i:
#             continue
#         else:
#             ans = i
#             break
# print(ans)

# -----------------------------
# B Piano 2

# n, m = map(int, input().split())
# a_l = list(map(int, input().split()))
# b_l = list(map(int, input().split()))
# c_l = []
# for a in a_l:
#     c_l.append((a, 0))
# for b in b_l:
#     c_l.append((b, 1))
# c_sorted = sorted(c_l, key=lambda x: x[0])
# count = 0
# ans = 'No'
# for c, check in c_sorted:
#     if check == 0:
#         count += 1
#         if count >= 2:
#             ans = 'Yes'
#             break
#     else:
#         count = 0
# print(ans)

# -----------------------------
# C Bingo 2
# def bingo_2(N, T, A):
#     # マス目の初期化
#     board = [[N * (i - 1) + j for j in range(1, N + 1)]
#              for i in range(1, N + 1)]

#     # マス目の印を管理するためのリスト
#     marked = [[False] * N for _ in range(N)]

#     # 行と列のカウント
#     row_count = [0] * N
#     col_count = [0] * N
#     diag1_count = 0
#     diag2_count = 0

#     for turn in range(T):
#         num = A[turn]
#         found = False

#         # 印をつける
#         for i in range(N):
#             for j in range(N):
#                 if board[i][j] == num:
#                     marked[i][j] = True
#                     row_count[i] += 1
#                     col_count[j] += 1
#                     if i == j:
#                         diag1_count += 1
#                     if i + j == N - 1:
#                         diag2_count += 1
#                     found = True
#                     break
#             if found:
#                 break

#         # ビンゴの判定
#         if N in row_count or N in col_count or diag1_count == N or diag2_count == N:
#             return turn + 1

#     return -1


# n, t = map(int, input().split())
# a_l = list(map(int, input().split()))
# print(bingo_2(n, t, a_l))

# -----------------------------

# def bingo_2(N, T, A):

#     # マス目の印を管理するためのリスト
#     marked = [[False] * N for _ in range(N)]

#     # 行と列のカウント
#     row_count = [0] * N
#     col_count = [0] * N
#     diag1_count = 0
#     diag2_count = 0

#     for turn in range(T):
#         num = A[turn]

#         # 印をつける
#         i = (num-1)//N
#         j = (num-1) % N
#         marked[i][j] = True
#         row_count[i] += 1
#         col_count[j] += 1
#         if i == j:
#             diag1_count += 1
#         if i + j == N - 1:
#             diag2_count += 1

#         # ビンゴの判定
#         if N in row_count or N in col_count or diag1_count == N or diag2_count == N:
#             return turn + 1

#     return -1


# n, t = map(int, input().split())
# a_l = list(map(int, input().split()))
# print(bingo_2(n, t, a_l))

# -----------------------------
# D Intersecting Intervals

# def count_overlapping_intervals(intervals):
#     events = []
#     for i, (l, r) in enumerate(intervals):
#         events.append((l, 1))  # 区間の開始
#         events.append((r, -1))  # 区間の終了

#     # events.sort()
#     events.sort(key=lambda x: (x[0], x[1] == -1))  # 値が同じ場合、開始イベントを先に
#     # print(events)

#     overlapping_intervals = 0
#     active_intervals = 0

#     for pos, event in events:
#         if event == 1:  # 区間の開始
#             overlapping_intervals += active_intervals
#             active_intervals += 1
#         else:  # 区間の終了
#             active_intervals -= 1

#     return overlapping_intervals


# # 入力の読み込み
# n = int(input())
# intervals = []
# for i in range(n):
#     l, r = map(int, input().split())
#     intervals.append((l, r))

# # 関数を呼び出して結果を出力
# result = count_overlapping_intervals(intervals)
# print(result)


# -----------------------------
# E Guess the Sum

def interactive_query(l, r):
    print(f"? {l} {r}")
    sys.stdout.flush()
    response = int(input())
    return response


def get_segment(l, r):
    segment_sum = interactive_query(l, r)
    return segment_sum


def solve(N, L, R):
    segment_length = 1 << N
    result = [0] * segment_length

    for i in range(N+1):
        step = 1 << i
        for j in range(0, segment_length, step):
            if j >= L and j + step - 1 <= R:
                segment_sum = get_segment(j, j + step - 1)
                for k in range(j, j + step):
                    result[k] = segment_sum // step

    total_sum = sum(result[L:R+1])
    print(f"! {total_sum}")
    sys.stdout.flush()


if __name__ == "__main__":
    import sys
    n, l, r = map(int, input().split())
    solve(n, l, r)


# -----------------------------
# F

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))


# -----------------------------
# G

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))
