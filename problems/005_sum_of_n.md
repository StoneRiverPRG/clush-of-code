### 005: Sum of N Integers (数値の合計)
- **Difficulty:** Easy
- **Tags:** #math #sum #input

#### 📝 Original Statement (English)
The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests.

**Input:**
- An integer `N` (the number of integers to sum).
- `N` subsequent integers, each on a new line.

**Output:**
- The sum of the `N` integers.

#### 🇯🇵 日本語問題文
この問題は「REVERSE」モードです。問題文は提示されません。テストケースの入出力から、どのような処理を行うべきか推測してください。

**入力:**
- 最初に、合計したい整数の数 `N` が与えられます。
- 続く `N` 行に、それぞれの整数が与えられます。

**出力:**
- 与えられた `N` 個の整数の合計を出力してください。

#### 💡 解説付き解答例
- **Standard (Readable)**:
```python
import sys

# 標準入力からNを読み込む
n = int(input())
total = 0

# N回ループを回して、数値を1つずつ読み込み合計に加算する
for _ in range(n):
    num = int(input())
    total += num

# 合計を出力する
print(total)
```
もっとも標準的で読みやすい実装です。ループを使って1つずつ加算します。

- **Advanced (Efficient)**:
```python
import sys

# N個の数値をリスト内包表記で一気に読み込み、sum関数で合計を計算する
n = int(input())
total = sum(int(input()) for _ in range(n))

print(total)
```
リスト内包表記（またはジェネレータ式）と `sum()` 関数を組み合わせた、Pythonらしい簡潔な書き方です。

- **Shortest (Golfing)**:
```python
n,*a=map(int,open(0));print(sum(a))
```
`open(0)` で標準入力を読み込み、アンパックを使って `N` とそれ以降の数値リストを分け、合計を出力する短縮テクニックです。

#### 🧪 テストケース (Test Cases)
ユーザーが手動で動作確認するためのテストケースです。

| No | Input | Output | Description |
|:---|:---|:---|:---|
| 1 | `3\n1\n2\n3` | `6` | 3つの数値の合計 (1+2+3) |
| 2 | `5\n1\n2\n1\n10\n0` | `14` | 5つの数値の合計 |
| 3 | `2\n5\n2` | `7` | 2つの数値の合計 |
| 4 | `1\n8` | `8` | 1つの数値の合計 |
| 5 | `4\n42\n0\n1337\n666` | `2045` | 大きな数値を含む合計 |

```python
# 以下のコードブロックに自分の回答を書き、上記のテストケースを TEST_INPUT に貼り付けて実行してください。
import sys
from io import StringIO

# --- 🧪 テスト実行用設定 ---
TEST_INPUT = """
3
1
2
3
"""
sys.stdin = StringIO(TEST_INPUT.strip())
# -----------------------

def solve():
    # 競技プログラミング形式（input() など）でそのまま記述できます
    import sys
    
    # ここにプログラミングを記述
    # 例:
    # n = int(input())
    # print(sum(int(input()) for _ in range(n)))
    pass

if __name__ == "__main__":
    solve()
```
