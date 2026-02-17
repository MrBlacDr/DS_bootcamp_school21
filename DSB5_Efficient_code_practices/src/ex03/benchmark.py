import timeit
import sys
from functools import reduce


def ordinary_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i*i
    return s


def reduce_approach(n):
    return reduce(lambda x, y: x + y*y, range(1, n+1))


def main():
    if len(sys.argv) != 4:
        print('Usage: <function> <num_calls> <num_members>')
        return

    mapping = {'loop': 'ordinary_sum', 'reduce': 'reduce_approach'}

    try:
        if sys.argv[1] not in mapping.keys():
            raise ValueError('available functions: loop, reduce')
        try:
            num_calls = int(sys.argv[2])
            n = int(sys.argv[3])
        except ValueError:
            raise ValueError('num_calls and num_members must be integer!')            
        
        namespace = {
            'ordinary_sum': ordinary_sum,
            'reduce_approach': reduce_approach,
            'n': n
        }
        times = timeit.timeit(f'{mapping[sys.argv[1]]}(n)', globals=namespace, number=num_calls)
        print(times)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()