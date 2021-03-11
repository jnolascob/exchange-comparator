import requests
import lxml.html as html

KAMBISTA_URL = 'https://kambista.com'
XPATH_SELL_PRICE = '//div[@class="km_calc-encabezado"]/strong[@id="valventa"]/text()'
XPATH_PURCHASE_PRICE = '//div[@class="km_calc-encabezado"]/strong[@id="valcompra"]/text()'

def retrieve_website():
    try:
        response = requests.get(KAMBISTA_URL)
        if response.status_code == 200:
            content = response.content.decode('utf-8')
            parsed = html.fromstring(content)
            return parsed
        else:
            raise ValueError('request failed')
    except ValueError as error:
        print(error)

def get_sell_price(parsed):
    return parsed.xpath(XPATH_SELL_PRICE)[0].strip()

def get_purchase_price(parsed):
    return parsed.xpath(XPATH_PURCHASE_PRICE)[0].strip()

def run():
    content_parsed = retrieve_website()
    print('=> sell price:', get_sell_price(content_parsed))
    print('=> purchase price:', get_purchase_price(content_parsed))

if __name__ == '__main__':
    run()