import requests

class Indodax:
    def __init__(self):
        self.base_url = 'https://indodax.com'
    
    def external_rates_summaries(self):
        resp = requests.get(self.base_url + '/api/external_rates_summaries')

        if (resp.status_code == 200):
            return resp.json()

        return False

    def tickers(self):
        resp = requests.get(self.base_url + '/api/tickers')

        if (resp.status_code == 200):
            return resp.json()

        return False

    def ticker(self, pair):
        resp = requests.get(self.base_url + '/api/' + pair + '/ticker')

        if (resp.status_code == 200):
            return resp.json()

        return False

    def trade_history(self, pair):
        resp = requests.get(self.base_url + '/api/' + pair + '/trades')

        if (resp.status_code == 200):
            return resp.json()

        return False

    def last_prices(self, pair):
        resp = requests.get(self.base_url + '/api/' + pair + '/depth')

        if (resp.status_code == 200):
            return resp.json()

        return False

    def last_buy_prices(self, pair):
        resp = self.last_prices(pair)
        
        if (resp == False):
            return False

        return resp['buy']

    def last_sell_prices(self, pair):
        resp = self.last_prices(pair)
        
        if (resp == False):
            return False

        return resp['sell']
