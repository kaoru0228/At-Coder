# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# s = [list(input()) for _ in range(n)]
# s = input()
# x = int(input())

# AtCoder Beginner Contest 351
# https://atcoder.jp/contests/abc351

# -----------------------------
# A The bottom of the ninth

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# print(sum(a)-sum(b)+1)

# -----------------------------
# B Spot the Difference /

# n = int(input())
# a_l = []
# b_l = []
# for i in range(n):
#     a_l.append(input())
# for i in range(n):
#     b_l.append(input())
# ans = []
# for i in range(n):
#     if ans:
#         break
#     for j in range(n):
#         if a_l[i][j] != b_l[i][j]:
#             ans.append(i+1)
#             ans.append(j+1)
#             break
# print(*ans)

# -----------------------------
# C Merge the balls

# n = int(input())
# a_l = list(map(int, input().split()))
# list = []
# for i in range(n):
#     list.append(a_l[i])
#     while len(list) > 1 and list[-1] == list[-2]:
#         new_size = list.pop() + 1
#         tmp = list.pop()
#         list.append(new_size)
# print(len(list))

# -----------------------------
# D Grid and Magnet
from collections import deque


def is_free(grid, i, j, H, W):
    if grid[i][j] == '#':
        return False
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '#':
            return False
    return True


def bfs(grid, start_i, start_j, H, W, confirmed):
    queue = deque([(start_i, start_j)])
    visited = set([(start_i, start_j)])
    count = 0
    while queue:
        count += 1
        ci, cj = queue.popleft()
        if not is_free(grid, ci, cj, H, W):
            continue
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < H and 0 <= nj < W and (ni, nj) not in visited and grid[ni][nj] == '.':
                if confirmed[ni][nj] > 1:
                    return confirmed[ni][nj]
                visited.add((ni, nj))
                queue.append((ni, nj))
    return count


def max_freedom_degree(H, W, grid, confirmed):
    max_degree = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '.':
                if is_free(grid, i, j, H, W):
                    degree = bfs(grid, i, j, H, W, confirmed)
                    max_degree = max(max_degree, degree)
                    confirmed[i][j] = degree
                else:
                    degree = 1
                    max_degree = max(max_degree, degree)
                    confirmed[i][j] = degree
    return max_degree


h, w = map(int, input().split())
s_l = []
for i in range(h):
    s_l.append(input())
confirmed = [[-1]*w for _ in range(h)]
print(max_freedom_degree(h, w, s_l, confirmed))


# -------------------------------------
# C++にしたら行けた．pythonではTLE．C++にした後一部修正が必要だった．まるまる同じコードにはしてくれなかった．大幅なタイムロス．．．
# 以下，C++コード
# #include <iostream>
# #include <vector>
# #include <queue>
# #include <set>
# #include <utility>
# #include <string>

# using namespace std;

# bool is_free(const vector<string>& grid, int i, int j, int H, int W) {
#     if (grid[i][j] == '#') return false;
#     const int dx[] = {-1, 1, 0, 0};
#     const int dy[] = {0, 0, -1, 1};
#     for (int d = 0; d < 4; ++d) {
#         int ni = i + dx[d], nj = j + dy[d];
#         if (ni >= 0 && ni < H && nj >= 0 && nj < W && grid[ni][nj] == '#') {
#             return false;
#         }
#     }
#     return true;
# }

# int bfs(const vector<string>& grid, int start_i, int start_j, int H, int W, vector<vector<int>>& confirmed) {
#     queue<pair<int, int>> queue;
#     set<pair<int, int>> visited;
#     queue.emplace(start_i, start_j);
#     visited.insert({start_i, start_j});
#     int count = 0;

#     while (!queue.empty()) {
#         auto [ci, cj] = queue.front(); queue.pop();
#         count++;
#         if (!is_free(grid, ci, cj, H, W)) continue;
#         const int dx[] = {-1, 1, 0, 0};
#         const int dy[] = {0, 0, -1, 1};
#         for (int d = 0; d < 4; ++d) {
#             int ni = ci + dx[d], nj = cj + dy[d];
#             if (ni >= 0 && ni < H && nj >= 0 && nj < W && visited.find({ni, nj}) == visited.end() && grid[ni][nj] == '.') {
#                 if (confirmed[ni][nj] > 0 && is_free(grid, ni, nj, H, W)) {
#                     return confirmed[ni][nj];
#                 }
#                 visited.insert({ni, nj});
#                 queue.emplace(ni, nj);
#             }
#         }
#     }
#     return count;
# }

# int max_freedom_degree(int H, int W, const vector<string>& grid, vector<vector<int>>& confirmed) {
#     int max_degree = 0;
#     for (int i = 0; i < H; ++i) {
#         for (int j = 0; j < W; ++j) {
#             if (grid[i][j] == '.') {
#                 if (is_free(grid, i, j, H, W)){
#                     int degree = bfs(grid, i, j, H, W, confirmed);
#                     max_degree = max(max_degree, degree);
#                     confirmed[i][j] = degree;
#                 }
#                 else {
#                     int degree = 1;
#                     max_degree = max(max_degree, degree);
#                     confirmed[i][j] = degree;
#                 }
#             }
#         }
#     }
#     return max_degree;
# }

# int main() {
#     int H, W;
#     cin >> H >> W;
#     vector<string> grid(H);
#     for (int i = 0; i < H; ++i) {
#         cin >> grid[i];
#     }
#     vector<vector<int>> confirmed(H, vector<int>(W, -1));
#     cout << max_freedom_degree(H, W, grid, confirmed) << endl;
#     return 0;
# }


# -----------------------------
# E Jump Distance Sum

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
