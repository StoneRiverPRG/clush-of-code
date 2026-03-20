# 🛠 自動判定スクリプト (Judge Script)
import io
import sys

def check_solution(func):
    # テストケース定義
    test_cases = [
        ("5\n11111", "3"),
        ("9\n123456789", "25"),
        ("6\n1a2b3c", "6"),
        ("6\na1b2c3", "Invalid"),
        ("10\nazertyuiop", "Invalid"),
        ("28\n7s5g0n6g5r1t0b2c8d9f6y5h0g4s", "58"),
        ("15\n010101010101010", "0"),
        ("1\n5", "5"),
        ("1\nA", "Invalid"),
        ("2\n2B", "2"),
        ("2\nB2", "Invalid"),
        ("3\n1!2", "3"),
        ("4\n1234", "4"),
        ("5\n9-8-7", "24"),
        ("11\n0a0b0c0d0e0", "0"),
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
    line1 = sys.stdin.readline()
    if not line1: return
    n = int(line1.strip())
    s = sys.stdin.readline().strip()
    total = 0
    for i in range(0, n, 2):
        if s[i].isdigit():
            total += int(s[i])
        else:
            print("Invalid")
            return
    print(total)

def solution_v2_efficient():
    """Advanced (Efficient)"""
    import sys
    sys.stdin.readline() # ignore n
    s = sys.stdin.readline().strip()
    if not s: return
    target = s[::2]
    if target.isdigit():
        print(sum(int(c) for c in target))
    else:
        print("Invalid")

def solution_v3_shortest():
    """Shortest (Golfing)"""
    import sys;input();s=sys.stdin.read().strip()[::2];print(sum(map(int,s))if s.isdigit()else"Invalid")

# --- 実行 ---
if __name__ == "__main__":
    check_solution(solution_v1_readable)
    check_solution(solution_v2_efficient)
    check_solution(solution_v3_shortest)
