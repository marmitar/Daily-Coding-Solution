from random import SystemRandom
from time import clock
from matplotlib import pyplot

class Existance(dict):
    def __missing__(self, key):
        self[key] = False


def can_sum(nums, k):

    exist = Existance()

    for i in range(len(nums)):
        if exist[k - nums[i]]:
            return i

        exist[nums[i]] = True

    return -1


if __name__ == "__main__":
    rng = SystemRandom()
    def randnum():
        return rng.randrange(100, 1000000)
    def randkey():
        return rng.randrange(200, 1500000)
    def randarr(size):
        return [randnum() for _ in range(size)]

    sizes = [2, 10, 100, 1000, 10000, 100000, 1000000]
    times = []
    anss = []
    repeat = 100

    for size in sizes:
        timearr = []
        ansarr = []

        for _ in range(repeat):
            array = randarr(size)
            key = randkey()

            init = clock()
            ans = can_sum(array, key)
            timearr.append(clock()-init)
            ansarr.append((ans / size) if ans >= 0 else 1)

        times.append(timearr)
        anss.append(ansarr)

    pyplot.figure(1)
    
    pyplot.subplot(211)
    pyplot.semilogx(sizes, times, 'b--')
    pyplot.title("Time")

    pyplot.subplot(212)
    pyplot.semilogx(sizes, anss, 'r^')
    pyplot.title("Ans")

    pyplot.show()
