from distinct_substr import distinct_substr_trivial as trivial
from dist_substr import distinct_substr_opt as fast

import random
import string
import time


def gens(l, r):
    lenght = random.randint(l, r)
    letters = random.choices(string.ascii_lowercase, k=lenght)
    return ''.join(letters)

def test(limits=(10, 100), k=10):
    s = gens(*limits)

    t0 = time.time()
    t = trivial(s, k)
    t1 = time.time()
    f = fast(s, k)
    t2 = time.time()

    if len(set(t)) != len(set(f)) or len(set(t)) > k:
        raise ValueError(f"Problem with {s}: t'{t}' != f'{f}'")

    return t1-t0, t2-t1

def speedtest(tests=1000, limits=(10, 100), ks=(2, 10)):
    triv, opt = 0.0, 0.0

    for _ in range(tests):
        for k in range(*ks):
            t, f = test(limits, k)
            triv += t
            opt += f
    return t, f


if __name__ == "__main__":
    t, f = speedtest(tests=100, limits=(100, 1000), ks=(2, 50, 8))
    print(f"triv: {t:.6f} s")
    print(f"fast: {f:.6f} s")
