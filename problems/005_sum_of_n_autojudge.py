# 🛠 自動判定スクリプト (Judge Script)
import io, sys

def check_solution(func):
    test_cases = [
        ("3\n1\n2\n3", "6"),
        ("5\n1\n2\n1\n10\n0", "14"),
        ("2\n5\n2", "7"),
        ("1\n8", "8"),
        ("4\n42\n0\n1337\n666", "2045"),
        ("0", "0"),
        ("10\n1\n1\n1\n1\n1\n1\n1\n1\n1\n1", "10"),
        ("3\n-1\n-2\n-3", "-6"),
        ("2\n100\n-100", "0"),
        ("5\n0\n0\n0\n0\n0", "0"),
        ("1\n0", "0"),
        ("2\n1000000000\n1000000000", "2000000000"),
        ("3\n10\n20\n30", "60"),
        ("4\n1\n2\n4\n8", "15"),
        ("2\n999\n1", "1000"),
    ]
    
    success_count = 0
    for i, (inp, exp) in enumerate(test_cases):
        sys.stdin = io.StringIO(inp)
        sys.stdout = io.StringIO()
        try:
            func()
            result = sys.stdout.getvalue().strip()
            if result == exp:
                success_count += 1
            else:
                print(f"Test case {i+1} failed: expected {exp}, got {result}", file=sys.stderr)
        except Exception as e:
            print(f"Test case {i+1} raised error: {e}", file=sys.stderr)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
            
    print(f"Results for {func.__name__}: {success_count}/{len(test_cases)} passed")

# --- 解答関数パターン ---

def solution_v1():
    import sys
    try:
        line = sys.stdin.readline()
        if not line: return
        n = int(line.strip())
        total = 0
        for _ in range(n):
            total += int(sys.stdin.readline().strip())
        print(total)
    except (EOFError, ValueError):
        pass

def solution_v2():
    import sys
    try:
        data = sys.stdin.read().split()
        if not data: return
        n = int(data[0])
        nums = map(int, data[1:])
        print(sum(nums))
    except (EOFError, ValueError, IndexError):
        pass

def solution_v3():
    import sys
    try:
        input_data = sys.stdin.read().split()
        if len(input_data) > 0:
            print(sum(map(int, input_data[1:])))
    except:
        pass

# --- ユーザー回答パターン ---
def user_solution():
    # ここに回答をコピーしてテストできます
    pass

# --- 実行 ---
if __name__ == "__main__":
    check_solution(solution_v1)
    check_solution(solution_v2)
    check_solution(solution_v3)
    # check_solution(user_solution)
