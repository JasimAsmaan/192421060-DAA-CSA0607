"""Compare fixed algorithm with an independent recursive reference."""
import random
from functools import lru_cache
from word_break import word_break_faulty, word_break_fixed


def reference(text, words):
    @lru_cache(None)
    def go(i):
        return i == len(text) or any(text.startswith(w, i) and go(i + len(w)) for w in words)
    return go(0)


random.seed(11)
wrong_faulty = 0
for t in range(1000):
    text = "".join(random.choice("ab") for _ in range(random.randint(1, 8)))
    words = {"".join(random.choice("ab") for _ in range(random.randint(1, 3))) for _ in range(3)}
    ref = reference(text, frozenset(words))
    assert word_break_fixed(text, words)[0] == ref, (text, words)
    wrong_faulty += word_break_faulty(text, words)[0] != ref
print("PASS: fixed algorithm == reference on 1000 random cases")
print(f"Faulty algorithm was wrong on {wrong_faulty} of the same 1000 cases")
