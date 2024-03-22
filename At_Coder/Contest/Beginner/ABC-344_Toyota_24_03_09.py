# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# トヨタ自動車プログラミングコンテスト2024#3（AtCoder Beginner Contest 344）
# https://atcoder.jp/contests/abc344

# -----------------------------
# A Spoiler

# s = input()
# ans = ''
# flag = 0
# for s_ in s:
#     if s_ == '|' and flag == 0:
#         flag = 1
#         continue
#     elif s_ == '|' and flag == 1:
#         flag = 0
#         continue
#     if flag == 0:
#         ans += s_
# print(ans)

# -----------------------------
# B Delimiter

# a = -1
# ans = []
# while a != 0:
#     a = int(input())
#     ans.append(a)
# for i in range(1, len(ans)+1):
#     print(ans[-1*i])

# -----------------------------
# C A+B+C
# 解説
# n = int(input())
# a_l = list(map(int, input().split()))
# m = int(input())
# b_l = list(map(int, input().split()))
# l = int(input())
# c_l = list(map(int, input().split()))
# q = int(input())
# x_l = list(map(int, input().split()))

# sum_ = set()
# for a in a_l:
#     for b in b_l:
#         for c in c_l:
#             sum_.add(a+b+c)
# for x in x_l:
#     result = 'Yes' if x in sum_ else 'No'
#     print(result)


# # chat-GPT4
# from itertools import product
# n = int(input())
# a_l = list(map(int, input().split()))
# m = int(input())
# b_l = list(map(int, input().split()))
# l = int(input())
# c_l = list(map(int, input().split()))
# q = int(input())
# x_l = list(map(int, input().split()))


# def can_sum_to_X_efficient(A, B, C, X):
#     AB_sums = {a + b for a, b in product(A, B)}

#     results = []
#     for x in X:
#         found = any((x - c) in AB_sums for c in C)
#         results.append("Yes" if found else "No")

#     return results


# results = can_sum_to_X_efficient(a_l, b_l, c_l, x_l)
# for result in results:
#     print(result)


# -----------------------------
# D String Bags
# GPT4 WA
# def min_cost_to_match(T, bags):
#     dp = [[float('inf')] * (len(T) + 1) for _ in range(len(bags) + 1)]
#     dp[0][0] = 0

#     for i in range(1, len(bags) + 1):
#         for j in range(len(T) + 1):
#             dp[i][j] = min(dp[i][j], dp[i - 1][j])

#             for s in bags[i - 1]:
#                 for k in range(len(s) + 1):
#                     if j + k <= len(T) and T[:j+k].endswith(s[:k]):
#                         dp[i][j+k] = min(dp[i][j+k], dp[i - 1][j] + 1)

#     return dp[len(bags)][len(T)] if dp[len(bags)][len(T)] != float('inf') else -1

# print(min_cost_to_match(t, s_l))

# 自力 WA, TEL 修正により，WA1, 残りAC ----------------------------------
t = input()
n = int(input())
a_n = []
s_ll = []
for _ in range(n):
    s_l = list(input().split())
    a_n.append(s_l[0])
    s_ll.append(s_l[1:])

candidates = [None for _ in range(len(t))]

ans = []
for i, s_l in enumerate(s_ll):
    for s in s_l:
        if s == t[:len(s)]:
            candidates[len(s)-1] = [s, 1]
        for j, candidate in enumerate(candidates):
            if candidate == None:
                continue
            if s == t[j+1:(j+1+len(s))]:
                tmp = candidate[0]+s
                if candidates[j+len(s)] == None:
                    count = candidate[1]+1
                else:
                    count = min(candidates[j+len(s)][1], candidate[1]+1)
                candidates[j+len(s)] = [tmp, count]

result = candidates[len(t)-1][1] if candidates[len(t)-1] != None else -1
print(result)

# 解答   AC------------------------------
# def min_steps_to_form_string(t, bags):
#     # DPテーブルの初期化
#     dp = [[float('inf')] * (len(t) + 1) for _ in range(len(bags) + 1)]
#     dp[0][0] = 0

#     # 入力された袋についてループ
#     for i in range(len(bags)):

#         # 前の袋までの状態を引き継ぐ
#         for j in range(len(t) + 1):
#             dp[i+1][j] = dp[i][j]

