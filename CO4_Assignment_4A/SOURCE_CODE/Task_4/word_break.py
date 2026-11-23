"""Task 4 - Word Break: faulty version vs corrected version.

Defect: the faulty code sets DP[i] = TRUE when Text[j:i] is a dictionary word,
without checking that the prefix Text[0:j] is itself segmentable (DP[j]).
Fix: add the condition DP[j] = TRUE.
"""


def word_break_faulty(text, dictionary):
    n = len(text)
    DP = [False] * (n + 1)
    DP[0] = True
    for i in range(1, n + 1):
        DP[i] = False
        for j in range(0, i):
            if text[j:i] in dictionary:          # BUG: DP[j] not checked
                DP[i] = True
                break
    return DP[n], DP


def word_break_fixed(text, dictionary):
    n = len(text)
    DP = [False] * (n + 1)
    DP[0] = True
    for i in range(1, n + 1):
        DP[i] = False
        for j in range(0, i):
            if DP[j] and text[j:i] in dictionary:   # FIX: DP[j] AND word match
                DP[i] = True
                break
    return DP[n], DP


def show(title, text, dictionary):
    print(f"--- {title} ---")
    print(f"Text = {text!r}, Dictionary = {sorted(dictionary)}")
    r1, d1 = word_break_faulty(text, dictionary)
    r2, d2 = word_break_fixed(text, dictionary)
    print("Faulty : result =", r1, " DP =", d1)
    print("Fixed  : result =", r2, " DP =", d2)
    print()


if __name__ == "__main__":
    # Task 4.2 failing input
    show("Failing input (faulty gives wrong answer)", "abcd", {"cd"})
    # Another failing input
    show("Second failing input", "catsanddog", {"dog"})
    # Task 4.4 regression input (faulty already correct, fix preserves it)
    show("Regression input", "applepen", {"apple", "pen"})
    show("Regression input 2 (genuinely FALSE)", "xyz", {"a", "b"})
