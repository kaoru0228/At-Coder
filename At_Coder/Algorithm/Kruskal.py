# 同じサイクルに属するかは，各サイクルにグループ名を付与することで実現できる．
# UnionFindクラスで管理．
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])  # Path compression
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX


def kruskal(edges, N):
    # Nは頂点の数、edgesは(重み, 頂点1, 頂点2)の形式の辺のリスト
    edges.sort()  # 辺を重みに基づいてソートする
    uf = UnionFind(N)  # Union-Findのインスタンスを作成

    mst_weight = 0  # 最小全域木の重みの合計
    mst_edges = []  # 最小全域木を構成する辺のリスト

    for weight, u, v in edges:
        # サイクルを形成しない場合（異なる連結成分に属する場合）、辺を追加
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((weight, u, v))
            mst_weight += weight

    return mst_weight, mst_edges


# 例
edges = [
    (1, 0, 1),
    (4, 0, 2),
    (3, 1, 2),
    (2, 1, 3),
    (5, 2, 3),
    (1, 3, 4),
    (5, 2, 4)
]
N = 5  # 頂点数

mst_weight, mst_edges = kruskal(edges, N)
print("Minimum Spanning Tree Weight:", mst_weight)
print("Edges in MST:", mst_edges)
