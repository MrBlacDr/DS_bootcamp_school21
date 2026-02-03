import sys

def main():
    if len(sys.argv) != 2:
        return

    company_ticker = sys.argv[1]

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

    if company_ticker.upper() not in STOCKS.keys():
        print('Unknown ticker')
        return

    founded_value = ''
    for ticker in STOCKS.keys():
        if ticker == company_ticker.upper():
            founded_value = ticker
            break
    
    founded_name = ''
    for k, v in COMPANIES.items():
        if v == founded_value:
            founded_name = k
            break
    
    print(founded_name, STOCKS[founded_value])


if __name__ == "__main__":
    main()