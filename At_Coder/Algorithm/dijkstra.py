import heapq

n = 10  # 頂点数

# グラフの構築 リストのリスト．
# graph[i] = [(cost, next_stage), ...]
graph = [[] for _ in range(n + 1)]


def dijkstra(start, n):
    # dp[i]はステージiに達するための最短時間
    dp = [float('inf')] * (n + 1)  # 各頂点への最短コストを保持するリスト
    dp[start] = 0
    queue = [(0, start)]  # (cost, stage)

    while queue:
        current_cost, current_stage = heapq.heappop(queue)
        # なくてもよいが，若干時短．
        if dp[current_stage] < current_cost:
            continue

        for cost, next_stage in graph[current_stage]:
            if dp[next_stage] > current_cost + cost:  # 現在記憶しているコストよりも新たな経路のコストが小さい場合
                dp[next_stage] = current_cost + cost  # 更新
                # コストが更新されたため，頂点を経由する経路は再調査の必要あり．よってキューに追加．
                heapq.heappush(queue, (dp[next_stage], next_stage))

    return dp


dp = dijkstra(1, n)
# print(dp)
print(dp[n])
