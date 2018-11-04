from collections import defaultdict


def cnt_inc(counter, letter):
    if counter[letter] == 0:
        counter["space"] -= 1
    counter[letter] += 1

def cnt_dec(counter, letter):
    counter[letter] -= 1
    if counter[letter] == 0:
        counter["space"] += 1


def distinct_substr_opt(s: str, k: int):
    count = defaultdict(lambda: 0)
    count["space"] = k

    max_init, max_len = 0, 0
    init, lenght = 0, max_len

    for letter in s:
        cnt_inc(count, letter)
        lenght += 1

        if count["space"] < 0:
            if lenght-1 > max_len:
                max_init, max_len = init, lenght-1

            while count["space"] < 0:
                cnt_dec(count, s[init])
                init += 1
                lenght -= 1

    if lenght-1 > max_len:
        max_init, max_len = init, lenght-1


    return s[max_init:max_init+max_len]


if __name__ == "__main__":
    # ans = distinct_substr_opt("abcba", 2)
    ans = distinct_substr_opt("cmzomiq", 2)
    print(ans, len(ans))
