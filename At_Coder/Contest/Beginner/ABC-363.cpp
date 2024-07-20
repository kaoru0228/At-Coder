// g++ -o test file_name.cpp
// test

#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

bool is_palindrome(const string &s)
{
    int left = 0;
    int right = s.size() - 1;
    while (left < right)
    {
        if (s[left] != s[right])
        {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int count_valid_permutations(int N, int K, const string &S)
{
    set<string> permutations;
    string str = S;
    sort(str.begin(), str.end());
    do
    {
        permutations.insert(str);
    } while (next_permutation(str.begin(), str.end()));

    int count = 0;

    for (const auto &perm : permutations)
    {
        bool valid = true;
        for (int i = 0; i <= N - K; i++)
        {
            if (is_palindrome(perm.substr(i, K)))
            {
                valid = false;
                break;
            }
        }
        if (valid)
        {
            count += 1;
        }
    }

    return count;
}

int main()
{
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;

    cout << count_valid_permutations(N, K, S) << endl;

    return 0;
}
