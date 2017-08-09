import datetime
import time
import matplotlib.pyplot as plt
import numpy
import krakenex

k = krakenex.API()					# Define the Kraken API object
k.load_key('.krakenkey/kraken.key')	# Input the key to communicate with private account
currency_pair = 'XXBTZEUR'

'''

#--------------------------#
#
#  Latest Submitted Orders
#
spread_latest = k.query_public(method='Spread', req={'pair': currency_pair})
spread_latest = spread_latest['result'][currency_pair]

time_utc = [ float(spread_latest[i][0]) for i in numpy.arange(len(spread_latest))]
bids = [ float(spread_latest[i][1]) for i in numpy.arange(len(spread_latest))]
asks = [ float(spread_latest[i][2]) for i in numpy.arange(len(spread_latest))]

time_utc = [ time_utc[i]/(24.*60.*60.) for i in numpy.arange(len(spread_latest))]
#fmt_times = [ time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime(time_utc[i])) for i in numpy.arange(len(spread_latest))]
#print(fmt_times)

plt.figure(1)
plt.plot_date(time_utc, asks, 'r', linewidth=0.5)
plt.plot_date(time_utc, asks, 'bo', markersize=1.0)
plt.plot_date(time_utc, bids, 'g', linewidth=0.5)
plt.plot_date(time_utc, bids, 'bo', markersize=1.0)
plt.ylabel('XXBTZEUR Echange Rate')
plt.xlabel('Time (UT)')
axes = plt.gca()
axes.set_ylim([min(bids)-0.5, max(asks)+0.5])
grid(b=True, which='major', color='#d3d3d3', linestyle='--')
plt.show()

#--------------------------#
#
# Perform a balance query
#
balance = k.query_private('TradeBalance', req={'asset':'EUR'})
balance_keys = balance.keys()
equity_balance = float(balance['result']['eb'])	# EUR

#print(balance['result'])
#message_line = '----------'
#print(message_line)
#print(' Current equity balance: %4.2f EUR.' % equity_balance)
#print(message_line)

#--------------------------#
#
# Get the latest tading metrics
#
ticker_latest = k.query_public(method='Ticker', req={'pair': currency_pair}, conn=None)
ticker_latest = result['XXBTZEUR']
latest_ask = float(ticker_latest['a'][0])	# EUR
latest_buy = float(ticker_latest['b'][0]) 	# EUR
volume_24hr = float(ticker_latest['v'][0])
ask_mean_24hr = float(ticker_latest['p'][1])	# Is this the ask?

#---------------------------#
#
# 	Latest executed trades
#
trades_latest = k.query_public(method='Trades', req={'pair': currency_pair})
trades_latest = trades_latest['result'][currency_pair]
# Sells
sells_latest = [ float(trades_latest[i][0]) for i in numpy.arange(len(trades_latest)) if trades_latest[i][3]=='s']
sell_times = [ float(trades_latest[i][2]) for i in numpy.arange(len(trades_latest)) if trades_latest[i][3]=='s']
# Buys
buys_latest = [ float(trades_latest[i][0]) for i in numpy.arange(len(trades_latest)) if trades_latest[i][3]=='b']
buy_times = [ float(trades_latest[i][2]) for i in numpy.arange(len(trades_latest)) if trades_latest[i][3]=='b']

sort_index = numpy.argsort(ask_time)
ask_time = [ask_time[x] for x in sort_index]
asks = [asks[x] for x in sort_index]

# time.gmtime(1247169778)
# time.ctime(1247169778))
# time.strftime("%Y/%m/%d %H:%M:%S" ,time.gmtime(1247169778))

#---------------------------#
#
# 	Placing a buy/sell order
#
#result = k.query_private('AddOrder', {'pair': 'XXBTZEUR', 'type': 'buy', 'ordertype': 'limit', 'price': '1102.7', 'volume': '0.005'})
#result = k.query_private('AddOrder', {'pair': 'XXBTZEUR', 'type': 'sell', 'ordertype': 'limit', 'price': '1104.0', 'volume': '0.005'})

'''