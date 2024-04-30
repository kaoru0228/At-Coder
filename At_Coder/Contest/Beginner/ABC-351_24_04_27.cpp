// A ------------------------------
// #include <iostream>
// #include <vector>
// #include <queue>
// #include <set>
// #include <utility>
// #include <string>

// using namespace std;

// int main()
// {
//     int x = 0, y = 0, tmp;
//     for (int i = 0; i < 9; i++)
//     {
//         cin >> tmp;
//         x += tmp;
//     }
//     for (int i = 0; i < 8; i++)
//     {
//         cin >> tmp;
//         y += tmp;
//     }
//     cout << (x - y + 1) << endl;
//     return 0;
// }

// B ------------------------------
// #include <iostream>
// #include <vector>
// #include <queue>
// #include <set>
// #include <utility>
// #include <string>

// using namespace std;

// int main()
// {
//     int n;
//     cin >> n;
//     string a, b;
//     vector<string> A(n), B(n);
//     for (auto &s : A)
//         cin >> s;
//     for (auto &s : B)
//         cin >> s;
//     for (int i = 0; i < n; i++)
//     {
//         for (int j = 0; j < n; j++)
//         {
//             if (A[i][j] != B[i][j])
//             {
//                 cout << i + 1 << " " << j + 1 << endl;
//                 return 0;
//             }
//         }
//     }
// }

// C ------------------------------
// #include <iostream>
// #include <vector>
// #include <queue>
// #include <set>
// #include <utility>
// #include <string>

// using namespace std;

// int main()
// {
//     int n, a_, cnt = 0, new_value;
//     cin >> n;
//     vector<int> X;
//     for (int i = 0; i < n; i++)
//     {
//         // for (int k : X)
//         // {
//         //     cout << k << " ";
//         // }
//         // cout << endl;
//         cin >> a_;
//         X.push_back(a_);
//         cnt++;
//         while (cnt > 1 && X[cnt - 1] == X[cnt - 2])
//         {
//             new_value = X[cnt - 1] + 1;
//             X.pop_back();
//             X.pop_back();
//             X.push_back(new_value);
//             cnt--;
//         }
//     }
//     cout << X.size() << endl;
// }

// // D ------------------------------
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <utility>
#include <string>

using namespace std;

bool is_fold(vector<string> grid, int i, int j, int H, int W)
{
    const int dx[] = {-1, 1, 0, 0};
    const int dy[] = {0, 0, -1, 1};
    for (int k = 0; k < 4; k++)
    {
        int ni = i + dx[k], nj = j + dy[k];
        if (ni >= 0 && ni < H && nj >= 0 && nj < W && grid[ni][nj] == '#')
        {
            return true;
        }
    }
    return false;
}

int dfs(vector<string> grid, int si, int sj, int H, int W, vector<vector<int>> &value)
{
    int count = 0;

    // stack<pair<int, int>> st;
    queue<pair<int, int>> que;
    vector<pair<int, int>> memo;
    vector<vector<bool>> visited(H, vector<bool>(W, false));
    // st.push({si, sj});
    que.push({si, sj});
    visited[si][sj] = true;
    // while (!st.empty())
    while (!que.empty())
    {
        // auto [ci, cj] = st.top();
        auto [ci, cj] = que.front();
        // st.pop();
        que.pop();
        count++;
        if (is_fold(grid, ci, cj, H, W))
            continue;
        const int dx[] = {-1, 1, 0, 0};
        const int dy[] = {0, 0, -1, 1};
        for (int k = 0; k < 4; k++)
        {
            int ni = ci + dx[k], nj = cj + dy[k];
            if (ni >= 0 && ni < H && nj >= 0 && nj < W && !visited[ni][nj] && grid[ni][nj] != '#')
            {
                if (value[ni][nj] > 1)
                    return value[ni][nj];
                // st.push({ni, nj});
                que.push({ni, nj});
                visited[ni][nj] = true;
            }
        }
    }
    return count;
}

int main()
{
    int H, W, degree, maxdegree = 0;
    cin >> H >> W;
    vector<string> S(H);
    vector<vector<int>> value(H, vector<int>(W, -1));

    for (int i = 0; i < H; i++)
        cin >> S[i];
    for (int i = 0; i < H; i++)
    {
        for (int j = 0; j < W; j++)
        {
            if (S[i][j] == '#')
            {
                // value[i][j] = 0;
                continue;
            }
            if (is_fold(S, i, j, H, W))
            {
                degree = 1;
                value[i][j] = 1;
                maxdegree = max(maxdegree, degree);
            }
            else
            {
                degree = dfs(S, i, j, H, W, value);
                value[i][j] = degree;
                maxdegree = max(maxdegree, degree);
            }
        }
    }
    cout << maxdegree << endl;
}