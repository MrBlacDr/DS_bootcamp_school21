import sys

def send_to_call_center(clients, recipients):
    c = set(clients)
    r = set(recipients)
    print(list(c-r))


def can_be_potential_clients(clients, participants):
    c = set(clients)
    p = set(participants)
    print(list(p-c))


def suggest_loyalty_program(clients, participants):
    c = set(clients)
    p = set(participants)
    print(list(c-p))


def main():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
        'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
        'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
        'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
        'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if len(sys.argv) != 2:
        return
    
    command = sys.argv[1]

    if command == 'call_center':
        send_to_call_center(clients, recipients)
    elif command == 'potential_clients':
        can_be_potential_clients(clients, participants)
    elif command == 'loyalty_program':
        suggest_loyalty_program(clients, participants)
    else:
        raise Exception('the wrong name is given')

if __name__ == "__main__":
    main()
