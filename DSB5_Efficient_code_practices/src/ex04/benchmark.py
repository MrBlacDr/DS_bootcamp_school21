import timeit
import random
from collections import Counter


def my_counter(a):
    d = {}
    for elem in a:
        d[elem] = d.get(elem, 0) + 1
    return d

def my_top10(a):
    d = my_counter(a)
    i = 0
    top10 = {}
    for pair in sorted(d.items(), key=lambda x: -x[1]):
        if i == 10:
            break
        top10[pair[0]] = pair[1]
        i += 1
    return top10


def main():
    rand_list = [random.randint(0,100) for _ in range(1000000)]

    times_my_count = timeit.timeit(lambda: my_counter(rand_list), number=1)
    times_count = timeit.timeit(lambda: Counter(rand_list), number=1)
    times_my_top10 = timeit.timeit(lambda: my_top10(rand_list), number=1)
    times_top10 = timeit.timeit(lambda: Counter(rand_list).most_common(10), number=1)

    print(f'my function: {times_my_count}')
    print(f'Counter: {times_count}')
    print(f'my top: {times_my_top10}')
    print(f'Counter\'s top: {times_top10}')


if __name__ == "__main__":
    main()