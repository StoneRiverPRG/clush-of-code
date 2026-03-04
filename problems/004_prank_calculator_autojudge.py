# 🛠 自動判定スクリプト (Judge Script)
import io, sys

def check_solution(func):
    # テストケース定義
    # (入力文字列, 期待される出力文字列)
    test_cases: list[tuple[str, str]] = [
        ("10\n+\n3\n", "7\n"),
        ("5\n-\n4\n", "20\n"),
        ("10\n*\n3\n", "3\n"),
        ("-10\n*\n3\n", "-3\n"),
        ("20\n/\n5\n", "25\n")
    ]
    
    passed = 0
    for i, (input_data, expected) in enumerate(test_cases, 1):
        # 標準入力のモック
        sys.stdin = io.StringIO(input_data)
        # 標準出力のキャプチャ
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            func()
        except Exception as e:
            print(f"Test Case {i}: Error - {e}", file=sys.__stdout__)
            continue
        finally:
            # 標準入力・出力を元に戻す
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
            
        output = captured_output.getvalue()
        if output == expected:
            print(f"Test Case {i}: PASSED")
            passed += 1
        else:
            print(f"Test Case {i}: FAILED")
            print(f"  Input: {repr(input_data)}")
            print(f"  Expected: {repr(expected)}")
            print(f"  Got: {repr(output)}")
            
    print(f"Result: {passed}/{len(test_cases)} passed.\n")

# 各解答関数の定義と実行
def solution_v1():
    try:
        a = int(input())
        op = input()
        b = int(input())
        
        if op == '+': print(a - b)
        elif op == '-': print(a * b)
        elif op == '*': print(int(a / b))
        elif op == '/': print(a + b)
    except EOFError:
        pass

def solution_v2():
    lines = sys.stdin.read().split()
    if not lines: return
    a, op, b = int(lines[0]), lines[1], int(lines[2])
    operations = {
        '+': lambda x, y: x - y,
        '-': lambda x, y: x * y,
        '*': lambda x, y: int(x / y),
        '/': lambda x, y: x + y
    }
    print(operations[op](a, b))

def solution_v3():
    lines = sys.stdin.read().split()
    if len(lines) < 3: return
    a, o, b = lines[0], lines[1], lines[2]
    a, b = int(a), int(b)
    print({"+":a-b,"-":a*b,"*":int(a/b) if b else 0,"/":a+b}[o])

# --- ユーザー回答パターン ---
# ここにユーザーが実装した解答を追加してください
def user_solution():
    pass

# --- 実行 ---
if __name__ == '__main__':
    print("=== Testing solution_v1 (Standard) ===")
    check_solution(solution_v1)
    
    print("=== Testing solution_v2 (Advanced) ===")
    check_solution(solution_v2)
    
    print("=== Testing solution_v3 (Shortest) ===")
    check_solution(solution_v3)
    
    # print("=== Testing user_solution ===")
    # check_solution(user_solution)
