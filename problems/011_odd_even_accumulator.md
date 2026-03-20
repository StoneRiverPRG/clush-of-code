### [011]: 奇偶アキュムレータ (Odd-Even Accumulator)
- **Difficulty:** Easy
- **Tags:** #math #loop #logic

#### 📝 Original Statement (English)
Initially output equals 0. Iterate through each number in the input and perform the following operation:
- If the number is odd: Multiply it to output
- If the number is even: Add it to the output

**Input**
Line 1: An integer `count` which represents the amount of given numbers.
Line 2: A list of integer numbers of length `count` separated by space.

**Output**
Line 1: An integer `output`

**Constraints**
0 < `count` ≤ 100
-10000 ≤ `number` ≤ 10000
-2147483648 < `output` < 2147483648

**Example**
Input
```
5
2 4 8 10 6
```
Output
```
30
```

#### 🇯🇵 日本語問題文
初期値を 0 とした変数 `output` に対して、与えられた数値のリストを順番に処理し、以下のルールに従って更新してください。

- 与えられた数値が**奇数**の場合： `output` にその数値を**掛ける** (`output *= number`)
- 与えられた数値が**偶数**の場合： `output` にその数値を**足す** (`output += number`)

最終的な `output` の値を出力してください。

**入力**
1行目: 数値の個数 `count`
2行目: スペース区切りの `count` 個の整数

**出力**
計算後の `output` の値

**制約**
0 < `count` ≤ 100
-10000 ≤ `number` ≤ 10000
-2147483648 < `output` < 2147483648

#### 💡 解説付き解答例

- **Standard (Readable)**:
  `for` ループと `if-else` 文を使った最も基本的で読みやすい実装です。
```python
import sys

def solve():
    # 入力を読み込む
    try:
        input_data = sys.stdin.read().split()
        if not input_data: return
        
        count = int(input_data[0])
        numbers = list(map(int, input_data[1:]))
    except:
        return
    
    # 初期値は 0
    output = 0
    
    for n in numbers:
        if n % 2 != 0:
            # 奇数の場合は掛ける
            output *= n
        else:
            # 偶数の場合は足す
            output += n
            
    print(output)

if __name__ == "__main__":
    solve()
```

- **Advanced (Efficient)**:
  `functools.reduce` を使用した関数型プログラミングスタイルの実装です。累積計算をスマートに記述できます。
```python
import sys
from functools import reduce

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2: return
    
    numbers = map(int, input_data[1:])
    
    # reduce(関数, イテラブル, 初期値)
    result = reduce(lambda acc, n: acc * n if n % 2 else acc + n, numbers, 0)
    print(result)

if __name__ == "__main__":
    solve()
```

- **Shortest (Golfing)**:
  1行で記述した例です。
```python
r=0;input();[r:=r*x if x%2 else r+x for x in map(int,input().split())];print(r)
```

#### 🧪 テストケース (Test Cases)
ユーザーが手動で動作確認するためのテストケースです。

| No | Input | Output | Description |
|:---|:---|:---|:---|
| 1 | `5\n2 4 8 10 6` | `30` | すべて偶数のケース (0+2+4+8+10+6=30) |
| 2 | `3\n2 3 4` | `10` | 偶数・奇数混在 (0+2=2, 2*3=6, 6+4=10) |
| 3 | `2\n3 5` | `0` | 最初に奇数が来るケース (0*3=0, 0*5=0) |
| 4 | `4\n1 2 3 4` | `10` | 奇数から始まる (0*1=0, 0+2=2, 2*3=6, 6+4=10) |
| 5 | `4\n2 -1 4 -3` | `-6` | 負の数を含むケース |

```python
# 以下のコードブロックに自分の回答を書き、上記のテストケースを TEST_INPUT に貼り付けて実行してください。
import sys
from io import StringIO

# --- 🧪 テスト実行用設定 ---
TEST_INPUT = """
5
2 4 8 10 6
"""
sys.stdin = StringIO(TEST_INPUT.strip())
# -----------------------

def solve():
    # ここにプログラミングを記述
    r = 0
    input()
    for x in map(int, input().split()):
        r = r * x if x % 2 else r + x
    print(r)

if __name__ == "__main__":
    solve()
```
