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
def add_5(k):
    k += 5
    return k


a = 5
add_5(a)
print(a)
