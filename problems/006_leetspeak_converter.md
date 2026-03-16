### 006: Leetspeak Converter (母音の置換)
- **Difficulty:** Easy
- **Tags:** #string #replace #leet

#### 📝 Original Statement (English)
Leet (or "1337") is a system of modified spellings used primarily on the Internet. In this task, you need to create a simple converter that replaces specific lowercase vowels with numbers.

**Rules:**
- `a` -> `4`
- `e` -> `3`
- `i` -> `1`
- `o` -> `0`

**Input:**
- A single line of string `S`.

**Output:**
- The converted string.

#### 🇯🇵 日本語問題文
「Leetspeak（リートスピーク）」とは、インターネット上で使われる、文字を似た形の数字や記号に置き換える表記法です。この問題では、入力された文字列に含まれる特定の小母音を、以下のルールに従って数字に置換してください。

**置換ルール:**
- `a` を `4` に置換
- `e` を `3` に置換
- `i` を `1` に置換
- `o` を `0` に置換

**入力:**
- 1行の文字列 `S` が与えられます。

**出力:**
- 置換後の文字列を出力してください。

#### 💡 解説付き解答例
- **Standard (Readable)**:
```python
import sys

# 文字列を読み込む
s = input()

# replace() をチェイン（連続）させて置換を行う
# 文字列はイミュータブル（不変）なので、結果を新しい変数に入れるか、上書きする
result = s.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0')

print(result)
```
Pythonの `str.replace(old, new)` メソッドを使用する最も基本的な方法です。1つずつ順番に置換を適用していきます。

- **Advanced (Efficient)**:
```python
# str.maketrans と translate を使うと、複数の文字を一気に置換できる
s = input()
table = str.maketrans("aeio", "4310")
print(s.translate(table))
```
多くの文字を一度に置換したい場合、`str.translate()` と `str.maketrans()` を使うのが効率的で、コードもスッキリします。

- **Shortest (Golfing)**:
```python
print(input().translate(str.maketrans("aeio","4310")))
```
`translate` を使った最短記述です。

#### 🧪 テストケース (Test Cases)
ユーザーが手動で動作確認するためのテストケースです。

| No | Input | Output | Description |
|:---|:---|:---|:---|
| 1 | `apple` | `4ppl3` | aとeが置換される |
| 2 | `hello world` | `h3ll0 w0rld` | eとoが置換される |
| 3 | `python programming` | `pyth0n pr0gr4mm1ng` | o, a, iが置換される |
| 4 | `aeio` | `4310` | すべての対象文字が含まれる |
| 5 | `xyz` | `xyz` | 置換対象がない場合はそのまま |

```python
# 以下のコードブロックに自分の回答を書き、上記のテストケースを TEST_INPUT に貼り付けて実行してください。
import sys
from io import StringIO

# --- 🧪 テスト実行用設定 ---
TEST_INPUT = """
apple
"""
sys.stdin = StringIO(TEST_INPUT.strip())
# -----------------------

def solve():
    # 競技プログラミング形式（input() など）でそのまま記述できます
    import sys
    
    # ここにプログラミングを記述
    # 例: print(input().replace('a', '4')...)
    pass

if __name__ == "__main__":
    solve()
```
