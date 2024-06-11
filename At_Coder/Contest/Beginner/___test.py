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
# all ()
# a = [True, True, '']
# b = []
# print(all(a))
# print(all(b))


# for文の内包表現 ---------------------------
# a = [1, 2, 3, 4, 5, 3]
# b = [x**2 for x in a]
# c = {x**2 for x in a} # set型（集合）
# print(a)
# print(b)
# print(c)


# 文字列 ---------------------------
# a = 'a'*3
# print(a)


# ---------------------------
# リスト b = [[]]*3 という書き方では，参照先がダブってしまう．
# a = [0]*3
# b = [[]]*3
# b[0].append(0)
# b[2] = 2
# b[1].append(1)
# b[0].append(4)
# print(a)
# print(b)
# 正しい表現 -----
# c = [[] for _ in range(3)]
# print(c)


# ---------------------------
# 関数とポインタ　アドレスで指定しなくても，リストなら引数に与えたリストの中身を書き換えてくれる
# a = [0]*3
# def test01(b):
#     b[0] = 1
# print(a)
# test01(a)
# print(a)

# ---------------------------
# def test02(b, c): # int, strなどの不変値は書き換わらない．return（返り値）を利用するしかない-----
#     b += 1
#     c = 'a'
# a = 1
# d = 'b'
# print(a, d)
# test02(a, d)
# print(a, d)

# ---------------------------
# a = 'aaa bbb'
# b = 'aaa'
# c = list(a.split())
# d = list(b.split())
# print(c, d)

# b, c, k = 'a b'.split()

# ---------------------------
# ---------------------------
# ---------------------------
# ---------------------------
# ---------------------------
# ---------------------------
# ---------------------------

import sys
import copy
from datetime import datetime
import calendar


# 2022年の各日付について、発送可能な商品数を管理するリスト
def make_year_rest(m, n, hi):
    # 2022年1月1日の曜日を取得(月曜日 = 0, ..., 日曜日 = 6)
    weekday_num = calendar.weekday(2022, 1, 1)

    # hiの条件(h0=日曜日)に合わせる
    weekday_num = (weekday_num+1) % 7

    year_rest = []
    for i in range(365):
        if hi[weekday_num] == 1:
            year_rest.append([m]*n)
        else:
            year_rest.append([0]*n)
        weekday_num = (weekday_num+1) % 7
    return year_rest


# 日付を受け取り、一年の何日目かを返す関数
# 引数　date：yyyy-MM-ddTHH:mm:ss
def day_of_year(date):

    # 日付部分を datetime オブジェクトに変換
    date_obj = datetime.strptime(date, "%Y-%m-%d")

    # 一年における何日目かを計算
    day_of_year = date_obj.timetuple().tm_yday

    return day_of_year


# 注文クエリを受け取り、指定日に発送可能かを確認する関数。発送可能ならTrue、不可能ならFalseを返す
# 引数　t：クエリ取得日時, b：注文番号, c：発送日の日付, k：注文する商品の種類数, xi：商品番号のリスト, yi：注文する個数のリスト, year_rest：発送可能残数を示すリスト, shipping_scheduled：発送予定の注文, item_idx：商品のインデックスを確認する辞書, is_update：shipping_scheduledを更新するかどうかの真偽値（発送日変更クエリの際は更新しない）
def order(t, b, c, k, xi, yi, year_rest, shipping_scheduled, item_idx, is_update=True):

    # 更新前のリストをコピー（注文を拒否する際に必要）
    year_rest_copy = copy.deepcopy(year_rest)

    days = day_of_year(c)

    for x, y in zip(xi, yi):
        x_idx = item_idx[x]
        if year_rest[days-1][x_idx-1] >= y:
            year_rest[days-1][x_idx-1] -= y
        else:
            # 発送できない商品があったため、受理しない。また、受理しないため発送可能残数は更新しない。
            is_order = False
            return is_order, year_rest_copy

    # すべての商品を発送可能であったため受理
    is_order = True

    # 注文クエリの際は更新、発送日変更クエリの場合は更新なし（元の発送日の発送可能個数を修正するために必要な情報であるため）
    if is_update:
        shipping_scheduled[b] = (days, xi, yi)

    return is_order, year_rest

# 注文取り消しクエリを受け取り、取り消しの実行（発送する商品の更新）を行う関数
# 引数　t：クエリ取得日時, b：注文番号, year_rest：発送可能残数を示すリスト, shipping_scheduled：発送予定の注文, item_idx：商品のインデックスを確認する辞書


def cancel(t, b, year_rest, shipping_scheduled, item_idx):

    days, xi, yi = shipping_scheduled[b]

    # 注文を取り消すため、発送可能残数を復元する
    for x, y in zip(xi, yi):
        x_idx = item_idx[x]
        year_rest[days-1][x_idx-1] += y

    # 発送リストから注文を削除
    del shipping_scheduled[b]

    return year_rest, shipping_scheduled

# 発送クエリを受け取り、標準出力を行う関数
# 引数　t：クエリ取得日時, year_rest：発送可能残数を示すリスト, shipping_scheduled：発送予定の注文


def ship(t, shipping_scheduled):
    # 発送日の取得
    date = t.split("T")[0]
    day = day_of_year(date)

    # 発送日が一致する注文番号を取得
    orders = []
    for key, value in shipping_scheduled.items():
        if value[0] == day:
            orders.append(key)
    for key in orders:
        del shipping_scheduled[key]

    # 辞書順にソート
    orders = sorted(orders)

    # 発送する注文数
    num_orders = len(orders)

    if len(orders) > 0:
        print(f'{t} Shipped {num_orders} Orders')
        print(*orders)

    return shipping_scheduled


