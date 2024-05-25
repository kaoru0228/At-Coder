// #include <iostream>
// #include <vector>
// using namespace std;

// int bingo_2(int N, int T, vector<int> &A)
// {
//     vector<vector<bool>> marked(N, vector<bool>(N, false));
//     vector<int> row_count(N, 0);
//     vector<int> col_count(N, 0);
//     int diag1_count = 0;
//     int diag2_count = 0;

//     for (int turn = 0; turn < T; ++turn)
//     {
//         int num = A[turn];
//         int i = (num - 1) / N;
//         int j = (num - 1) % N;
//         marked[i][j] = true;
//         row_count[i] += 1;
//         col_count[j] += 1;
//         if (i == j)
//         {
//             diag1_count += 1;
//         }
//         if (i + j == N - 1)
//         {
//             diag2_count += 1;
//         }

//         if (row_count[i] == N || col_count[j] == N || diag1_count == N || diag2_count == N)
//         {
//             return turn + 1;
//         }
//     }

//     return -1;
// }

// int main()
// {
//     int N, T;
//     cin >> N >> T;
//     vector<int> A(T);
//     for (int i = 0; i < T; ++i)
//     {
//         cin >> A[i];
//     }

//     cout << bingo_2(N, T, A) << endl;
//     return 0;
// }

// D Intersecting Intervals -----------------------------
// #include <iostream>
// #include <vector>
// #include <algorithm>

// using namespace std;

// struct Interval
// {
//     int start, end;
// };

// bool compareStart(const Interval &a, const Interval &b)
// {
//     return a.start < b.start;
// }

// bool compareEnd(const Interval &a, const Interval &b)
// {
//     return a.end < b.end;
// }

// int countIntersectingPairs(vector<Interval> &intervals)
// {
//     int N = intervals.size();
//     vector<int> starts(N), ends(N);

//     for (int i = 0; i < N; ++i)
//     {
//         starts[i] = intervals[i].start;
//         ends[i] = intervals[i].end;
//     }

//     sort(starts.begin(), starts.end());
//     sort(ends.begin(), ends.end());

//     int i = 0, j = 0, count = 0, active = 0;
//     while (i < N)
//     {
//         if (starts[i] <= ends[j])
//         {
//             active++;
//             count += active - 1;
//             i++;
//         }
//         else
//         {
//             active--;
//             j++;
//         }
//     }

//     return count;
// }

// int main()
// {
//     int N;
//     cin >> N;
//     vector<Interval> intervals(N);

//     for (int i = 0; i < N; ++i)
//     {
//         cin >> intervals[i].start >> intervals[i].end;
//     }

//     int result = countIntersectingPairs(intervals);
//     cout << result << endl;

//     return 0;
// }

// 修正Ver -----------------------------

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Event
{
    int time;
    int type; // 1 for start, -1 for end
};

int countIntersectingPairs(vector<pair<int, int>> &intervals)
{
    vector<Event> events;
    for (const auto &interval : intervals)
    {
        events.push_back({interval.first, 1});
        events.push_back({interval.second, -1});
    }

    // ソート基準は、timeが小さい順、同じtimeの場合はtypeが小さい順（終了イベントが先）
    sort(events.begin(), events.end(), [](const Event &a, const Event &b)
         {
        if (a.time != b.time)
            return a.time < b.time;
        return a.type < b.type; });

    int active_intervals = 0;
    int intersecting_pairs = 0;

    for (const auto &event : events)
    {
        if (event.type == 1)
        { // 開始イベント
            intersecting_pairs += active_intervals;
            active_intervals++;
        }
        else
        { // 終了イベント
            active_intervals--;
        }
    }

    return intersecting_pairs;
}

int main()
{
    int N;
    cin >> N;
    vector<pair<int, int>> intervals(N);

    for (int i = 0; i < N; ++i)
    {
        cin >> intervals[i].first >> intervals[i].second;
    }

    int result = countIntersectingPairs(intervals);
    cout << result << endl;

    return 0;
}