#         # 現在の袋の各文字列についてループ
#         for s in bags[i]:
#             sl = len(s)
#             for j in range(len(t) - sl + 1):
#                 # 文字列がマッチするかチェック
#                 if t[j:j+sl] == s:
#                     dp[i+1][j+sl] = min(dp[i+1][j+sl], dp[i][j] + 1)

#     # 結果の出力
#     return dp[len(bags)][len(t)] if dp[len(bags)][len(t)] < float('inf') else -1


# t = input()
# n = int(input())
# a_n = []
# s_ll = []
# for _ in range(n):
#     s_l = list(input().split())
#     a_n.append(s_l[0])
#     s_ll.append(s_l[1:])

# result = min_steps_to_form_string(t, s_ll)
# print(result)

# -----------------------------
# E Insert or Erase
# TEL
# class QueryProcessor:
#     def __init__(self, initial_array):
#         self.array = initial_array
#         self.element_index = {val: idx for idx,
#                               val in enumerate(initial_array)}

#     def process_queries(self, queries):
#         for query in queries:
#             if query[0] == 2:
#                 self.remove_element(query[1])
#             elif query[0] == 1:
#                 self.insert_element(query[1], query[2])

#     def remove_element(self, x):
#         idx = self.element_index[x]
#         self.array.pop(idx)
#         for val, index in self.element_index.items():
#             if index > idx:
#                 self.element_index[val] -= 1
#         del self.element_index[x]

#     def insert_element(self, x, y):
#         idx = self.element_index[x] + 1
#         self.array.insert(idx, y)
#         for val, index in self.element_index.items():
#             if index >= idx:
#                 self.element_index[val] += 1
#         self.element_index[y] = idx

#     def get_array(self):
#         return self.array


# n = int(input())
# a_l = list(map(int, input().split()))
# q = int(input())
# queries = []
# for _ in range(q):
#     query = list(map(int, input().split()))
#     queries.append(query)


# processor = QueryProcessor(a_l)
# processor.process_queries(queries)
# final_array = processor.get_array()

# print(*final_array)

# AC --------------------------------
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.prev = None
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.nodes = {}

#     def insert_after(self, target, value):
#         new_node = Node(value)
#         self.nodes[value] = new_node

#         if target == None:
#             if self.head is None:
#                 self.head = self.tail = new_node
#             else:
#                 new_node.next = self.head
#                 self.head.prev = new_node
#                 self.head = new_node
#         else:
#             target_node = self.nodes[target]
#             new_node.prev = target_node
#             if target_node.next is None:
#                 target_node.next = new_node
#                 self.tail = new_node
#             else:
#                 new_node.next = target_node.next
#                 target_node.next.prev = new_node
#                 target_node.next = new_node

#     def remove(self, value):
#         target_node = self.nodes[value]

#         if target_node.prev is None:
#             self.head = target_node.next
#         else:
#             target_node.prev.next = target_node.next

#         if target_node.next is None:
#             self.tail = target_node.prev
#         else:
#             target_node.next.prev = target_node.prev

#         del self.nodes[value]

#     def to_list(self):
#         values = []
#         current = self.head
#         while current:
#             values.append(current.value)
#             current = current.next
#         return values


# n = int(input())
# a_l = list(map(int, input().split()))
# q = int(input())
# queries = []
# for _ in range(q):
#     query = list(map(int, input().split()))
#     queries.append(query)

# ll = LinkedList()
# for a in a_l:
#     ll.insert_after(ll.tail.value if ll.tail else None, a)

# for query in queries:
#     if query[0] == 1:
#         ll.insert_after(query[1], query[2])
#     elif query[0] == 2:
#         ll.remove(query[1])

# final_list = ll.to_list()
# print(*final_list)


# -----------------------------
# F

# n = int(input())
# n, q = map(int, input().split())
# s = list(map(int, input().split()))


# -----------------------------
# G
# n = int(input())
# x_l = []
# y_l = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     x_l.append(x)
#     y_l.append(y)
# q = int(input())
# g, ra, rb = map(int, input().split())

# g_l = [g]
# a_l = []
# b_l = []
# for i in range(1, 3*q+1):
#     g_l.append((48271*g_l[i-1]) % ((2**31)-1))
# for j in range(1, q+1):
#     a = -1*ra + (g_l[(3*j)-2] % ((2*ra)+1))
#     b = -1*rb + (g_l[(3*j)-1]*((2**31)-1) + g_l[3*j]) % ((2*rb)+1)
#     a_l.append(a)
#     b_l.append(b)