def main(lines):

    # サイト情報を受け取り、各変数へ代入
    n, m, d = map(int, lines[0].split())
    ai = list(lines[1].split())
    hi = list(map(int, lines[2].split()))
    q = int(lines[3])

    # 各商品を 1~N のインデックスで管理
    item_idx = {}
    for i in range(n):
        item_idx[ai[i]] = i+1

    # 2022年の各日付について、発送可能な商品数を管理するリスト
    year_rest = make_year_rest(m, n, hi)

    # 発送予定の注文を保持する辞書（キー：注文番号、要素：(発送日, 各所品の種類, 個数)）
    shipping_scheduled = {}

    # クエリの処理（サイト情報以外の標準入力の処理）
    for i, v in enumerate(lines[4:]):
        i += 4  # vとlinesのインデックスを合わせるため（サイト情報の分インデックスが4ずれている）
        query = list(v.split())

        # 注文クエリ
        if 'ORDER' in query:
            # クエリ発行日時(t)、注文番号(b)、発送日の日付(c)、注文する商品の種類数(k)
            t = query[1]
            b, c, k = lines[i+1].split()
            k = int(k)

            # 各商品の情報(xi:商品番号のリスト、yi:注文する個数のリスト)
            xi = []
            yi = []
            for j in range(k):
                x, y = lines[i+2+j].split()
                xi.append(x)
                yi.append(int(y))

            # クエリの実行
            is_order, year_rest = order(
                t, b, c, k, xi, yi, year_rest, shipping_scheduled, item_idx)
            if is_order:
                print(f'{t} Ordered {b}')
            else:
                print(
                    f'{t} Ordered {b} Error: the number of available shipments has been exceeded.')

        # 注文取消しクエリ
        elif 'CANCEL' in query:
            # クエリ発行日時(t)、注文番号(b)
            t = query[1]
            b = lines[i+1]

            # クエリの実行
            year_rest, shipping_scheduled = cancel(
                t, b, year_rest, shipping_scheduled, item_idx)
            print(f'{t} Canceled {b}')

        # 発送クエリ
        elif 'SHIP' in query:
            t = query[1]

            # クエリの実行
            ship(t, shipping_scheduled)

        # 以下、応用実装 ---------------------------
        # 発送日変更クエリ
        elif 'CHANGE' in query:
            # クエリ発行日時(t)、注文番号(b)、変更後の発送日の日付(c)
            t = query[1]
            b, c = lines[i+1].split()

            # 変更後の日付を取得
            day = day_of_year(c)

            # 発送日が変更可能かを確認
            is_order, year_rest = order(
                t, b, c, k, xi, yi, year_rest, shipping_scheduled, item_idx, is_update=False)

            # 変更可能であった場合、元の日付をキャンセル
            if is_order:
                cancel(t, b, year_rest, shipping_scheduled, item_idx)

                # 更新された注文を追加
                shipping_scheduled[b] = (day, xi, yi)

                print(f'{t} Changed {b}')
            else:
                print(
                    f'{t} Changed {b} Error: the number of available shipments has been exceeded.')

        # 発送可能数拡充クエリ
        elif 'EXPAND' in query:
            # クエリ発行日時(t)、期間の開始日と終了日(c1, c2)、拡充する個数(f)
            t = query[1]
            c1, c2, f = lines[i+1].split()
            f = int(f)
            day1 = day_of_year(c1)
            day2 = day_of_year(c2)

            # 指定した期間の発送可能数を拡充
            for i in range(day2-day1+1):
                for j in range(n):
                    year_rest[day1-1+i][j] += f

            print(f'{t} Expanded')

        # クエリの先頭でない場合はスキップ(なくても可)
        else:
            continue


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)


# 正解
# 2022-01-01T01:00:00 Ordered AAAAAAAAAA Error: the number of available shipments has been exceeded.
# 2022-01-01T02:00:00 Expanded
# 2022-01-01T03:00:00 Ordered BBBBBBBBBB
# 2022-01-01T04:00:00 Ordered CCCCCCCCCC
# 2022-01-02T00:00:00 Shipped 1 Orders
# BBBBBBBBBB
# 2022-01-02T01:00:00 Ordered DDDDDDDDDD
# 2022-01-02T02:00:00 Changed CCCCCCCCCC Error: the number of available shipments has been exceeded.
# 2022-01-02T03:00:00 Changed DDDDDDDDDD
# 2022-01-03T00:00:00 Shipped 1 Orders
# CCCCCCCCCC
# 2022-01-04T00:00:00 Shipped 1 Orders
# DDDDDDDDDD

# 自分の解答
# 2022-01-01T01:00:00 Ordered AAAAAAAAAA Error: the number of available shipments has been exceeded.
# 2022-01-01T02:00:00 Expanded
# 2022-01-01T03:00:00 Ordered BBBBBBBBBB
# 2022-01-01T04:00:00 Ordered CCCCCCCCCC
# 2022-01-02T00:00:00 Shipped 1 Orders
# BBBBBBBBBB
# 2022-01-02T01:00:00 Ordered DDDDDDDDDD
# 2022-01-02T02:00:00 Changed CCCCCCCCCC
# 2022-01-02T03:00:00 Changed DDDDDDDDDD
# 2022-01-04T00:00:00 Shipped 2 Orders
# CCCCCCCCCC DDDDDDDDDD
