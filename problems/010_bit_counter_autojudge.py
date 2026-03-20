# 🛠 自動判定スクリプト (Judge Script)
import io
import sys

def check_solution(func):
    # テストケース定義
    test_cases = [
        ("00101110", "8"),
        ("00000000", "0"),
        ("11111111", "16"),
        ("10101010", "8"),
        ("01010101", "8"),
        ("11001100", "8"),
        ("11110000", "8"),
        ("00001111", "8"),
        ("10000000", "2"),
        ("00000001", "2"),
        ("11100111", "12"),
        ("10110111", "12"),
        ("00011000", "4"),
        ("11011011", "12"),
        ("01111110", "12"),
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
            print(f"   Input:    {input_data}")
            print(f"   Expected: {expected_output}")
            print(f"   Actual:   {actual_output}")

    print(f"Result: {passed}/{len(test_cases)} cases passed.")

# --- 解答パターン ---

def solution_v1_readable():
    """Standard (Readable)"""
    line = sys.stdin.read().strip()
    if line:
        print(line.count('1') * 2)

def solution_v2_efficient():
    """Advanced (Efficient)"""
    line = sys.stdin.read().strip()
    if line:
        # bit_count() is available in Python 3.10+
        n = int(line, 2)
        print(n.bit_count() * 2)

def solution_v3_shortest():
    """Shortest (Golfing)"""
    print(sys.stdin.read().strip().count('1')*2)

# --- 実行 ---
if __name__ == "__main__":
    check_solution(solution_v1_readable)
    check_solution(solution_v2_efficient)
    check_solution(solution_v3_shortest)
