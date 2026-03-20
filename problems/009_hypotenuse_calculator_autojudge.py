# 🛠 自動判定スクリプト (Judge Script)
import io
import sys
import math

def check_solution(func):
    # テストケース定義
    test_cases = [
        ("2\n3", "4"),
        ("3\n4", "5"),
        ("5\n12", "13"),
        ("8\n15", "17"),
        ("7\n24", "25"),
        ("1\n1", "1"),
        ("25\n25", "35"),
        ("1\n2", "2"),
        ("9\n12", "15"),
        ("10\n10", "14"),
        ("15\n20", "25"),
        ("1\n10", "10"),
        ("2\n2", "3"),
        ("11\n23", "25"),
        ("20\n21", "29"),
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
    import math
    input_data = sys.stdin.read().split()
    if not input_data: return
    a, b = map(int, input_data)
    print(round(math.sqrt(a*a + b*b)))

def solution_v2_efficient():
    """Advanced (Efficient)"""
    import math
    nums = list(map(int, sys.stdin.read().split()))
    if len(nums) >= 2:
        print(round(math.hypot(*nums[:2])))

def solution_v3_shortest():
    """Shortest (Golfing)"""
    import math,sys;print(round(math.hypot(*map(int,sys.stdin.read().split()))))

# --- 実行 ---
if __name__ == "__main__":
    check_solution(solution_v1_readable)
    check_solution(solution_v2_efficient)
    check_solution(solution_v3_shortest)
