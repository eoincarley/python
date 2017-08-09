import matplotlib
import matplotlib.pyplot as plt
import datetime
import numpy as np
import pdb
from os import listdir

# Set the directory and list the files
directory = '/Users/eoincarley/python/memory_usage/'
files = listdir(directory)

#---------------------------------------#
#		Read column data from multiple years
#
for i in range(len(files)):
	print files[i]
	size, dates = np.loadtxt(directory+files[i], unpack='True', dtype={'names':('times', 'data'), 'formats':('f4', 'a10')} )
	size = size*512./1e6
	# Get rid of folders that arent yyyy/mm/dd
	indices = [x for x in range(len(dates)) if len(dates[x]) > 9]

	size_yend = size[len(size)-1]
	dates_yend = dates[len(dates)-1]+'12/12'
	
	size = size[indices]
	dates = dates[indices]

	if i==0: 
		dates_total = dates
		size_total = size
		size_histo = size_yend
		dates_histo = dates_yend
	else:
		dates_total = np.append(dates_total, dates)
		size_total = np.append(size_total, size)
		size_histo = np.append(size_histo, size_yend)
		dates_histo = np.append(dates_histo, dates_yend)

# Put dates into useable time format
dates_new=[datetime.datetime.strptime(date, '%Y/%m/%d') for date in dates_total]

# Sort by dates
sort_index = numpy.argsort(dates_new)
dates_new1 = [dates_new[x] for x in sort_index]
size_total = size_total[sort_index]

#---------------------------------------#
#			Plot Data rates
#
plt.figure(1)
plt.subplot(311)
plt.plot_date(dates_new1, size_total, linestyle='dashed',  markersize=0.1)
plt.yscale('log')
plt.ylabel('Data Rate (Mb per day)')
plt.xlabel('Time (UT)')
grid(b=True, which='major', color='#d3d3d3', linestyle='--')

size_cumulat = [sum(size_total[0:i]) for i in range(len(size_total))]
plt.subplot(312)
plt.plot_date(dates_new1, size_cumulat, linestyle='dashed',  markersize=0.1, color='g')
plt.yscale('log')
plt.ylabel('Cumulative Data (Mb)')
plt.xlabel('Time (UT)')
grid(b=True, which='major', color='#d3d3d3', linestyle='--')
axes = plt.gca()
axes.set_ylim([10.,1e7])

#---------------------------------------#
#			Make histogram
#
size_histo = size_histo/1e3
dates_new = [datetime.datetime.strptime(date, '%Y/%m/%d') for date in dates_histo]
bins = np.linspace(dates_new[0].year, dates_new[len(dates_new)-1].year, len(dates_new)) 
width = 1.0*(bins[1] -bins[0])
center = (bins[:-1] + bins[1:])/2.0	

#---------------------------------------#
#			Plot histogram
#
plt.subplot(313)
plt.bar(bins, size_histo, width=width, bottom=1.0, edgecolor='b', color='#d2c3c4')
plt.yscale('log')
plt.ylabel('Stored data (Gb)')
plt.xlabel('Year')
axes = plt.gca()
axes.set_xlim([1996,2017])
plt.xticks( np.arange(1997, 2017, 2.0) )
grid(b=True, which='major', color='#d3d3d3', linestyle='--')
plt.show()

pdb.set_trace()



