def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # 目的の値が見つかった場合、そのインデックスを返す
        elif arr[mid] < target:
            left = mid + 1  # 目的の値が中央値より大きい場合、左端を中央の右に移動
        else:
            right = mid - 1  # 目的の値が中央値より小さい場合、右端を中央の左に移動

    return -1  # 目的の値が見つからなかった場合、-1を返す


# ソートされた配列と探索対象の値
arr = [1, 2, 4, 5, 7, 8, 12]
target = 5

# 二分探索の実行
index = binary_search(arr, target)

# 結果の出力
print(index)
