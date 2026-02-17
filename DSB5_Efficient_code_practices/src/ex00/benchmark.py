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


def main():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com']
    extended_emails = []
    for _ in range(5):
        extended_emails.extend(emails)


    namespace = {
        'loop': loop,
        'comprehension': comprehension,
        'emails': extended_emails
    }

    times_loop = timeit.repeat(
        'loop(emails)',
        globals=namespace,
        repeat=1,
        number=900000
    )

    times_comp = timeit.repeat(
        'comprehension(emails)',
        globals=namespace,
        repeat=1,
        number=900000
    )

    if times_loop[0] <= times_comp[0]:
        print('It is better to use a loop')
        print(f'{times_loop[0]} vs {times_comp[0]}')
    else:
        print('It is better to use a list comprehension')
        print(f'{times_comp[0]} vs {times_loop[0]}')


if __name__ == "__main__":
    main()