### 004: Prank Calculator
- **Difficulty:** Easy
- **Tags:** #math #if #演算子

#### 📝 Original Statement (English)
> Goal
> A prankster colleague has reprogrammed your calculator to make it lose its mind! The basic mathematical operators no longer do what they are supposed to do. Here are the new rules:
> 
> - The + operator performs subtraction.
> - The - operator performs multiplication.
> - The * operator performs integer division (keep only the integer part, truncation towards zero).
> - The / operator performs addition.
> 
> Your mission is to write a program that takes two numbers and an operator, and displays the result according to this "pranked" logic.
> 
> Input
> Line 1: An integer A for the first operand.
> Line 2: A character op among +, -, *, / for the original operator.
> Line 3: An integer B for the second operand.
> 
> Output
> Line 1: A single integer: the result of the modified operation.
> 
> Constraints
> -10000 ≤ A, B ≤ 10000
> B will never be 0 when the operator displayed is * (since this corresponds to division).
> 
> Example
> Input
> 10
> +
> 3
> Output
> 7

#### 🇯🇵 日本語問題文
**目標**
いたずら好きな同僚があなたの電卓をハッキングし、動作をおかしくしてしまいました！ 基本的な四則演算子が本来の動作をしなくなっています。新しいルールは以下の通りです：

- `+` 演算子は **引き算（減算）** を行います。
- `-` 演算子は **掛け算（乗算）** を行います。
- `*` 演算子は **整数割り算（除算・小数点以下切り捨て）** を行います。
- `/` 演算子は **足し算（加算）** を行います。

あなたの任務は、2つの数字と演算子を受け取り、この「いたずらされた電卓」のロジックに従って結果を出力するプログラムを書くことです。

**入力**
1行目: 1つ目のオペランド（整数 A）
2行目: 元の演算子（`+`, `-`, `*`, `/` のいずれか1文字 `op`）
3行目: 2つ目のオペランド（整数 B）

**出力**
1行目: 変更された演算ロジックに従った計算結果の一つの整数

**制約**
-10000 ≤ A, B ≤ 10000
入力される演算子が `*`（実際の計算は割り算）のとき、Bが0になることはありません。

**例**
入力:
```
10
+
3
```
出力:
```
7
```

#### 💡 解説付き解答例
- **Standard (Readable)**:
```python
import sys

def solve():
    # 入力を受け取る
    a = int(input())
    op = input()
    b = int(input())
    
    # 演算子に応じて計算を行う
    if op == '+':
        print(a - b)  # + は引き算
    elif op == '-':
        print(a * b)  # - は掛け算
    elif op == '*':
        # * は整数割り算。Pythonの // は切り捨てだが、負の数の切り捨て方向（負の無限大方向・床関数）
        # に注意が必要。「ゼロ方向への切り捨て」を行う場合は float の割り算をして int() でキャストするのが安全です。
        print(int(a / b))
    elif op == '/':
        print(a + b)  # / は足し算

if __name__ == '__main__':
    solve()
```
*解説*: 初心者にとって分かりやすい素直な `if-elif` 構成の分岐処理です。注意点として、Pythonの `//` は `-1 // 3 == -1` のように負の無限大方向に丸められるため、問題文の「ゼロ方向に切り捨て (truncation towards zero)」を行う場合は `int(a / b)` とするのが正確です。

- **Advanced (Efficient)**:
```python
import sys

def solve():
    # 入力をすべて読み込む
    lines = sys.stdin.read().split()
    if not lines: return
    a, op, b = int(lines[0]), lines[1], int(lines[2])
    
    # 演算子とラムダ関数（匿名関数）の辞書を作成
    operations = {
        '+': lambda x, y: x - y,
        '-': lambda x, y: x * y,
        '*': lambda x, y: int(x / y),
        '/': lambda x, y: x + y
    }
    
    # 辞書から対応する関数を取得して実行
    result = operations[op](a, b)
    print(result)

if __name__ == '__main__':
    solve()
```
*解説*: 分岐処理を `dict`（辞書）と `lambda` 式（無名関数）の組み合わせでシンプルに実装した例です。大量の分岐がある場合、このように関数を辞書でマッピングする事でコードの見通しが良くなり、保守性も上がります。

- **Shortest (Golfing)**:
```python
a,o,b=open(0).read().split();a,b=int(a),int(b);print({"+":a-b,"-":a*b,"*":int(a/b if b else 0),"/":a+b}[o])
```
*解説*: `open(0).read().split()` で標準入力から一括で読み込み、辞書を用いて1行に収めたコードです。競技プログラミングのショートコーディング（Golfing）で頻繁に利用されるハックです。
