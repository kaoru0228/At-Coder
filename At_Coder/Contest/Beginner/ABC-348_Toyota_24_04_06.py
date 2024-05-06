# n, x = map(int, input().split())
# list = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]

# -----------------------------
# A Penalty Kick

# n = int(input())
# ans = ''
# for i in range(1, n+1):
#     if i%3==0:
#         ans = ans + 'x'
#     else:
#         ans = ans + 'o'
# print(ans)

# -----------------------------
# -----------------------------
# B Farthest Point / 

# n = int(input())
# x_l = []
# y_l = []
# for i in range(n):
#     x, y = map(int, input().split())
#     x_l.append(x)
#     y_l.append(y)
# ans = []
# for i in range(n):
#     max_len = 0
#     for j in range(n):
#         if i==j:
#             continue
#         if max_len < ((x_l[i]-x_l[j])**2 + (y_l[i]-y_l[j])**2):
#             max_len = (x_l[i]-x_l[j])**2 + (y_l[i]-y_l[j])**2
#             idx = j+1
#     ans.append(idx)
# for ans_ in ans:
#     print(ans_)


# -----------------------------
# -----------------------------
# C Colorful Beans

# n = int(input())
# check = {}
# for i in range(n):
#     a, c = map(int, input().split())
#     if c in check:
#         check[c] = min(check[c], a)
#     else:
#         check[c] = a
# max_min_price = max(check.values())
# print(max_min_price)



# -----------------------------
# -----------------------------
# D Medicines on Grid
# h, w = map(int, input().split())
# grid = []
# for i in range(h):
#     s_ = input()
#     grid.append(s_)
# n = int(input())
# for i in range(n):
#     r, c, e = map(int, input().split())

# GPT4あり
from collections import deque

H, W = map(int, input().split())  # グリッドのサイズ
grid = [input() for _ in range(H)]  # グリッドの状態
N = int(input())  # 薬の数
medicines = {}  # 薬の位置とエネルギーを記録する辞書

for _ in range(N):
    r, c, e = map(int, input().split())
    medicines[(r-1, c-1)] = e  # 0-indexed に調整

# スタートとゴールの位置を見つける
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start = (i, j)
        if grid[i][j] == 'T':
            goal = (i, j)

# 上下左右の移動方向
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs(start, goal):
    if (start[0], start[1]) in medicines:
        queue = deque([(start[0], start[1], medicines[(start[0], start[1])])])  # (i, j, energy)
    else:
        return False
    visited = set([(start[0], start[1], medicines[(start[0], start[1])])])
    
    while queue:
        x, y, energy = queue.popleft()
        
        if (x, y) == goal:
            return True
                
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # エネルギーが1以上で移動可能な場合
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#' and energy > 0 and (nx, ny, energy-1) not in visited:
                if (nx, ny) == goal:
                    return True
                if (nx, ny) in medicines and (x, y, medicines[(nx, ny)]) not in visited:
                    visited.add((nx, ny, max(medicines[(nx, ny)], energy-1)))
                    queue.append((nx, ny, max(medicines[(nx, ny)], energy-1)))
                    
                else:
                    visited.add((nx, ny, energy-1))
                    queue.append((nx, ny, energy-1))
                
    return False

if bfs(start, goal):
    print("Yes")
else:
    print("No")





# -----------------------------
# -----------------------------
# E 
# n = input()
# n, x = map(int, input().split())


# -----------------------------
# -----------------------------
# F 
# n = input()
# n, x = map(int, input().split())


