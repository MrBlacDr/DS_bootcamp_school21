import timeit


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

def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    extended_emails = []
    for _ in range(5):
        extended_emails.extend(emails)

    times_loop = timeit.timeit(lambda: loop(extended_emails), number=900000)
    times_comp = timeit.timeit(lambda: comprehension(extended_emails), number=900000)
    times_map = timeit.timeit(lambda: map_approach(extended_emails), number=900000)

    times_dict = {'It is better to use a loop': times_loop,
                'It is better to use a list comprehension': times_comp,
                'It is better to use a map': times_map}
    order = sorted(times_dict.items(), key=lambda x:x[1])
    print(order[0][0])
    result_str = ' vs '.join(map(lambda x: str(x[1]), order))
    print(result_str)

if __name__ == "__main__":
    main()