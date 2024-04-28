#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <utility>
#include <string>

using namespace std;

bool is_free(const vector<string> &grid, int i, int j, int H, int W)
{
    if (grid[i][j] == '#')
        return false;
    const int dx[] = {-1, 1, 0, 0};
    const int dy[] = {0, 0, -1, 1};
    for (int d = 0; d < 4; ++d)
    {
        int ni = i + dx[d], nj = j + dy[d];
        if (ni >= 0 && ni < H && nj >= 0 && nj < W && grid[ni][nj] == '#')
        {
            return false;
        }
    }
    return true;
}

int bfs(const vector<string> &grid, int start_i, int start_j, int H, int W, vector<vector<int>> &confirmed)
{
    queue<pair<int, int>> queue;
    set<pair<int, int>> visited;
    queue.emplace(start_i, start_j);
    visited.insert({start_i, start_j});
    int count = 0;

    while (!queue.empty())
    {
        auto [ci, cj] = queue.front();
        queue.pop();
        count++;
        if (!is_free(grid, ci, cj, H, W))
            continue;
        const int dx[] = {-1, 1, 0, 0};
        const int dy[] = {0, 0, -1, 1};
        for (int d = 0; d < 4; ++d)
        {
            int ni = ci + dx[d], nj = cj + dy[d];
            if (ni >= 0 && ni < H && nj >= 0 && nj < W && visited.find({ni, nj}) == visited.end() && grid[ni][nj] == '.')
            {
                if (confirmed[ni][nj] > 0 && is_free(grid, ni, nj, H, W))
                {
                    return confirmed[ni][nj];
                }
                visited.insert({ni, nj});
                queue.emplace(ni, nj);
            }
        }
    }
    return count;
}

int max_freedom_degree(int H, int W, const vector<string> &grid, vector<vector<int>> &confirmed)
{
    int max_degree = 0;
    for (int i = 0; i < H; ++i)
    {
        for (int j = 0; j < W; ++j)
        {
            if (grid[i][j] == '.')
            {
                if (is_free(grid, i, j, H, W))
                {
                    int degree = bfs(grid, i, j, H, W, confirmed);
                    max_degree = max(max_degree, degree);
                    confirmed[i][j] = degree;
                }
                else
                {
                    int degree = 1;
                    max_degree = max(max_degree, degree);
                    confirmed[i][j] = degree;
                }
            }
        }
    }
    return max_degree;
}

int main()
{
    int H, W;
    cin >> H >> W;
    vector<string> grid(H);
    for (int i = 0; i < H; ++i)
    {
        cin >> grid[i];
    }
    vector<vector<int>> confirmed(H, vector<int>(W, -1));
    cout << max_freedom_degree(H, W, grid, confirmed) << endl;
    return 0;
}