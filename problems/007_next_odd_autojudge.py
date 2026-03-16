# 🛠 自動判定スクリプト (Judge Script)
import io, sys

def check_solution(func):
    test_cases = [
        ("3\n1\n2\n3", "1\n3\n3"),
        ("2\n0\n-2", "1\n-1"),
        ("2\n-1\n-3", "-1\n-3"),
        ("1\n10000", "10001"),
        ("4\n10\n11\n12\n13", "11\n11\n13\n13"),
        ("5\n2\n4\n6\n8\n10", "3\n5\n7\n9\n11"),
        ("5\n1\n3\n5\n7\n9", "1\n3\n5\n7\n9"),
        ("1\n-10000", "-9999"),
        ("1\n0", "1"),
        ("2\n101\n102", "101\n103"),
        ("3\n-100\n-101\n-102", "-99\n-101\n-101"),
        ("1\n9999", "9999"),
        ("2\n2\n2", "3\n3"),
        ("10\n2\n2\n2\n2\n2\n2\n2\n2\n2\n2", "3\n3\n3\n3\n3\n3\n3\n3\n3\n3"),
        ("3\n100\n0\n-100", "101\n1\n-99"),
    ]
    
    success_count = 0
    for i, (inp, exp) in enumerate(test_cases):
        sys.stdin = io.StringIO(inp)
        sys.stdout = io.StringIO()
        try:
            func()
            result = sys.stdout.getvalue().strip()
            if result == exp.strip():
                success_count += 1
            else:
                print(f"Test case {i+1} failed: expected\n({exp}), got\n({result})", file=sys.stderr)
        except Exception as e:
            print(f"Test case {i+1} raised error: {e}", file=sys.stderr)
        finally:
            sys.stdin = sys.__stdin__
            sys.stdout = sys.__stdout__
            
    print(f"Results for {func.__name__}: {success_count}/{len(test_cases)} passed")

# --- 解答関数パターン ---

def solution_v1():
    import sys
    line = sys.stdin.readline()
    if not line: return
    m = int(line.strip())
    for _ in range(m):
        n = int(sys.stdin.readline().strip())
        if n % 2 == 0:
            print(n + 1)
        else:
            print(n)

def solution_v2():
    import sys
    data = sys.stdin.read().split()
    if not data: return
    m = int(data[0])
    for i in range(1, m + 1):
        print(int(data[i]) | 1)

# --- ユーザー回答パターン ---
def user_solution():
    pass

# --- 実行 ---
if __name__ == "__main__":
    check_solution(solution_v1)
    check_solution(solution_v2)
