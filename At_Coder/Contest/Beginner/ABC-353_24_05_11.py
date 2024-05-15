# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# AtCoder Beginner Contest 353
# https://atcoder.jp/contests/abc353

# -----------------------------
# A Buildings

# n = int(input())
# h_l = list(map(int, input().split()))
# first = h_l[0]
# ans = -1
# for i, h_ in enumerate(h_l):
#     if i == 0:
#         continue
#     if h_ > first:
#         ans = (i+1)
#         break
# print(ans)

# -----------------------------
# B AtCoder Amusement Park

# n, k = map(int, input().split())
# a_l = list(map(int, input().split()))
# count = 0
# seets_rest = k
# for i, a in enumerate(a_l):
#     if seets_rest >= a:
#         seets_rest -= a
#     else:
#         seets_rest = k-a
#         count += 1
#     if i == (n-1) and seets_rest != k:
#         count += 1
# print(count)

# -----------------------------
# C Sigma Problem

# n = int(input())
# a_l = list(map(int, input().split()))
# ans = (sum(a_l)*(n-1)) % (10**8)
# print(ans)

# 全探索 多分TLE -----------------------------
# n = int(input())
# a_l = list(map(int, input().split()))
# mod = 10**8
# ans = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         ans += (a_l[i]+a_l[j]) % mod
# print(ans)

# -----------------------------
# import bisect


# def count_pairs_exceeding_or_equal_sum(a, threshold):
#     n = len(a)
#     a.sort()  # 配列をソート
#     count = 0

#     for i in range(n):
#         # A[i] + A[j] >= threshold となる最小の j を見つける
#         # A[j] >= threshold - A[i] となる最小の j を探す
#         j = bisect.bisect_left(a, threshold - a[i], i + 1, n)
#         count += n - j  # 条件を満たす j の数を加算

#     return count


# # 入力例
# n = int(input())
# a = list(map(int, input().split()))
# threshold = 10**8

# # 関数を呼び出して結果を表示
# result = count_pairs_exceeding_or_equal_sum(a, threshold)

# tmp = (sum(a)*(n-1))//threshold
# tmp -= result

# ans = (sum(a)*(n-1)) % (10**8)
# ans += tmp*threshold

# print(ans)


# -----------------------------
# D

MOD = 998244353


def mod_pow(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


def solve(N, A):
    # 各数値の長さとそれに対応する 10^L を計算
    powers_of_10 = {}
    for num in A:
        length = len(str(num))
        if length not in powers_of_10:
            powers_of_10[length] = mod_pow(10, length, MOD)

    # 各数値の貢献を計算
    contribution_as_first = [0] * N
    contribution_as_second = [0] * N
    for i in range(N):
        l1 = len(str(A[i]))
        power1 = powers_of_10[l1]
        for j in range(N):
            if i != j:
                l2 = len(str(A[j]))
                power2 = powers_of_10[l2]
                # A[i] が最初の数の場合
                contribution_as_first[i] += A[j] + A[i] * power2
                contribution_as_first[i] %= MOD
                # A[j] が最初の数の場合
                contribution_as_second[i] += A[j] * power1 + A[i]
                contribution_as_second[i] %= MOD

    # 総和を計算
    total_contribution = sum(contribution_as_first) + \
        sum(contribution_as_second)
    total_contribution %= MOD
    return total_contribution


# 入力
N = int(input())
A = list(map(int, input().split()))

# 問題を解く
print(solve(N, A))


# -----------------------------
# E

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))


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
