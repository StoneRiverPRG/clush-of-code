### [009]: 斜辺の計算機 (Hypotenuse Calculator)
- **Difficulty:** Easy
- **Tags:** #math #sqrt #round

#### 📝 Original Statement (English)
Find the hypotenuse of a right triangle given the length of the legs. Round to the nearest integer.

**Input**
Line 1: `leg_1`
Line 2: `leg_2`

**Output**
length of the hypotenuse

**Constraints**
1 ≤ `leg_1` ≤ 25
1 ≤ `leg_2` ≤ 25

**Example**
Input
```
2
3
```
Output
```
4
```

#### 🇯🇵 日本語問題文
直角三角形の2つの隣辺（足）の長さが与えられたとき、斜辺（もっとも長い辺）の長さを求めてください。
結果は最も近い整数に四捨五入して出力してください。

**入力**
1行目: 隣辺1の長さ `leg_1`
2行目: 隣辺2の長さ `leg_2`

**出力**
斜辺の長さ（整数）

**制約**
1 ≤ `leg_1` ≤ 25
1 ≤ `leg_2` ≤ 25

#### 💡 解説付き解答例

- **Standard (Readable)**:
  `math.sqrt` を使って平方根を計算し、`round` 関数で四捨五入する素直な方法です。
```python
import sys
import math

def solve():
    # 入力を2行分読み込む
    try:
        a = int(sys.stdin.readline())
        b = int(sys.stdin.readline())
    except:
        return

    # ピタゴラスの定理: c = sqrt(a^2 + b^2)
    hypotenuse = math.sqrt(a**2 + b**2)
    
    # 最も近い整数に四捨五入して出力
    print(round(hypotenuse))

if __name__ == "__main__":
    solve()
```

- **Advanced (Efficient)**:
  Python 3.5以降で利用可能な `math.hypot` 関数を使用します。これは斜辺の計算を直接行うための関数で、精度や速度の面で最適化されています。
```python
import sys
import math

def solve():
    # mapとsys.stdin.read().split()を使って入力をまとめて数値に変換
    nums = list(map(int, sys.stdin.read().split()))
    if len(nums) < 2: return
    
    # math.hypot は sqrt(x*x + y*y) を計算する
    print(round(math.hypot(*nums)))

if __name__ == "__main__":
    solve()
```

- **Shortest (Golfing)**:
  1行で記述した例です。
```python
import math,sys;print(round(math.hypot(*map(int,sys.stdin.read().split()))))
```

#### 🧪 テストケース (Test Cases)
ユーザーが手動で動作確認するためのテストケースです。

| No | Input | Output | Description |
|:---|:---|:---|:---|
| 1 | `2\n3` | `4` | 例題のケース (sqrt(13) ≈ 3.6 -> 4) |
| 2 | `3\n4` | `5` | 3:4:5 の直角三角形 |
| 3 | `5\n12` | `13` | 5:12:13 の直角三角形 |
| 4 | `1\n1` | `1` | sqrt(2) ≈ 1.41 -> 1 |
| 5 | `25\n25` | `35` | 最大値のケース (sqrt(1250) ≈ 35.35 -> 35) |

```python
# 以下のコードブロックに自分の回答を書き、上記のテストケースを TEST_INPUT に貼り付けて実行してください。
import sys
from io import StringIO

# --- 🧪 テスト実行用設定 ---
TEST_INPUT = """
2
3
"""
sys.stdin = StringIO(TEST_INPUT.strip())
# -----------------------

def solve():
    import math
    a = int(input())
    b = int(input())
    print(round(math.hypot(a, b)))

if __name__ == "__main__":
    solve()
```
