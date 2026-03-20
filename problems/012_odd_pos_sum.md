### [012]: 奇数番目合計 (Odd Position Sum) - REVERSE Mode
- **Difficulty:** Easy
- **Tags:** #string #math #reverse

#### 📝 Original Statement (English)
**REVERSE Mode**: You do not have access to the statement. You have to guess what to do by observing the following set of tests.

**Test 1**
Input:
```
5
11111
```
Output: `3`

**Test 2**
Input:
```
9
123456789
```
Output: `25`

**Test 3**
Input:
```
6
1a2b3c
```
Output: `6`

**Test 4**
Input:
```
6
a1b2c3
```
Output: `Invalid`

**Test 5**
Input:
```
10
azertyuiop
```
Output: `Invalid`

**Test 6**
Input:
```
28
7s5g0n6g5r1t0b2c8d9f6y5h0g4s
```
Output: `58`

**Test 7**
Input:
```
15
010101010101010
```
Output: `0`

#### 🇯🇵 日本語問題文
**REVERSE モード**: この問題には説明文がありません。テストケースから期待される動作を推論してください。

**推論されたルール:**
与えられた文字列の**1番目、3番目、5番目...（奇数番目）**の文字を抽出します。
- それらがすべて数字である場合、その合計値を出力してください。
- 数字以外の文字が1つでも含まれている場合、`Invalid` と出力してください。
- 偶数番目の文字は任意であり、判定には影響しません。

**入力**
1行目: 文字列の長さ `N`
2行目: 長さ `N` の文字列 `S`

**出力**
奇数番目の数字の合計、または `Invalid`

#### 💡 解説付き解答例

- **Standard (Readable)**:
  `range(0, N, 2)` を使って 0-indexed で 0, 2, 4... 番目の文字をチェックする基本的なループ処理です。
```python
import sys

def solve():
    # 入力を読み込む
    try:
        n = int(sys.stdin.readline().strip())
        s = sys.stdin.readline().strip()
    except:
        return
    
    total = 0
    # 奇数番目（0-indexedでは 0, 2, 4...）をループ
    for i in range(0, n, 2):
        char = s[i]
        if char.isdigit():
            total += int(char)
        else:
            print("Invalid")
            return
            
    print(total)

if __name__ == "__main__":
    solve()
```

- **Advanced (Efficient)**:
  スライス `s[::2]` を使用して奇数番目の文字を一括で抽出し、 `isdigit()` や `sum()` を組み合わせてスマートに処理します。
```python
import sys

def solve():
    line1 = sys.stdin.readline()
    s = sys.stdin.readline().strip()
    if not s: return
    
    # 奇数番目（0, 2, 4...番目）の文字をスライスで取得
    target = s[::2]
    
    # targetがすべて数字かどうかをチェック
    if target.isdigit():
        # 数字であれば整数に変換して合計
        print(sum(int(c) for c in target))
    else:
        # 数字以外が含まれていれば Invalid
        print("Invalid")

if __name__ == "__main__":
    solve()
```

- **Shortest (Golfing)**:
  1行で記述した例です。
```python
input();s=input()[::2];print(sum(map(int,s))if s.isdigit()else"Invalid")
```

#### 🧪 テストケース (Test Cases)
ユーザーが手動で動作確認するためのテストケースです。

| No | Input | Output | Description |
|:---|:---|:---|:---|
| 1 | `5\n11111` | `3` | Test 1 (1+1+1=3) |
| 2 | `6\n1a2b3c` | `6` | Test 3 (1+2+3=6) |
| 3 | `6\na1b2c3` | `Invalid` | Test 4 (先頭が文字) |
| 4 | `28\n7s5g0n6g5r1t0b2c8d9f6y5h0g4s` | `58` | Test 6 (長い文字列) |
| 5 | `11\n0a0b0c0d0e0` | `0` | Test 7に近いケース |

```python
# 以下のコードブロックに自分の回答を書き、上記のテストケースを TEST_INPUT に貼り付けて実行してください。
import sys
from io import StringIO

# --- 🧪 テスト実行用設定 ---
TEST_INPUT = """
6
1a2b3c
"""
sys.stdin = StringIO(TEST_INPUT.strip())
# -----------------------

def solve():
    input()
    s = input()[::2]
    print(sum(map(int, s)) if s.isdigit() else "Invalid")

if __name__ == "__main__":
    solve()
```
