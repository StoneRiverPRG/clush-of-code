import io
import sys

def check_solution(func):
    """
    関数を受け取り、複数のテストケースで検証する関数
    """
    test_cases = [
        {
            "input": "2 2\n2 8\n4 3",
            "expected": "2",
            "desc": "基本ケース (2x2)"
        },
        {
            "input": "3 3\n2 4 7\n8 3 1\n1 0 8",
            "expected": "10",
            "desc": "例題ケース (3x3)"
        },
        {
            "input": "2 2\n1 1\n1 1",
            "expected": "0",
            "desc": "偶数が存在しないケース"
        }
    ]

    print(f"--- Checking: {func.__name__} ---")
    passed = 0
    for i, tc in enumerate(test_cases):
        # 標準入力をシミュレート
        sys.stdin = io.StringIO(tc["input"])
        # 出力をキャプチャ
        actual_output = io.StringIO()
        sys.stdout = actual_output

        try:
            func()
            result = actual_output.getvalue().strip()
            if result == tc["expected"]:
                print(f"✅ Case {i+1} PASSED ({tc['desc']})")
                passed += 1
            else:
                print(f"❌ Case {i+1} FAILED! Expected {tc['expected']}, got {result}")
        except Exception as e:
            print(f"💥 Case {i+1} ERROR: {e}")
        finally:
            sys.stdout = sys.__stdout__ # 出力を元に戻す

    print(f"Result: {passed}/{len(test_cases)}\n")

# --- 解答例パターン1: 全探索 ---
def solution_v1():
    h, w = map(int, sys.stdin.readline().split())
    total = 0
    for i in range(h):
        row = list(map(int, sys.stdin.readline().split()))
        if i % 2 == 0: # 行が偶数
            for j in range(w):
                if j % 2 == 0 and row[j] % 2 == 0: # 列が偶数 かつ 値が偶数
                    total += row[j]
    print(total)

# --- 解答例パターン2: スライス活用 ---
def solution_v2():
    h, w = map(int, sys.stdin.readline().split())
    total = 0
    for i in range(h):
        line = sys.stdin.readline()
        if i % 2 == 0:
            row = list(map(int, line.split()))
            # インデックス 0, 2, 4... の要素だけを合計
            total += sum(v for v in row[::2] if v % 2 == 0)
    print(total)

# --- 解答例パターン3: One-liner (Golfing) ---
def solution_v3():
    # 最初の行でHを取得し、残りの行から偶数行(0,2,..)だけ抽出し、その中の偶数列かつ偶数値を合計
    h, _ = map(int, sys.stdin.readline().split())
    print(sum(sum(int(v) for v in l.split()[::2] if int(v)%2==0) for i, l in enumerate(sys.stdin) if i < h and i%2==0))

# --- ユーザー回答パターン ---
# ここにユーザーが実装した解答を追加してください
def user_solution():
    pass


# --- 実行 ---
check_solution(solution_v1)
check_solution(solution_v2)
check_solution(solution_v3)
check_solution(user_solution)
