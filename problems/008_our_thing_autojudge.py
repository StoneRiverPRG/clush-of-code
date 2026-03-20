# 🛠 自動判定スクリプト (Judge Script)
import io
import sys
import re

def check_solution(func):
    # テストケース定義
    test_cases = [
        ("You will find my fridge next to the oven.", "Our fridge."),
        ("my my", "Our my."),
        ("Look at My House.", "Our House."),
        ("Is that my phone?", "Our phone."),
        ("This is my   car", "Our car."),
        ("MY computer IS broken.", "Our computer."),
        ("give me my Apple!", "Our Apple."),
        ("my X", "Our X."),
        ("the word is my word.", "Our word."),
        ("Tell me, is this my Secret?", "Our Secret."),
        ("This is My   Room.", "Our Room."),
        ("Where is My bag?", "Our bag."),
        ("I lost my Keys.", "Our Keys."),
        ("Found my Wallet!", "Our Wallet."),
        ("No, it is my Pencil.", "Our Pencil."),
    ]

    print(f"\n--- Testing Function: {func.__name__} ---")
    passed = 0
    for i, (input_data, expected_output) in enumerate(test_cases, 1):
        # sys.stdin をモック
        sys.stdin = io.StringIO(input_data)
        # stdout をキャプチャ
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
    sentence = sys.stdin.read().strip()
    if not sentence: return
    words = re.findall(r'[a-zA-Z]+', sentence)
    for i in range(len(words) - 1):
        if words[i].lower() == 'my':
            print(f"Our {words[i+1]}.")
            break

def solution_v2_efficient():
    """Advanced (Efficient)"""
    sentence = sys.stdin.read().strip()
    match = re.search(r'\bmy\b\s+([a-zA-Z]+)', sentence, re.IGNORECASE)
    if match:
        print(f"Our {match.group(1)}.")

def solution_v3_shortest():
    """Shortest (Golfing)"""
    # 実際の問題では1行で書くことが想定されます
    import re,sys;print(f"Our {re.search('(?i)\\bmy\\s+([a-z]+)',sys.stdin.read())[1]}.")

# --- 実行 ---
if __name__ == "__main__":
    check_solution(solution_v1_readable)
    check_solution(solution_v2_efficient)
    check_solution(solution_v3_shortest)
