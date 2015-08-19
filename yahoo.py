import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import pandas.io.data as web
all_data = {}
try:
	for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
		all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2003', '1/1/2013')
		price = DataFrame({tic: data['Adj Close']
			for tic, data in all_data.iteritems()})
		volume = DataFrame({tic: data['Volume']       
			for tic, data in all_data.iteritems()})
except Exception, e:
	print "Cant find ", ticker

 	
returns = price.pct_change()
print returns.tail()
