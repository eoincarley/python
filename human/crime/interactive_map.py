import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import time
import pandas as pd
from matplotlib import colors as mcolors 
import plotly.plotly as py
import pdb

file = open('stats_crime_v2.csv', 'rt')
reader = csv.reader(file)
data = [x for x in reader]
data = np.array(data)

#--------------------------------------------------------#
#				Arrange the data 
#
data0 = data[0]
indices = np.where(data0 != '')
indices = indices[0]
master_keys = data0[indices]
years_counts = data[1][indices[0]:indices[1]-1]
years_counts_1e5 = data[1][indices[1]:len(data[1])]

data = data[2:len(data)]
region = np.array([data[x][0] for x in range(len(data))]) 	   # if data[x][0] != '']
sub_region =  np.array([data[x][1] for x in range(len(data))]) # if data[x][1] != '']
country =  np.array([data[x][2] for x in range(len(data))])    # if data[x][2] != '']
counts = [data[x][indices[0]:indices[1]-1] for x in range(len(data))]
counts_per_1e5 = [data[x][indices[1]:len(data[1])] for x in range(len(data))]


#---------------------------------#
#			Get latest
#

latest = [dat[5] for dat in counts_per_1e5]
latest = np.array(latest)
latest[np.where(latest=='')] = '0.0'
cntry_data = dict()
result = [cntry_data.update( {country[i]:float(latest[i])} ) for i in np.arange(0, len(country))]


country_key = np.load('country_key.npy').item()
countries = country_key.keys()
countries = [i for i in countries ]
codes = country_key.values()
codes = [i for i in codes]
new_counts=[]


for ind, item in enumerate(countries):
	if item in cntry_data:
		new_counts = np.append(new_counts, cntry_data[item])
	else:
		print(item)
		new_counts = np.append(new_counts, 0.0)	
	

countries = pd.Series(countries, index=np.arange(len(countries)))
codes = pd.Series(codes, index=np.arange(len(codes)))
new_counts = pd.Series(new_counts, index=np.arange(len(new_counts)))


data = [ dict(
        type = 'choropleth',
        locations = codes,
        z = new_counts,
        text = countries,
        colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
            [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(180,100,180)',
                width = 0.5
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '',
            title = 'Crime per 1e5'),
      ) ]


layout = dict(
    title = '2014 Crime per 100,000 of population<br>Source:\
            <a href="">UNODC</a>',
    geo = dict(
    	resolution=130,
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'eckert4'
        ),
    lonaxis = dict(showgrid=True),  
    lataxis = dict(showgrid=True)    
    )
)

fig = dict( data=data, layout=layout )
py.iplot( fig, validate=False, filename='d3-world-map' )