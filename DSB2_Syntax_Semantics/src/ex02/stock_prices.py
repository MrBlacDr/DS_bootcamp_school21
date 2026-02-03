import sys

def main():
    if len(sys.argv) != 2:
        return

    company_name = sys.argv[1]

    COMPANIES = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Netflix': 'NFLX',
    'Tesla': 'TSLA',
    'Nokia': 'NOK'
    }

    STOCKS = {
    'AAPL': 287.73,
    'MSFT': 173.79,
    'NFLX': 416.90,
    'TSLA': 724.88,
    'NOK': 3.37
    }

    if company_name.lower() not in list(map(lambda x: x.lower(), COMPANIES.keys())):
        print('Unknown company')
        return

    founded_key = ''
    for name in COMPANIES.keys():
        if name.lower() == company_name.lower():
            founded_key = name
            break
    
    print(STOCKS[COMPANIES[founded_key]])


if __name__ == "__main__":
    main()