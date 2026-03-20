# 🛠 自動判定スクリプト (Judge Script)
import io
import sys

def check_solution(func):
    # テストケース定義
    test_cases = [
        ("5\n2 4 8 10 6", "30"),
        ("3\n2 3 4", "10"),
        ("2\n3 5", "0"),
        ("4\n1 2 3 4", "10"),
        ("1\n7", "0"),
        ("1\n8", "8"),
        ("4\n2 -1 4 -3", "-6"),
        ("3\n0 5 0", "0"),
        ("2\n10 0", "10"),
        ("10\n1 1 1 1 1 1 1 1 1 2", "2"),
        ("5\n2 2 1 2 2", "8"),
        ("2\n1000 -1", "-1000"),
        ("3\n4 5 -2", "18"),
        ("2\n1 0", "0"),
        ("1\n-10000", "-10000"),
    ]

    print(f"\n--- Testing Function: {func.__name__} ---")
    passed = 0
    for i, (input_data, expected_output) in enumerate(test_cases, 1):
        sys.stdin = io.StringIO(input_data)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        try:
            func()
            actual_output = sys.stdout.getvalue().strip()
        except Exception as e:
            actual_output = f"Error: {e}"
        finally:
            sys.stdout = old_stdout
            
        if actual_output == expected_output:
            print(f"Test case {i:02}: [OK] PASSED")
            passed += 1
        else:
            print(f"Test case {i:02}: [FAIL] FAILED")
            print(f"   Input:    {input_data.replace('\\n', ' ')}")
            print(f"   Expected: {expected_output}")
            print(f"   Actual:   {actual_output}")

    print(f"Result: {passed}/{len(test_cases)} cases passed.")

# --- 解答パターン ---

def solution_v1_readable():
    """Standard (Readable)"""
    import sys
    data = sys.stdin.read().split()
    if not data: return
    it = iter(map(int, data[1:]))
    r = 0
    for x in it:
        if x % 2: r *= x
        else: r += x
    print(r)

def solution_v2_efficient():
    """Advanced (Efficient)"""
    from functools import reduce
    data = sys.stdin.read().split()
    if len(data) < 2: return
    print(reduce(lambda r, x: r * x if x % 2 else r + x, map(int, data[1:]), 0))

def solution_v3_shortest():
    """Shortest (Golfing)"""
    import sys;r=0;d=sys.stdin.read().split();[r:=r*int(x)if int(x)%2 else r+int(x)for x in d[1:]];print(r)

# --- 実行 ---
if __name__ == "__main__":
    check_solution(solution_v1_readable)
    check_solution(solution_v2_efficient)
    check_solution(solution_v3_shortest)
