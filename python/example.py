import json

from indodax import Indodax

idx = Indodax()

# Get rates from external exchange
external_rates_summaries = idx.external_rates_summaries()

if external_rates_summaries != False:
    print(json.dumps(external_rates_summaries, sort_keys=True, indent=4))
    print (external_rates_summaries['cny_idr'])

# Get ticker of all pairs
all_tickers = idx.tickers()

if (all_tickers != False):
    print(json.dumps(all_tickers, sort_keys=True, indent=4))
    print (all_tickers['tickers']['trx_idr']['last'])

# Get ticker of a pair
btc_idr_ticker = idx.ticker('btc_idr')

if (btc_idr_ticker != False):
    print(json.dumps(btc_idr_ticker, sort_keys=True, indent=4))
    print (btc_idr_ticker['ticker']['last'])

# Get sell prices of a pair
last_btc_idr_sell_prices = idx.last_sell_prices('btc_idr')

if (last_btc_idr_sell_prices != False):
    print(json.dumps(last_btc_idr_sell_prices, sort_keys=True, indent=4))
