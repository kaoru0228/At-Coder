// g++ -o test ABC-357_suntory_24_06_08.cpp
// test

// AC 20 TLE 11
#include <iostream>
#include <vector>
#include <unordered_set>
#include <stack>

using namespace std;

// 各頂点から到達可能な頂点を探すためのDFS関数
unordered_set<int> dfs(int start, vector<vector<int>> &graph, vector<unordered_set<int>> &reachable_from)
{
    if (!reachable_from[start].empty())
    {
        return reachable_from[start];
    }

    vector<bool> visited(graph.size(), false);
    stack<int> stk;
    stk.push(start);
    unordered_set<int> reachable_nodes;

    while (!stk.empty())
    {
        int node = stk.top();
        stk.pop();
        if (!visited[node])
        {
            visited[node] = true;
            reachable_nodes.insert(node);
            for (int neighbor : graph[node])
            {
                if (!visited[neighbor])
                {
                    if (!reachable_from[neighbor].empty())
                    {
                        // すでに探索済みの頂点に到達した場合、その結果を再利用する
                        reachable_nodes.insert(reachable_from[neighbor].begin(), reachable_from[neighbor].end());
                    }
                    else
                    {
                        stk.push(neighbor);
                    }
                }
            }
        }
    }

    // 探索結果をメモ
    reachable_from[start] = reachable_nodes;
    return reachable_nodes;
}

// 全ての頂点についてDFSを実行し、到達可能なペアの数を数える関数
int find_reachable_pairs(int N, vector<int> &a)
{
    // グラフを作成
    vector<vector<int>> graph(N + 1);
    for (int i = 1; i <= N; ++i)
    {
        graph[i].push_back(a[i - 1]);
    }

    // 各頂点から到達可能な頂点のメモ
    vector<unordered_set<int>> reachable_from(N + 1);

    int total_reachable_pairs = 0;
    for (int i = 1; i <= N; ++i)
    {
        unordered_set<int> reachable_nodes = dfs(i, graph, reachable_from);
        total_reachable_pairs += reachable_nodes.size();
    }

    return total_reachable_pairs;
}

int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }

    // 結果を出力
    cout << find_reachable_pairs(n, a) << endl;

    return 0;
}

// -----------------------------
