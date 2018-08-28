from opt_query import Query as FastQuery
from query import Query as SlowQuery


def example(mode="fast"):
    autocomplete = FastQuery() if mode == "fast" else SlowQuery()

    autocomplete.insert(["dog", "deer", "deal"])
    print(autocomplete['de'])


def time_insertion(mode):
    import time

    autocomplete = FastQuery() if mode == "fast" else SlowQuery()
    measurement = float("NaN")

    with open("words.txt", "rt") as text:
        start = time.time()

        for word in text:
            autocomplete.insert(word.strip())

        end = time.time()
        measurement = end - start

    return autocomplete, measurement


def time_queries(autocomplete):
    import time
    import string

    start = time.time()

    for letter in string.ascii_lowercase:
        autocomplete[letter]

    end = time.time()
    return end - start


def print_times(mode, insertion, query, queries=26):
    print(mode, 'Query:')
    print('\t', 'Insertion: ', insertion, 's')
    print('\t', queries, 'queries:', query, 's')
    print()


def speed_test():
    fastcomplete, fast_insert = time_insertion("fast")
    slowcomplete, slow_insert = time_insertion("slow")

    fast_queries = time_queries(fastcomplete)
    slow_queries = time_queries(slowcomplete)

    print_times("Fast", fast_insert, fast_queries)
    print_times("Slow", slow_insert, slow_queries)


speed_test()
