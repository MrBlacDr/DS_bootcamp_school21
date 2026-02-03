import sys

def all_stocks():

    if len(sys.argv) != 2:
        return
    
    input_string = sys.argv[1].strip()
    
    if ',,' in input_string:
        return
    
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
    
    companies_lower = {k.lower(): (k, v) for k, v in COMPANIES.items()}
    stocks_lower = {k.lower(): (k, v) for k, v in STOCKS.items()}
    
    expressions = [expr.strip() for expr in input_string.split(',')]
    
    results = []
    
    for expr in expressions:
        if not expr:
            # не обрабатываем строку, в которой были пробелы в запятых
            return
        
        expr_lower = expr.lower()
        
        if expr_lower in companies_lower.keys():
            company_name, ticker = companies_lower[expr_lower]
            price = STOCKS[ticker]
            results.append(f"{company_name} stock price is {price}")
        
        elif expr_lower in stocks_lower:
            ticker_symbol, price = stocks_lower[expr_lower]
            for comp_name, comp_ticker in COMPANIES.items():
                if comp_ticker == ticker_symbol:
                    results.append(f"{ticker_symbol} is a ticker symbol for {comp_name}")
                    break
        
        else:
            results.append(f"{expr} is an unknown company or an unknown ticker symbol")
    
    if results:
        print('\n'.join(results))

if __name__ == "__main__":
    all_stocks()