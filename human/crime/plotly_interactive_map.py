import csv
import numpy as np
import pandas as pd
import plotly.plotly as py
import pdb

file = open('sexual_violence.csv', 'rt')
reader = csv.reader(file)
data = [x for x in reader]
data = np.array(data)

#---------------------------------------------#
#				Arrange the data 
#
data0 = data[0]
indices = np.where(data0 != '')
indices = indices[0]
master_keys = data0[indices]
years_counts = data[1][indices[0]:indices[1]-1]
years_counts_1e5 = data[1][indices[1]:len(data[1])]

data = data[2:len(data)]
region = np.array([data[x][0] for x in range(len(data))]) 	  
sub_region =  np.array([data[x][1] for x in range(len(data))]) 
country =  np.array([data[x][2] for x in range(len(data))])    


for index, arr in enumerate(data):
    count = arr[indices[0]:indices[1]-1] 
    count[np.where(count=='')] ='0.0'
    count = [float(el.replace(',','')) for el in count]
    if index==0:
        counts = [count]
    else:
        counts.append(count)
        
for index, arr in enumerate(data):
    count = arr[indices[1]:len(data[1])] 
    count[np.where(count=='')] ='0.0'
    count = [float(el) for el in count]
    if index==0:
        counts_per_1e5 = [count]
    else:
        counts_per_1e5.append(count)
        
#---------------------------------#
#		Get average over time
# 
average = [mean(dat) for dat in counts_per_1e5]    # yr is the index of the chosen year
cntry_data = dict()
result = [cntry_data.update( {country[i]:average[i]} ) for i in np.arange(0, len(country))]

#---------------------------------#
#       Get specific lear
# 
#yr=5
#latest = [dat[yr] for dat in counts_per_1e5]    # yr is the index of the chosen year
#cntry_data = dict()
#result = [cntry_data.update( {country[i]:latest[i]} ) for i in np.arange(0, len(country))]

country_key = np.load('country_key.npy').item()
countries = country_key.keys()
countries = [i for i in countries ]
codes = country_key.values()
codes = [i for i in codes]
new_counts=[]


for ind, item in enumerate(countries):
	if item in cntry_data:
		new_counts = np.append(new_counts, float('%.1f' %round(cntry_data[item], 3)))
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
                width = 0.3
            ) ),
        colorbar = dict(
            autotick = False,
            tickprefix = '',
            title = 'Assault <br>per 1e5',
            thickness = 5,
            len =0.6,
            xpad=0,
            ypad=0),
      ) ]


layout = dict(
    title = 'Sexual assault per 100,000 of population',
    geo = dict(
    	resolution=130,
        showframe = False,
        showcoastlines = False,
        projection = dict(
            type = 'eckert4'),
        lonaxis = dict(showgrid=True),  
        lataxis = dict(showgrid=True) 
        ),
    )

fig = dict( data=data, layout=layout )
py.iplot( fig, validate=False, filename='Sexual-assault-per-1e5' )