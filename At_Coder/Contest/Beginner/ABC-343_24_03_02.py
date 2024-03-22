# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# AtCoder Beginner Contest 343
# https://atcoder.jp/contests/abc343

# -----------------------------
# A Wrong Answer

# a, b = map(int, input().split())
# ans = 0 if (a+b) != 0 else 1
# print(ans)

# -----------------------------
# B Adjacency Matrix

# n = int(input())
# ans = [[] for _ in range(n)]
# for i in range(n):
#     a = list(map(int, input().split()))
#     for j in range(n):
#         if a[j] == 1:
#             ans[i].append(j+1)
# for i in range(n):
#     print(*ans[i])

# -----------------------------
# C 343

# def is_palindrome(num):
#     return str(num) == str(num)[::-1]


# def max_palindrome_cube(N):
#     max_palindrome = -1
#     x = 1
#     while (x+1) ** 3 <= N:
#         x += 1
#     for x in range(x, 0, -1):
#         cube = x ** 3
#         if is_palindrome(cube):
#             max_palindrome = cube
#             break
#     return max_palindrome


# n = int(input())
# ans = max_palindrome_cube(n)
# print(ans)


# -----------------------------
# D Diversity of Scores

# n, t = map(int, input().split())
# score = [0]*n
# check = {0: n}
# ans = []
# for i in range(t):
#     a, b = map(int, input().split())
#     if (score[a-1]+b) in check:
#         check[score[a-1]+b] += 1
#     else:
#         check[score[a-1]+b] = 1

#     if check[score[a-1]] == 1:
#         del check[score[a-1]]
#     else:
#         check[score[a-1]] -= 1

#     score[a-1] += b
#     ans.append(len(check))
# for ans_ in ans:
#     print(ans_)

# -----------------------------
# E 7x7x7 解答参考 C++なら行ける，pythonはTEL
# def calc_two_vol(x1, y1, z1, x2, y2, z2):
#     volume = 1
#     volume *= max(0, ((min(x1, x2)+7) - max(x1, x2)))
#     volume *= max(0, ((min(y1, y2)+7) - max(y1, y2)))
#     volume *= max(0, ((min(z1, z2)+7) - max(z1, z2)))
#     return volume


# def calc_three_vol(x1, y1, z1, x2, y2, z2, x3, y3, z3):
#     volume = 1
#     volume *= max(0, ((min(x1, x2, x3)+7) - max(x1, x2, x3)))
#     volume *= max(0, ((min(y1, y2, y3)+7) - max(y1, y2, y3)))
#     volume *= max(0, ((min(z1, z2, z3)+7) - max(z1, z2, z3)))
#     return volume


# def find_match(v1, v2, v3):
#     a1 = b1 = c1 = 0
#     ans = [['No']]
#     for a2 in range(-7, 8, 1):
#         for b2 in range(-7, 8, 1):
#             for c2 in range(-7, 8, 1):
#                 for a3 in range(-7, 8, 1):
#                     for b3 in range(-7, 8, 1):
#                         for c3 in range(-7, 8, 1):
#                             v3_test = calc_three_vol(
#                                 a1, b1, c1, a2, b2, c2, a3, b3, c3)

#                             C1C2 = calc_two_vol(a1, b1, c1, a2, b2, c2)
#                             C2C3 = calc_two_vol(a2, b2, c2, a3, b3, c3)
#                             C3C1 = calc_two_vol(a3, b3, c3, a1, b1, c1)
#                             v2_test = C1C2+C2C3+C3C1-3*v3_test

#                             v1_test = (7**3)*3 - 2*v2_test - 3*v3_test

#                             if v1_test == v1 and v2_test == v2 and v3_test == v3:
#                                 ans = [
#                                     ['Yes'], [a1, b1, c1, a2, b2, c2, a3, b3, c3]]
#                                 return ans
#     return ans


# v1, v2, v3 = map(int, input().split())
# ans = find_match(v1, v2, v3)
# for ans_ in ans:
#     print(*ans_)

# -----------------------------
# F Second Largest Query  TEL
# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# ans = []
# for i in range(q):
#     q1, q2, q3 = map(int, input().split())
#     if q1 == 1:
#         a[q2-1] = q3
#     else:
#         sub_array_l = sorted(a[q2-1:q3])
#         sub_array = list(set(sub_array_l))
#         if len(sub_array) > 1:
#             second_largest = sub_array[-2]
#             flag = 0
#             count = 0
#             for j in range(1, q3-q2+2):
#                 if sub_array_l[-1*j] == second_largest:
#                     flag = 1
#                     count += 1
#                 elif sub_array_l[-1*j] != second_largest and flag == 1:
#                     break

#             # count = a[q2-1:q3].count(second_largest)
#             ans.append(count)
#         else:
#             ans.append(0)

# for ans_ in ans:
#     print(ans_)


# セグメントツリーの実装 ---------------------------
# 2値を比較する関数 value = [value, num]
# def compare(value1, value2):
#     if value1[0] == value2[0]:
#         value = [value1[0], value1[1]+value2[1]]
#     elif value1[0] > value2[0]:
#         value = [value1[0], value1[1]]
#     else:
#         value = [value2[0], value2[1]]
#     return value


# def merge(left, right):
#     # 最大値の更新
#     max_value = compare([left[0], left[1]], [right[0], right[1]])

#     # 2番目に大きい値の更新
#     if left[0] == right[0]:
#         second_max_value = compare(
#             [left[2], left[3]], [right[2], right[3]])
#     elif left[0] > right[0]:
#         second_max_value = compare(
#             [left[2], left[3]], [right[0], right[1]])
#     else:
#         second_max_value = compare(
#             [left[0], left[1]], [right[2], right[3]])
#     # 代入
#     value = [max_value[0], max_value[1],
#              second_max_value[0], second_max_value[1]]
#     return value


