import sys
import requests
from time import sleep
from bs4 import BeautifulSoup


def get_html(ticker):
    base_url = f'https://finance.yahoo.com/quote/{ticker}/financials/'
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36', # ua, #'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:147.0) Gecko/20100101 Firefox/147.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    response = session.get(
            base_url,
            headers=headers,
            timeout=5,
            allow_redirects=True
    )
    if response.status_code==200:
        txt = response.text
    elif response.status_code==400:
        raise Exception(f"Ticker '{ticker}' not found (404 error)")
    else:
        raise Exception(f"Failed to fetch data. HTTP status: {response.status_code}")

    return txt


def parse_finance(txt, field):
    soup = BeautifulSoup(txt, 'html.parser')

    table = soup.find('div', class_='table yf-yuwun0')

    if not table:
        raise Exception('URL does not exist')

    prices = table.find('div', title=field).find_all_next('div', limit=5)

    return tuple([field] + list(map(lambda x: x.text.strip(), prices)))


def main():
    try:
        if len(sys.argv) != 3:
            raise ValueError('incorrect input')
        # sleep(5)
        ticker = sys.argv[1]
        txt = get_html(ticker)
        field = sys.argv[2]
        result = parse_finance(txt, field)
        print(result)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()