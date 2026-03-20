### [010]: ビットカウンター (Bit Counter)
- **Difficulty:** Easy
- **Tags:** #bit #string #math

#### 📝 Original Statement (English)
Count the "1"s in the 8 bits and multiply the resulting integer by 2.

**Input**
line 1: 8 binary digits byte

**Output**
An integer N, which is double the "1"s that exist in the 8 binary digits given in input.

**Constraints**
`byte` is always 8 characters long

**Example**
Input
```
00101110
```
Output
```
8
```

#### 🇯🇵 日本語問題文
与えられた8ビットのバイナリ文字列（0と1の並び）の中に、"1"がいくつあるかを数え、その数に2を掛けた値を出力してください。

**入力**
1行目: 8文字のバイナリ文字列（例: `00101110`）

**出力**
"1"の個数を2倍した整数 N

**制約**
入力される文字列は常に8文字です。

#### 💡 解説付き解答例

- **Standard (Readable)**:
  文字列の `count` メソッドを使って "1" の個数を数える、最もシンプルで直感的な方法です。
```python
import sys

def solve():
    # 入力を読み込む
    line = sys.stdin.readline().strip()
    if not line:
        return
    
    # "1" の文字数を数える
    count_ones = line.count('1')
    
    # 2倍して出力
    print(count_ones * 2)

if __name__ == "__main__":
    solve()
```

- **Advanced (Efficient)**:
  Python 3.10以降で導入された `int.bit_count()` を使用する方法です。文字列を2進数として数値に変換してからビットを数えます。
```python
import sys

def solve():
    line = sys.stdin.readline().strip()
    if not line: return
    
    # 文字列を2進数として整数に変換し、立っているビット(1)を数える
    # bit_count() は非常に高速に動作します
    n = int(line, 2)
    print(n.bit_count() * 2)

if __name__ == "__main__":
    solve()
```

- **Shortest (Golfing)**:
  1行で記述した例です。
```python
print(input().count('1')*2)
```

#### 🧪 テストケース (Test Cases)
ユーザーが手動で動作確認するためのテストケースです。

| No | Input | Output | Description |
|:---|:---|:---|:---|
| 1 | `00101110` | `8` | 例題のケース (1が4個 -> 4*2=8) |
| 2 | `00000000` | `0` | 1が0個のケース |
| 3 | `11111111` | `16` | 1が8個のケース |
| 4 | `10101010` | `8` | 1が4個 (互い違い) |
| 5 | `00000001` | `2` | 1が1個のケース |

```python
# 以下のコードブロックに自分の回答を書き、上記のテストケースを TEST_INPUT に貼り付けて実行してください。
import sys
from io import StringIO

# --- 🧪 テスト実行用設定 ---
TEST_INPUT = """
00101110
"""
sys.stdin = StringIO(TEST_INPUT.strip())
# -----------------------

def solve():
    # ここにプログラミングを記述
    print(input().count('1')*2)

if __name__ == "__main__":
    solve()
```
