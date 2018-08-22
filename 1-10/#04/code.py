def lowest_missing_quadratic(array):

    ans = 1

    for i in range(len(array)):
        if array[i] == ans:
            ans += 1

            i = 0

    return ans

def lowest_missing_sorting(array):
    array_s = sorted(array)

    low = 1
    for val in array_s:
        if val == low:
            low += 1
        elif val > low:
            return low

    return low

# from GeeksforGeeks
def lowest_missing_linear(array):

    indexes = [True] * len(array)

    for i in range(len(array)):
        if array[i] > 0 and array[i] <= len(array):
            indexes[array[i] - 1] = False

    for i in range(len(indexes)):
        if indexes[i] is True:
            return i + 1

    return len(indexes) + 1


if __name__ == "__main__":

    array = [1, 2, 3]

    print(lowest_missing_linear(array))
