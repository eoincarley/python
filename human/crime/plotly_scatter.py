import plotly.plotly as py
import plotly.graph_objs as go
import csv
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as colors_fun
import pdb

file = open('sexual_violence.csv', 'rt')
reader = csv.reader(file)
data = [x for x in reader]
data = np.array(data)

#--------------------------------------------------------#
#		Arrange the data into a dictionary format
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

ind_region = np.where(region != '')
ind_region = ind_region[0]
ind_subreg = np.where(sub_region != '')
ind_subreg = ind_subreg[0]
ind_country = np.where(country != '')
ind_country= ind_country[0]

master_data = {}

for indexc, objc in enumerate(ind_country):
	cntry = country[objc]

	related_subr = np.where(ind_subreg==objc)
	related_reg = np.where(ind_region==objc)

	related_subr = [y for x in related_subr for y in x]
	related_reg = [y for x in related_reg for y in x]
	stat = [x for x in counts_per_1e5[indexc]]
	for i, obj in enumerate(stat): 
			if obj=='': stat[i] = '0' 

	stat = [float(x.replace(',','')) for x in stat]

	if len(related_reg) != 0:
		reg = region[ind_region[related_reg]][0]
		master_data.update({reg:{}})
		print(reg)

	if len(related_subr) != 0:
		subr = sub_region[ind_subreg[related_subr]][0]
		print('   ', subr)
		master_data[reg].update({subr:{}})

	master_data[reg][subr].update({cntry:stat})



#--------------------------------------------------------#
#		 	Produce plots of stats over time
#
#				First do Northern Europe
#
#trend = master_data['Europe']['Northern Europe']['Sweden']
#trend1 = master_data['Europe']['Northern Europe']['Ireland']
region = 'Europe'
subregion = 'Northern Europe'
neuro_keys =  master_data[region][subregion].keys()
colors = cm.rainbow(np.linspace(0, 1, len(neuro_keys)))
colors = [colors_fun.rgb2hex(color) for color in colors]

for index, key in enumerate(neuro_keys):
	trend = master_data[region][subregion][key]
	if index==0:
		traces = [go.Scatter(x=years_counts, y=trend, marker={'color': colors[index], 'symbol': 100, 'size': "10"}, 
            mode="markers+lines",  text=[key], name=key)]
	else:
		trace = go.Scatter(x=years_counts, y=trend, marker={'color': colors[index], 'symbol': 100, 'size': "10"}, 
                                               mode="markers+lines",  text=[key], name=key)
		traces.append(trace)


layout = {'xaxis': {'title': 'Year'},
  'yaxis': {'title': 'Assault per 100,000 of population'}}
data = go.Data(traces)
plot2 = py.iplot(go.Figure(data=data, layout=layout), filename='Sexual-Assault-N-Europe')



