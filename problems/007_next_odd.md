### 007: Next Odd Number (次なる奇数)
- **Difficulty:** Easy
- **Tags:** #math #logic #odd-even

#### 📝 Original Statement (English)
You will be given `M` values. Each value is an integer `N`. You must print the next highest odd number unless `N` is already odd, then print `N`.

**Input:**
- **Line 1:** An integer `M` for the number of integer values that follow.
- **Next M Lines:** `M` number of integer values.

**Output:**
- **M Lines:** `M` integers. If the integer `N` is odd, print `N`; otherwise, print the next highest odd integer (`N + 1`).

**Constraints:**
- 1 <= M <= 100
- -10000 <= N <= 10000

---
**Example:**
Input:
```
3
1
2
3
```
Output:
```
1
3
3
```

#### 🇯🇵 日本語問題文
`M` 個の数値が与えられます。それぞれの数値 `N` について、`N` が奇数ならそのまま `N` を、`N` が偶数ならその次に大きい奇数（`N + 1`）を出力してください。

**入力:**
- **1行目:** 続く整数の数 `M`。
- **続く M 行:** `M` 個の整数 `N`。

**出力:**
- **M 行:** それぞれの入力に対する判定結果。`N` が奇数なら `N`、偶数なら `N + 1` を出力します。

**制約:**
- 1 <= M <= 100
- -10000 <= N <= 10000

#### 💡 解説付き解答例
- **Standard (Readable)**:
```python
import sys

# 数値の個数 M を読み込む
m = int(input())

for _ in range(m):
    # 数値 N を読み込む
    n = int(input())
    
    # 2 で割った余りが 0 なら偶数
    if n % 2 == 0:
        print(n + 1)
    else:
        # 奇数ならそのまま出力
        print(n)
```
もっとも直感的で分かりやすい `if-else` による実装です。

- **Advanced (Efficient)**:
```python
import sys

m = int(input())
for _ in range(m):
    n = int(input())
    # ビット演算子 | (OR) を使う
    # 偶数は最下位ビットが 0 なので、1 と OR を取ると +1 される
    # 奇数は最下位ビットが 1 なので、1 と OR を取っても変わらない
    print(n | 1)
```
ビット演算を利用したスマートな方法です。`n | 1` は、偶数の場合は `n + 1` になり、奇数の場合は `n` のままになります。

- **Shortest (Golfing)**:
```python
input();[print(int(n)|1)for n in open(0)]
```
1行目を読み飛ばし、残りの標準入力をループしてビット演算で出力する短縮コードです。

#### 🧪 テストケース (Test Cases)
ユーザーが手動で動作確認するためのテストケースです。

| No | Input | Output | Description |
|:---|:---|:---|:---|
| 1 | `3\n1\n2\n3` | `1\n3\n3` | 基本的なケース (奇、偶、奇) |
| 2 | `2\n0\n-2` | `1\n-1` | 0と負の偶数 |
| 3 | `2\n-1\n-3` | `-1\n-3` | 負の奇数 |
| 4 | `1\n10000` | `10001` | 最大制約付近の偶数 |
| 5 | `4\n10\n11\n12\n13` | `11\n11\n13\n13` | 連続する数値 |

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
    # m = int(input())
    # ...
    pass

if __name__ == "__main__":
    solve()
```
