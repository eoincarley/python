##!/usr/bin/env python3

import datetime
import time
import matplotlib.pyplot as plt
import numpy
import krakenex
import pdb

k = krakenex.API()			# Define the Kraken API object
k.load_key('kraken.key')	# Input the key to communicate with private account
currency_pair = 'XXBTZEUR'	# Define currency pair

current_time = time.time()	# UTC in seconds since epoch 1970-01-01T00:00:00
plus_min = current_time + 60.0
plus_hour = current_time + 3600.

order_placed = 0
sold = 0
volume_XBT = 0.02

while current_time<plus_hour:

	#--------------------------#
	#  Latest Submitted Orders
	#
	spread_latest = k.query_public(method='Spread', req={'pair': currency_pair})
	spread_latest = spread_latest['result'][currency_pair]

	time_utc = [ float(spread_latest[i][0]) for i in numpy.arange(len(spread_latest)) ]
	fmt_times = [ time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime(time_utc[i])) for i in numpy.arange(len(spread_latest))]
	time_utc = [ time_utc[i]/(24.*60.*60.) for i in numpy.arange(len(spread_latest)) ]
	bids = [ float(spread_latest[i][1]) for i in numpy.arange(len(spread_latest)) ]
	asks = [ float(spread_latest[i][2]) for i in numpy.arange(len(spread_latest)) ]
	#print(fmt_times)

	#----------------------------------#
	#	Plot latest submitted orders
	#
	#pdb.set_trace()
	plt.figure(1)
	line1, =plt.plot_date(time_utc, asks, 'r', linewidth=0.5)
	plt.plot_date(time_utc, asks, 'bo', markersize=1.0)
	line2, =plt.plot_date(time_utc, bids, 'g', linewidth=0.5)
	plt.plot_date(time_utc, bids, 'bo', markersize=1.0)
	plt.ylabel('XXBTZEUR Latest Asks/Bids (1 XBT = y EUR)')
	plt.xlabel('Time (UT)')
	axes = plt.gca()
	axes.set_ylim([min(bids)-0.5, max(asks)+0.5])
	grid(b=True, which='major', color='#d3d3d3', linestyle='--')
	plt.legend([line1, line2], ["Asks", "Bids"], loc=4)
	plt.show()

	#----------------------------------#
	#	 Calculate useful metrics
	#
	mean_bid = mean( bids[-21:-1] )
	mean_ask = mean( asks[-21:-1] )
	'''
	print(' Mean of last 20 bids: %6.2f EUR.' % mean_bid)
	print(' Mean of last 20 asks: %6.2f EUR.' % mean_ask)
	print('- - - -')
	'''

	#----------------------------------#
	#	 	Place orders
	#
	#print(order_placed)
	if order_placed==0:
		print('Market bid placed at: %6.2f' % mean_ask)
		desired_price = mean_ask + 0.01/volume_XBT
		order_placed=1

	print('Waiting for bid to reach %6.2f:' % desired_price)
	print('Current mean bid %6.2f' % mean_bid)
	print('- - - -')

	if order_placed==1 and mean_bid >= desired_price:
		print('Market ask placed at: %6.2f ' % mean_bid)
		print('Profit: %1.3f cents' % 0.01)
		# Then wait for the market to drop again below the sell price.
		# if mean_ask < sold_value - 5. then go again.

	# If the market drops significantly shift the desired price down.	
	# NOTE. This will accept a loss.
	#if mean_bid <= desired_price - 10.0:
	#	desired_price = desired_price - 7.0	
	
	current_time = time.time()
	plt.pause(5.0)

