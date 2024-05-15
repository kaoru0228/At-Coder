#include <iostream>
#include <vector>

int main()
{
    const int MOD = 100000000;
    int N;
    std::cin >> N;
    std::vector<int> A(N);
    for (int i = 0; i < N; ++i)
    {
        std::cin >> A[i];
    }

    long long result = 0;
    long long sum = 0;
    for (int i = N - 1; i >= 0; --i)
    {
        result += A[i] * sum;
        result %= MOD; // 途中で MOD で割ることでオーバーフローを防ぐ
        sum += A[i];
        sum %= MOD;
    }

    std::cout << result << std::endl;
    return 0;
}
