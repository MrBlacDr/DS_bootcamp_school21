import timeit
import sys


def loop(emails):
    new_list = []
    for email in emails:
        if email.endswith('@gmail.com'):
            new_list.append(email)
    return new_list


def comprehension(emails):
    new_list = [email for email in emails if email.endswith('@gmail.com')]
    return new_list


def map_approach(emails):
    new_list = list(map(lambda x: x if x.endswith('@gmail.com') else None, emails))
    return new_list


def filter_approach(emails):
    new_list = list(filter(lambda x: x.endswith('@gmail.com'), emails))
    return new_list


def main():
    if len(sys.argv) != 3:
        print('Usage: <function> <num_calls>')
        return
    
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    extended_emails = []
    for _ in range(5):
        extended_emails.extend(emails)

    namespace = {
        'loop': loop,
        'comprehension': comprehension,
        'map_approach': map_approach,
        'filter_approach': filter_approach,
        'emails': extended_emails
    }
    mapping = {'loop': 'loop',
        'list_comprehension': 'comprehension',
        'map': 'map_approach',
        'filter': 'filter_approach'
    }

    try:
        if sys.argv[1] not in mapping.keys():
            raise ValueError('available functions: loop, list_comprehension, map, filter')
        try:
            num_calls = int(sys.argv[2])
        except ValueError:
            raise ValueError('num_calls must be integer!')            
        
        times = timeit.timeit(f'{mapping[sys.argv[1]]}(emails)', globals=namespace, number=num_calls)
        print(times)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()