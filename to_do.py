#To-do

# Read a txt


# Read a csv and xcel file


# Read a fits file


# Read an ASCII file


# Read a binary file


# Manipulate a time array, from formatted to time since epoch, and vice versa
import time
time_utc = time.mktime( time.strptime("2017-08-07 12:00:00", "%Y-%m-%d %H:%M:%S") )
fmtd_times = time.strftime("%Y-%m-%d %H:%M:%S", time.gntime(time_utc))


# Plot a time series, between two specific times
# Fit a curve to the time series
# Oplot a second time series


# Plot a histogram, binned in units of 10
# Plot a hisotgram of times, binned in units of seconds, minutes, hours
# Fit a Gaussian to the histogram


# Produce a Gaussian of random values and fit it.


# Plot an X-Y scatter plot and get all stats on correlations coefficient etc.


# Design an experiment to produce a chi square distribution.


# Write a function


# Define a class and make an object from that class