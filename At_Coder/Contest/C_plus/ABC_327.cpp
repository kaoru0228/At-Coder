// D Good Tuple Problem
#include <iostream>
#include <vector>
using namespace std;

constexpr int nmax = 200200;
int N, M;
int A[nmax], B[nmax];
vector<int> g[nmax];
int X[nmax];
int bipartite = true;

void dfs(int c, int x)
{           // c:頂点，x:与えるグループ名(0 or 1)
  X[c] = x; // 頂点cにグループxを割り当て
  for (auto &d : g[c])
  { // 頂点cと隣り合う頂点 g[c] に対して，深さ優先でたどりながらグループを与えて行く
    if (X[d] == -1)
    {                // 隣り合う頂点が未探索だった場合
      dfs(d, 1 - x); // その頂点を現在の頂点と異なるグループとし，さらに深く探索を行う．
    }
    else if (X[d] == X[c])
    { // 隣り合う頂点が探索済みで，同じグループに属する場合，アウト．
      bipartite = false;
    }
  }
}
int main()
{
  cin >> N >> M;
  for (int i = 0; i < M; i++)
    cin >> A[i], A[i]--;
  for (int i = 0; i < M; i++)
    cin >> B[i], B[i]--;
  for (int i = 0; i < M; i++)
  {
    g[A[i]].push_back(B[i]);
    g[B[i]].push_back(A[i]);
  }
  for (int i = 0; i < N; i++)
    X[i] = -1;
  for (int i = 0; i < N; i++)
  {
    if (X[i] == -1)
      dfs(i, 0);
  }
  cout << (bipartite ? "Yes" : "No") << endl;
}