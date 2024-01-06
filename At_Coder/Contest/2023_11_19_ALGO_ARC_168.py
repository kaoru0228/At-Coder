# n, x = map(int, input().split())
# list = list(map(int, input().split()))


# ALGO ARTIS プログラミングコンテスト2023 秋 （AtCoder Regular Contest 168
# https://atcoder.jp/contests/arc168


# -----------------------------
# A <Inversion>

# GPT4 マージソート
# def merge_sort_count_inversion(arr):
#     if len(arr) <= 1:
#         return arr, 0
#     else:
#         mid = len(arr) // 2
#         left, left_inv = merge_sort_count_inversion(arr[:mid])
#         right, right_inv = merge_sort_count_inversion(arr[mid:])
#         merged, merge_inv = merge_count_split_inversion(left, right)
#         return merged, left_inv + right_inv + merge_inv

# def merge_count_split_inversion(left, right):
#     merged = []
#     count = 0
#     i, j = 0, 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             merged.append(left[i])
#             i += 1
#         else:
#             merged.append(right[j])
#             count += len(left) - i  # ここで転倒数をカウント
#             j += 1

#     merged += left[i:]
#     merged += right[j:]
#     return merged, count

# n = int(input())
# s = input()
# x = [1]
# for i in range(len(s)):
#     if s[i] == '<':
#         x.append(x[i]+1)
#     else:
#         x.append(x[i]-1)
# # print(x)

# sorted_arr, count = merge_sort_count_inversion(x)
# print(count)
# # print("Sorted array:", sorted_arr)
# # print("Number of inversions:", count)  # 出力: Number of inversions: 5



# -----------------------------
# -----------------------------
# B Arbitrary Nim

n = int(input())
a_l = list(map(int, input().split()))



# -----------------------------
# -----------------------------
# C 


# -----------------------------
# -----------------------------
# D 


# -----------------------------
# -----------------------------
# E 


# -----------------------------
# -----------------------------
# F 



# -----------------------------
# -----------------------------
# G