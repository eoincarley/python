import matplotlib
import matplotlib.pyplot as plt
import datetime
import numpy as np
import pdb
from os import listdir

# Set the directory and list the files
directory = '/Users/eoincarley/python/memory_usage/'
files = listdir(directory)

# Read column data 
for i in range(len(files)):
	print files[i]
	size, dates = np.loadtxt(directory+files[i], unpack='True', dtype={'names':('times', 'data'), 'formats':('f4', 'a10')} )
	size = size*512./1e6
	size = size[len(size)-1]
	dates = dates[len(dates)-1]+'12/12'

	if i==0: 
		dates_total = dates
		size_total = size
	else:
		dates_total = np.append(dates_total, dates)
		size_total = np.append(size_total, size)


size_total = size_total/1e3
# Put dates into useable time format
dates_new = [datetime.datetime.strptime(date, '%Y/%m/%d') for date in dates_total]

bins = np.linspace(dates_new[0].year, dates_new[len(dates_new)-1].year, len(dates_new)+1) 
width = 1.0*(bins[1] -bins[0])
center = (bins[:-1] + bins[1:])/2	
plt.bar(center, size_total, width=width, bottom=1.0, edgecolor='g')
plt.yscale('log')
plt.ylabel('Stored data (Gb)')
plt.xlabel('Year')
plt.show()

#plt.set_trace()
