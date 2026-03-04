# Problem 000: Title of ploblem (問題のタイトルを日本語で)
- **Difficulty:** Easy / Medium / difficult
- **Tags:** #hash-tag1, #hash_tag2, ...

## 📝 Original Statement
（英語の問題分を整形して載せる。以下は例。）
Sum all numbers in a 2d array where A[i][j] is even and i and j is even, where i,j represent row index and column index respectively. the array starts at 0,0. assume 0 is even.

Example:
h=3 w=3
2 4 7
8 3 1
1 0 8
The possible numbers to sum are in: (0,0)=2 (0,2)=7 (2,0)=1 (2,2)=8
Sum only even numbers: 2 + 8 = 10. hence the answer is 10.

## 🇯🇵 日本語問題文
（英語の問題文が与えらえた時は日本語にした問題文を載せる。）
（AIが生成した問題はここに日本語問題文のみ載せる。以下は例。）
2次元配列 $A$ において、**「行番号 $i$ が偶数」かつ「列番号 $j$ が偶数」**である場所に注目し、その場所にある**「値が偶数」**であるものの合計を求めてください。
※配列のインデックスは $(0, 0)$ から始まり、0は偶数として扱います。

## 💡 解説付き解答例
（以下は例。）
この問題には、「愚直にすべて調べる方法」と「効率よくスキップする方法」の2つがあります。

### パターン1：（パターンのタイトル）
全ての要素を順番にチェックし、条件を `if` 文で判定する方法です。
```python
# パターン1：（パターンタイトル）
```

**ポイント**: i % 2 == 0 を使うことで、0, 2, 4...番目の要素だけを狙い撃ちできます。

### パターン2：（パターンのタイトル（Pythonic））
range(start, stop, step) を使って、最初から奇数行・奇数列を無視する方法です。

```python
# パターン2：（パターンタイトル）
```

**ポイント**:
- row[::2] は「0番目から1つ飛ばしで最後まで」という意味です。コードがスッキリし、計算も少し速くなります。
- **「解答例のパターン2（スライス）」**にある「奇数行の読み飛ばし」の部分が少しトリッキーだったかもしれません。