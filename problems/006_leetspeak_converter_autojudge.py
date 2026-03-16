# 🛠 自動判定スクリプト (Judge Script)
import io, sys

def check_solution(func):
    test_cases = [
        ("apple", "4ppl3"),
        ("hello world", "h3ll0 w0rld"),
        ("python programming", "pyth0n pr0gr4mm1ng"),
        ("aeio", "4310"),
        ("xyz", "xyz"),
        ("The quick brown fox jumps over the lazy dog", "Th3 qu1ck br0wn f0x jumps 0v3r th3 l4zy d0g"),
        ("12345", "12345"),
        ("A E I O", "A E I O"), # lowercase only
        ("aaaaa", "44444"),
        ("eeeee", "33333"),
        ("iiiii", "11111"),
        ("ooooo", "00000"),
        ("aeioaeio", "43104310"),
        ("", ""),
        ("beat", "b34t"),
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
        s = sys.stdin.read().strip('\n')
        if not s and not sys.stdin.isatty(): # Handle empty input for non-interactive
             # Special case for empty test input if read() is used
             pass
        print(s.replace('a','4').replace('e','3').replace('i','1').replace('o','0'))
    except EOFError:
        pass

def solution_v2():
    import sys
    s = sys.stdin.read().strip('\n')
    print(s.translate(str.maketrans("aeio", "4310")))

# --- ユーザー回答パターン ---
def user_solution():
    # ここに回答をコピーしてテストできます
    pass

# --- 実行 ---
if __name__ == "__main__":
    check_solution(solution_v1)
    check_solution(solution_v2)
