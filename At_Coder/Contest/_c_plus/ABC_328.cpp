// #include <iostream>
// int n, x, s[10]
// cin >> n >> x;
// for(int i = 0; i < n; i++) cin >> s[i];
// cout << ans << endl;

// トヨタシステムズプログラミングコンテスト2023(AtCoder Beginner Contest 330)
// https://atcoder.jp/contests/abc330

// -----------------------------
// A

// #include <iostream>
// using namespace std;

// int main(void)
// {
//     int n, x, s[8];
//     cin >> n >> x;
//     for (int i = 0; i < n; i++)
//         cin >> s[i];

//     int ans = 0;
//     for (int i = 0; i < n; i++)
//         if (s[i] <= x)
//             ans += s[i];
//     cout << ans << endl;

//     return 0;
// }

// -----------------------------
// B

// 1. それぞれの日付がゾロ目かチェックする
//  #include <iostream>
//  #include <vector>
//  #include <set>

// using namespace std;

// int main() {
//     int N;
//     cin >> N;
//     vector<int> D(N);
//     for (auto &&d : D)
//         cin >> d;

//     int ans = 0;
//     for (int m = 1; m <= N; ++m) {
//         string month = to_string(m);
//         for (int d = 1; d <= D[m - 1]; ++d) {
//             string date = month + to_string(d);
//             if (size(set<char>(date.begin(), date.end())) == 1)
//                 ++ans;
//         }
//     }
//     cout << ans << endl;

//     return 0;
// }

// 2. ゾロ目の日付が存在するかチェックする
//  #include <iostream>
//  #include <vector>
//  #include <utility>

// using namespace std;

// int main() {
//     int N;
//     cin >> N;
//     vector<int> D(N);
//     for(auto&& d : D)cin >> d;

//     vector<pair<int, int>> zorome; // ありえるゾロ目の日付
//     for(int i = 1; i <= 9; ++i){
//         zorome.emplace_back(i, i);
//         zorome.emplace_back(i, i * 11);
//         zorome.emplace_back(i * 11, i);
//         zorome.emplace_back(i * 11, i * 11);
//     }

//     int ans{};
//     for(const auto& [month, day] : zorome)
//         if(month <= N && day <= D[month - 1])
//             ++ans;

//     cout << ans << endl;

//     return 0;
// }

// -----------------------------
// C

// #include <iostream>
// using namespace std;

// int n, q;
// char s[300001];
// int a[300000], b[300000];

// int main(void)
// {
//   cin >> n >> q;
//   for(int i = 1; i <= n; i++) cin >> s[i];

//   for(int i = 1; i <= n-1; i++) if(s[i] == s[i+1]) a[i] = 1;
//   for(int i = 1; i <= n-1; i++) b[i] = b[i-1] + a[i];

//   int l, r;
//   for(int i = 1; i <= q; i++){
//     cin >> l >> r;
//     cout << b[r-1]-b[l-1] << "\n";
//   }

//   return 0;
// }

// -----------------------------
// D

// #include <iostream>
// using namespace std;

// int main(void)
// {
//   string s, ans;
//   cin >> s;

//   for(auto c : s){
//     ans += c;
//     if(ans.size() >= 3 && ans.substr(ans.size()-3) == "ABC") ans.erase(ans.end()-3, ans.end());
//   }
//   cout << ans << endl;

//   return 0;
// }

// -----------------------------
// E

// -----------------------------
// F

// -----------------------------
// G