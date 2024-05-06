#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>

using namespace std;

struct Edge
{
    int u, v, weight;
    Edge(int _u, int _v, int _w) : u(_u), v(_v), weight(_w) {}
    bool operator<(const Edge &other) const
    {
        return weight < other.weight;
    }
};

class UnionFind
{
public:
    vector<int> parent, rank;
    UnionFind(int size) : parent(size), rank(size, 0)
    {
        for (int i = 0; i < size; ++i)
            parent[i] = i;
    }
    int find(int x)
    {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int x, int y)
    {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY)
        {
            if (rank[rootX] < rank[rootY])
                swap(rootX, rootY);
            parent[rootY] = rootX;
            if (rank[rootX] == rank[rootY])
                rank[rootX]++;
        }
    }
};

int main()
{
    int N, M;
    cin >> N >> M;
    vector<Edge> edges;
    for (int i = 0; i < M; ++i)
    {
        int K, C;
        cin >> K >> C;
        vector<int> vertices(K);
        for (int j = 0; j < K; ++j)
        {
            cin >> vertices[j];
            vertices[j]--; // 0-based index
        }
        for (int j = 0; j < K; ++j)
        {
            for (int k = j + 1; k < K; ++k)
            {
                edges.emplace_back(vertices[j], vertices[k], C);
            }
        }
    }
    sort(edges.begin(), edges.end());
    UnionFind uf(N);
    int mst_weight = 0;
    for (const Edge &e : edges)
    {
        if (uf.find(e.u) != uf.find(e.v))
        {
            uf.unite(e.u, e.v);
            mst_weight += e.weight;
        }
    }
    // Check if all nodes are connected
    int root = uf.find(0);
    for (int i = 1; i < N; ++i)
    {
        if (uf.find(i) != root)
        {
            cout << -1 << endl;
            return 0;
        }
    }
    cout << mst_weight << endl;
    return 0;
}
