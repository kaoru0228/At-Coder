# セグメントツリーの実装（今回は，配列の和）
# 根ノードのインデックス番号を1としている．よって，tree[0]は使っていない．
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (2 * self.n)  # セグメントツリーを配列で表現

        # ツリーの葉に配列の要素をセット
        for i in range(self.n, 2 * self.n):
            self.tree[i] = arr[i - self.n]

        # 内部ノードを構築
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, pos, val):
        # posは更新したい値のインデックス(1~n)，valはその位置にセットしたい値
        pos += self.n  # 葉の位置に移動
        self.tree[pos] = val  # 葉を更新
        while pos > 1:  # 根ノードにたどり着くまで更新
            pos >>= 1  # 親ノードに移動（1ビット右にシフト = 2で割って余りを切り捨て）
            self.tree[pos] = self.tree[pos << 1] + \
                self.tree[pos << 1 | 1]  # 親ノードを更新（親=左右の子の和）

    def query(self, l, r):
        # [l, r) の区間の合計を求める
        l += self.n  # 葉の位置に移動
        r += self.n
        total = 0
        while l <= r:
            if l & 1:  # lが右の子なら，その値を足して一つ右へ移動
                total += self.tree[l]
                l += 1
            if r & 1:  # (r-1)が左の子なら，その値を足して一つ左へ移動(rは回区間に入り含まれない)
                total += self.tree[r-1]
                r -= 1
            # この時点でlは左の子，(r-1)は右の子となっているため，親ノードへ移動
            l >>= 1
            r >>= 1
        return total

    def get(self):
        return self.tree


# 使用例
# ※ 関数に渡す区間のインデックスは，0からカウント
arr = [1, 2, 3, 4, 5]
st = SegmentTree(arr)
print('セグメントツリー：', st.get())
print("初期状態の区間合計 [1, 5):", st.query(1, 5))
st.update(2, 10)  # arr[2]の値を10に更新
print(st.tree)
print("更新後の区間合計 [0, 5):", st.query(0, 5))
