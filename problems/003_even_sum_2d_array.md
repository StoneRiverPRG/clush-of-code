# Problem 003: Even Values at Even Positions (偶数位置の偶数和)
- **Difficulty:** Easy / Medium
- **Tags:** #2次元配列 #ネストしたループ #偶数判定 #スライス

## 📝 Original Statement
Sum all numbers in a 2d array where A[i][j] is even and i and j is even, where i,j represent row index and column index respectively. the array starts at 0,0. assume 0 is even.

Example:
h=3 w=3
2 4 7
8 3 1
1 0 8
The possible numbers to sum are in: (0,0)=2 (0,2)=7 (2,0)=1 (2,2)=8
Sum only even numbers: 2 + 8 = 10. hence the answer is 10.

## 🇯🇵 日本語問題文
2次元配列 $A$ において、**「行番号 $i$ が偶数」かつ「列番号 $j$ が偶数」**である場所に注目し、その場所にある**「値が偶数」**であるものの合計を求めてください。
※配列のインデックスは $(0, 0)$ から始まり、0は偶数として扱います。

## 💡 解説付き解答例
この問題には、「愚直にすべて調べる方法」と「効率よくスキップする方法」の2つがあります。

### パターン1：標準的な2重ループ（全探索）
全ての要素を順番にチェックし、条件を `if` 文で判定する方法です。
```python
h, w = map(int, input().split())
total = 0

for i in range(h):
    row = list(map(int, input().split()))
    for j in range(w):
        # 条件1: iが偶数, 条件2: jが偶数, 条件3: 値が偶数
        if i % 2 == 0 and j % 2 == 0 and row[j] % 2 == 0:
            total += row[j]

print(total)
```

**ポイント**: i % 2 == 0 を使うことで、0, 2, 4...番目の要素だけを狙い撃ちできます。

### パターン2：スライスによる効率化（Pythonic）
range(start, stop, step) を使って、最初から奇数行・奇数列を無視する方法です。

```python
h, w = map(int, input().split())
total = 0

for i in range(0, h, 2): # 0, 2, 4...番目の行だけをループ
    row = list(map(int, input().split()))
    # その行の 0, 2, 4...番目の値だけをスライス([::2])で取得
    for value in row[::2]:
        if value % 2 == 0: # 値が偶数かだけをチェック
            total += value

    # 奇数行の入力も読み飛ばす必要があるため、もし奇数行があれば空読みする
    if i + 1 < h:
        input()

print(total)
```

**ポイント**:
- row[::2] は「0番目から1つ飛ばしで最後まで」という意味です。コードがスッキリし、計算も少し速くなります。
- **「解答例のパターン2（スライス）」**にある「奇数行の読み飛ばし」の部分が少しトリッキーだったかもしれません。