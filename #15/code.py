import random


def pick_random(large_stream):
    pick = None

    for i, elem in enumerate(large_stream):
        prob = 1 / (1 + i)
        swap = random.choices([True, False], [prob, 1-prob], k=1)[0]

        if swap:
            pick = elem

    return pick


def test(stream, picks=1000):
    pick_rate = defaultdict(int)

    for _ in range(picks):
        pick_rate[pick_random(stream)] += 1/picks

    return pick_rate


if __name__ == "__main__":
    from collections import defaultdict

    v = [0, 1, 2, 3, 4, 5]
    print(test(v, 100000))
