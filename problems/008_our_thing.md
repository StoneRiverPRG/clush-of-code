### [008]: Our thing (共有財産)
- **Difficulty:** Easy
- **Tags:** #string #regex #basic

#### 📝 Original Statement (English)
« If you have an original idea, if it's good, it won't be yours for long. » -- hbomberguy, Plagiarism and You(Tube)

You are provided with a sentence from someone declaring a thing as theirs, by saying **my** (case-insensitive), followed by spaces, then a single-word **thing**.

You must extract the **thing**, then declare shared ownership by presenting it with the following format:

`Our thing.`

You must keep the original casing of the **thing**.

In this context, words are sets of letters from A to Z (case-insensitive). There will never be a case where **my** is followed by something else than a space then a **thing** (which can be **my**!), nor a case where there are more than one thing owned (i.e. no more than one **my**, or two consecutive **my** in the case where **thing** is **my**).

#### 🇯🇵 日本語問題文
誰かが「my [もの]」と言って自分の所有物を宣言している文が与えられます。
あなたはそれを「共有財産」として宣言し直す必要があります。

具体的には、文の中から英字（A〜Z）のみで構成される単語を抽出し、「my」（大文字小文字不問）という単語の直後にある単語（thing）を見つけてください。
そして、その単語の元のケース（大文字・小文字）を維持したまま、以下の形式で出力してください：

`Our thing.`

**注意点:**
- 単語は A から Z（大文字小文字不問）の文字の集まりです。
- 「my」の直後には必ず1つの単語が存在します。
- 文中に「my」は1つしか存在しません。ただし、所有される「もの」自体が「my」である場合は、2つの連続した「my」が存在することになります。

#### 💡 解説付き解答例

- **Standard (Readable)**:
  `re.findall` を使って文中のすべての単語をリスト化し、順番に調べていく最も基本的で分かりやすいアプローチです。
```python
import sys
import re

def solve():
    # 文を読み込む
    sentence = sys.stdin.read().strip()
    if not sentence:
        return
    
    # 英字（A-Z, a-z）の連続を「単語」としてすべて抽出
    words = re.findall(r'[a-zA-Z]+', sentence)
    
    # リストを走査し、"my" が見つかったらその次の単語を取得
    for i in range(len(words) - 1):
        if words[i].lower() == 'my':
            thing = words[i+1]
            print(f"Our {thing}.")
            break

if __name__ == "__main__":
    solve()
```

- **Advanced (Efficient)**:
  `re.search` と正規表現のグループ化、および大文字小文字を無視するフラグ `re.IGNORECASE` を使用した効率的なアプローチです。
```python
import sys
import re

def solve():
    sentence = sys.stdin.read().strip()
    # \bmy\b で単語としての "my" を探し、その後の空白 \s+ と英字グループ ([a-zA-Z]+) をマッチさせる
    match = re.search(r'\bmy\b\s+([a-zA-Z]+)', sentence, re.IGNORECASE)
    if match:
        # グループ1（([a-zA-Z]+)部分）を抽出して出力
        print(f"Our {match.group(1)}.")

if __name__ == "__main__":
    solve()
```

- **Shortest (Golfing)**:
  Pythonのワンライナー記法を用いた最短コード例です。
```python
import re,sys;print(f"Our {re.search('(?i)\\bmy\\s+([a-z]+)',sys.stdin.read())[1]}.")
```

#### 🧪 テストケース (Test Cases)
ユーザーが手動で動作確認するためのテストケースです。

| No | Input | Output | Description |
|:---|:---|:---|:---|
| 1 | `You will find my fridge next to the oven.` | `Our fridge.` | 標準的なケース |
| 2 | `my my` | `Our my.` | 所有物が "my" のケース |
| 3 | `Look at My House.` | `Our House.` | 大文字の "My" |
| 4 | `Is that my phone?` | `Our phone.` | 末尾に記号があるケース |
| 5 | `This is my   car` | `Our car.` | 空白が複数あるケース |

```python
# 以下のコードブロックに自分の回答を書き、上記のテストケースを TEST_INPUT に貼り付けて実行してください。
import sys
from io import StringIO

# --- 🧪 テスト実行用設定 ---
TEST_INPUT = """
You will find my fridge next to the oven.
"""
sys.stdin = StringIO(TEST_INPUT.strip())
# -----------------------

def solve():
    import sys
    import re
    # ここにプログラミングを記述
    sentence = sys.stdin.read().strip()
    match = re.search(r'\bmy\b\s+([a-zA-Z]+)', sentence, re.IGNORECASE)
    if match:
        print(f"Our {match.group(1)}.")

if __name__ == "__main__":
    solve()
```