# def add_candidates(max, sec_max, candidates):
#     # 最大値の更新がある場合
#     if max[0] <= candidates[0]:
#         if max[0] == candidates[0]:
#             max[1] += candidates[1]
#         else:
#             max = [candidates[0], candidates[1]]

#         if sec_max[0] == candidates[2]:
#             sec_max[1] += candidates[3]
#         elif sec_max[0] < candidates[2]:
#             sec_max = [candidates[2], candidates[3]]
#     else:
#         if sec_max[0] == candidates[0]:
#             sec_max[1] += candidates[1]
#         elif sec_max[0] < candidates[0]:
#             sec_max = [candidates[0], candidates[1]]
#     return max, sec_max


# # セグメントツリーの実装（今回は，配列の最大値，その個数，２番目に大きい値，その個数をノードに格納する）
# # 根ノードのインデックス番号を1としている．よって，tree[0]は使っていない．
# class SegmentTree:
#     def __init__(self, arr):
#         self.n = len(arr)
#         self.tree = [[0, 0, 0, 0] for _ in range(2 * self.n)]  # セグメントツリーを配列で表現

#         # ツリーの葉に配列の要素をセット
#         for i in range(self.n, 2 * self.n):
#             self.tree[i] = [arr[i - self.n], 1, -float('inf'), 0]

#         # 内部ノードを構築
#         for i in range(self.n - 1, 0, -1):
#             left = self.tree[i << 1]
#             right = self.tree[i << 1 | 1]
#             self.tree[i] = merge(left, right)

#     # posは更新したい値のインデックス(1~n)，valはその位置にセットしたい値

#     def update(self, pos, val):
#         pos += self.n  # 葉の位置に移動
#         self.tree[pos][0] = val  # 葉を更新
#         while pos > 1:  # 根ノードにたどり着くまで更新
#             pos >>= 1  # 親ノードに移動（1ビット右にシフト = 2で割って余りを切り捨て）
#             self.tree[pos] = merge(self.tree[pos << 1],
#                                    self.tree[pos << 1 | 1])

#     def query(self, l, r):
#         # [l, r) の区間の2番目に大きい値の個数を求める
#         l += self.n  # 葉の位置に移動
#         r += self.n
#         max = [-float('inf'), 0]
#         sec_max = [-float('inf'), 0]
#         while l <= r:
#             if l & 1:  # lが右の子なら，その値を追加して一つ右へ移動
#                 max, sec_max = add_candidates(max, sec_max, self.tree[l])
#                 l += 1
#             if not r & 1:  # rが左の子なら，その値を追加して一つ左へ移動
#                 max, sec_max = add_candidates(max, sec_max, self.tree[r])
#                 r -= 1
#             # この時点でlは左の子，rは右の子となっているため，親ノードへ移動
#             l >>= 1
#             r >>= 1
#         return max, sec_max

#     def get(self):
#         return self.tree


# n, q = map(int, input().split())
# a = list(map(int, input().split()))
# st = SegmentTree(a)
# # print(st.tree)

# ans = []
# for i in range(q):
#     q1, q2, q3 = map(int, input().split())
#     if q1 == 1:
#         st.update(q2-1, q3)
#         # print(st.tree)
#     else:
#         max, sec_max = st.query(q2-1, q3-1)
#         ans.append(sec_max[1])

# for ans_ in ans:
#     print(ans_)

# -----------------------------
# G Compress Strings
# def merge_strings(s1, s2):
#     """2つの文字列をマージして、共通部分が最大になるような新たな文字列を返す"""
#     max_overlap = 0
#     merged_string = ""
#     for i in range(1, min(len(s1), len(s2)) + 1):
#         # s1がs2に含まれる場合
#         if s1 in s2:
#             max_overlap = len(s1)
#             merged_string = s2

#         # s2がs1に含まれる場合
#         elif s2 in s1:
#             max_overlap = len(s2)
#             merged_string = s1

#         else:
#             # s1の後ろとs2の前が重なる場合
#             if s1.endswith(s2[:i]):
#                 if i > max_overlap:
#                     max_overlap = i
#                     merged_string = s1 + s2[i:]
#             # s2の後ろとs1の前が重なる場合
#             if s2.endswith(s1[:i]):
#                 if i > max_overlap:
#                     max_overlap = i
#                     merged_string = s2 + s1[i:]
#     return merged_string if merged_string else s1 + s2


# def shortest_common_superstring(strings):
#     """与えられた全ての文字列を部分文字列として含む最短の文字列を求める"""
#     while len(strings) > 1:
#         max_overlap = -1
#         best_merge = (0, 0, "")  # (i, j, merged_string)
#         for i in range(len(strings)):
#             for j in range(i+1, len(strings)):
#                 if i != j:
#                     merged = merge_strings(strings[i], strings[j])
#                     overlap = len(strings[i]) + len(strings[j]) - len(merged)
#                     if overlap > max_overlap:
#                         max_overlap = overlap
#                         best_merge = (i, j, merged)
#         strings.pop(max(best_merge[0], best_merge[1]))
#         strings.pop(min(best_merge[0], best_merge[1]))
#         strings.append(best_merge[2])
#         print(strings)
#     return strings[0]


# n = int(input())
# s_l = []
# for i in range(n):
#     s = input()
#     s_l.append(s)
# strings = shortest_common_superstring(s_l)
# print(len(strings))
# print(strings)
