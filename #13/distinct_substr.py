def distinct_substr_trivial(s: str, k: int):
    max_subs = ""

    for i in range(len(s)):
        count = 0
        pos = i

        while pos < len(s) and count <= k:
            if s[pos] not in s[i:pos]:
                count = count + 1
            pos = pos + 1

        if len(s[i:pos-1]) > len(max_subs):
            max_subs = s[i:pos-1]

    return max_subs


if __name__ == "__main__":
    ans = distinct_substr_trivial("abcba", 2)
    print(ans, len(ans))
