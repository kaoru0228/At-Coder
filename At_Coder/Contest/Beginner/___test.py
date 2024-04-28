import numpy as py


# DataFrame型の基本的操作
# import pandas as pd
# data = {'列1': [1, 2, 3], '列2': ['a', 'b', 'c']}
# df = pd.DataFrame(data)

# print(df)
# print(df['列1'])
# print(df.loc[0])
# print(df.iloc[0])
# df['新しい列'] = [4, 5, 6]
# print(df)
# df.loc[len(df)] = [4, 'd', 7]
# print(df)
# df.drop('列2', axis=1, inplace=True)
# print(df)
# df.drop(0, axis=0, inplace=True)
# print(df)

# # '列1'が3より以上の行を取得
# data = {'列1': [1, 2, 3, 4, 5], '列2': [1, 3, 5, 7, 9]}
# df = pd.DataFrame(data)
# print(df)
# filtered_df = df[df['列1'] >= 3]
# print(filtered_df)

# list_ = []
# for index, row in filtered_df.iterrows():
#     list_.append(row.tolist())
# print(list_)


# ---------------------------
# def add_5(k):
#     k += 5
#     return k
# a = 5
# print(add_5(a))
# print(a)

# ビットシフト ---------------------------
# a = 2
# print(a)
# a = a >> 2 | 1
# print(a)
# a <<= 2
# print(a)

# 排他的論理和 -----------------
# a = 63  # 111111
# b = 21  # 010101
# print(a ^ b)
# print(bin(a ^ b)[2:])
# print(type(bin(a ^ b)[2:]))


# DataFrame型 -----------------
# import pandas as pd

# data = {'ID': [1, 2], 'Name': ['Alice', 'Bob']}
# df = pd.DataFrame(data)
# print(df)
# print(df['ID'][0])
# print(df.iloc[0])
# print(df.columns)
# print(df.shape)

# リストの初期化 -----------------
# a = [[] for _ in range(10)]
# a[0].append(1)
# print(a)

# for文 printされない---------------------------
# for i in range(0, 0, -1):
#     print(i)


# 　range ---------------------------
# for a in range(-3, 3, 1):
#     print(a)

# リストの連結 ---------------------------
# a = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# b = [4, 5, 6]
# c = a + b
# print(c)

# ---------------------------
