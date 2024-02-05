# n, q = map(int, input().split())
# n = int(input())
# s = list(map(int, input().split()))

# AtCoder Beginner Contest 336
# https://atcoder.jp/contests/abc336

# -----------------------------
# A  Long Loong

# n = int(input())
# answer = 'L' + 'o'*n + 'ng'
# print(answer)

# -----------------------------
# B CTZ

# n = int(input())
# r = 1
# count = 0
# while (n != 0):
#     r = n % 2
#     n = n//2
#     if r == 0:
#         count += 1
#     else:
#         break
# print(count)


# -----------------------------
# C Even Digits

# 全探索  TEL ----------
# n = int(input())
# count = 0
# current = 0

# while True:
#     if all(digit in '02468' for digit in str(current)):
#         count += 1
#         if count == n:
#             break
#     current += 1

# print(current)


# 5進数の利用 ----------
# n = int(input())
# n -= 1


# def convert_to_base_5(n):
#     if n == 0:
#         return "0"

#     base_5 = ""
#     while n > 0:
#         base_5 = str(n % 5) + base_5
#         n //= 5

#     return base_5


# print(int(convert_to_base_5(n))*2)


# -----------------------------
# D Pyramid

# n = int(input())
# a = list(map(int, input().split()))
# def pyramid_size(center):
#     k = 1
#     left, right = center - 1, center + 1
#     max_value = a[center]

#     while left >= 0 and right < n:
#         max_value -= 1
#         if max_value <= 0:
#             break

#         if not (a[left] >= max_value and a[right] >= max_value):
#             break
#         k += 1
#         left -= 1
#         right += 1

#     return k
# result = []
# max_k = 0
# for i in range(n):
#     result.append(pyramid_size(i))
# # print(result)
# print(max(result))


# ピラミッドを生成し，配列aと引き算することで作成可能かを確認 TEL-----------
# n = int(input())
# a = list(map(int, input().split()))
# a_max = 0

# for i in range(1, n+1):
#     check = [0]*n
#     if i <= ((n//2)+(n % 2)):
#         k = i
#         for j in range((i*2)-1):
#             if j < i:
#                 if j == 0:
#                     check[j] = 1
#                 else:
#                     check[j] = check[j-1]+1
#             else:
#                 check[j] = check[j-1]-1
#     else:
#         k = n-i+1
#         for j in range(1, (k*2)):
#             if j <= k:
#                 if j == 1:
#                     check[-1*j] = 1
#                 else:
#                     check[-1*j] = check[(-1*j)+1]+1
#             else:
#                 check[-1*j] = check[(-1*j)+1]-1

#     b = [x - y for x, y in zip(a, check)]
#     if not any(x < 0 for x in b):
#         a_max = max(a_max, k)

# print(a_max)


# # 再チャレンジ OK --------------------------
# n = int(input())
# a = list(map(int, input().split()))
# right = [0]*n
# left = [0]*n
# for i in range(n):
#     if i == 0:
#         right[0] = 1
#         left[-1] = 1
#     else:
#         right[i] = (right[i-1]+1) if a[i] > right[i-1] else a[i]
#         left[(-1)*(i+1)] = (left[(-1)*(i+1)+1]+1) if a[(-1)
#                                                        * (i+1)] > left[(-1)*(i+1)+1] else a[(-1)*(i+1)]
# result = [min(r, l) for r, l in zip(right, left)]
# # print(right)
# # print(left)
# # print(result)
# print(max(result))


# -----------------------------
# E Digit Sum Divisible

'''
桁和は1ずつ増える
ただし繰上りが起きたとき8減少する
繰上りは 10^位 回に1回起こる
'''
n = int(input())
count = 0
digit_sum = 0
for k in range(1, n+1):
    check = k
    move_up = 0
    while True:
        if check % 10 == 0:
            move_up += 1
            check /= 10
        else:
            break
    digit_sum += (1-9*move_up)
    if k % digit_sum == 0:
        count += 1
print(count)


# -----------------------------
# F

# n, q = map(int, input().split())
# n = int(input())
# s = list(map(int, input().split()))


# -----------------------------
# G

# n, q = map(int, input().split())
# n = int(input())
# s = list(map(int, input().split()))
