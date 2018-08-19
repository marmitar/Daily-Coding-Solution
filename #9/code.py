import unittest
import random
import time


def n_adj_sum_trivial(int_list):
    """Quadratic solution"""
    max_sum = int_list[0] + int_list[2]

    for i in range(len(int_list)):
        for j in range(i+2, len(int_list)):
            if int_list[i] + int_list[j] > max_sum:
                max_sum = int_list[i] + int_list[j]

    return max_sum


def n_adj_sum_fast(int_list):
    """Linear solution"""
    top_three = [None] * 3
    for i in range(len(int_list)):
        for j in range(3):
            if top_three[j] is None or int_list[i] > int_list[top_three[j]]:
                top_three.insert(j, i)
                top_three.pop()
                break

    if abs(top_three[0] - top_three[1]) > 1:
        return int_list[top_three[0]] + int_list[top_three[1]]

    elif abs(top_three[0] - top_three[2]) > 1:
        return int_list[top_three[0]] + int_list[top_three[2]]

    else:
        return int_list[top_three[1]] + int_list[top_three[2]]


def n_adj_sum(int_list, mode="trivial"):
    """Find the largest sum of two non-adjacent number in list"""
    if len(int_list) < 3:
        raise ValueError("List too small")

    if mode == "trivial":
        return n_adj_sum_trivial(int_list)

    else:
        return n_adj_sum_fast(int_list)


class CodeTest(unittest.TestCase):
    known_solutions = [
        ([1, 2, 3, 4, 5, 6], 10),
        ([5, 1, 1, 5], 10),
        ([2, 4, 6, 8], 12),
        ([1, 1, 1], 2),
        ([10, 30, 20], 30),
        ([-1, -2, -3, -4], -4)
    ]

    type_errors = [1, -1, 1j, .1]
    value_errors = [[], (), [0], (1, 2), [1, 2]]

    def test_trivial(self):
        """Test for 'n_adj_sum' trivial solution"""
        for num_list, solution in self.known_solutions:
            self.assertEqual(solution, n_adj_sum(num_list, "trivial"))

    def test_fast(self):
        """Test for 'n_adj_sum' linear solution"""
        for num_list, solution in self.known_solutions:
            self.assertEqual(solution, n_adj_sum(num_list, "fast"))

    def test_error(self):
        """Test for expected exceptions"""
        for wrong_input in self.type_errors:
            self.assertRaises(TypeError,
                              n_adj_sum, wrong_input, mode="trivial")
            self.assertRaises(TypeError,
                              n_adj_sum, wrong_input, mode="fast")

        for wrong_input in self.value_errors:
            self.assertRaises(ValueError,
                              n_adj_sum, wrong_input, mode="trivial")
            self.assertRaises(ValueError,
                              n_adj_sum, wrong_input, mode="fast")


def speed_test(size, mode):
    test_list = random.sample(range(size), size)

    start = time.time_ns()
    n_adj_sum(test_list, mode=mode)
    stop = time.time_ns()

    return stop - start


if __name__ == "__main__":
    trivial, fast = 0, 0

    for _ in range(100):
            for i in [100, 1000]:
                trivial = trivial + speed_test(i, "trivial")
                fast = fast + speed_test(i, "fast")

    print("Trivial: {:.2f}s".format(trivial / 10**9))
    print("Fast: {:.2f}s".format(fast / 10**9))
