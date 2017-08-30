import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
import csv
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as colors_fun
import pdb

def make_traces(region, subregion, master_data):

	neuro_keys =  master_data[region][subregion].keys()
	colors = cm.rainbow(np.linspace(0, 1, len(neuro_keys)))
	colors = [colors_fun.rgb2hex(color) for color in colors]

	for index, key in enumerate(neuro_keys):
		trend = master_data[region][subregion][key]
		if index==0:
			traces = [go.Scatter(x=years_counts, y=trend, line = {'width':1}, marker={'color': colors[index], 'symbol': 100, 'size': "5"}, 
	            mode="markers+lines",  text=[key], name=key)]
		else:
			trace = go.Scatter(x=years_counts, y=trend, line = {'width':1}, marker={'color': colors[index], 'symbol': 100, 'size': "5"}, 
	                                               mode="markers+lines",  text=[key], name=key)
			traces.append(trace)

	return traces;		


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
region = 'Africa'

if region=='Europe':
	traces0 = make_traces(region, 'Northern Europe', master_data)
	traces1 = make_traces(region, 'Western Europe', master_data)
	traces2 = make_traces(region, 'Southern Europe', master_data)
	traces3 = make_traces(region, 'Eastern Europe', master_data)

	pdb.set_trace()


	fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Northern Europe', 'Western Europe',
	                                                          'Southern Europe', 'Eastern Europe'))

	for trace in traces0: fig.append_trace(trace, 1, 1)
	for trace in traces1: fig.append_trace(trace, 1, 2)
	for trace in traces2: fig.append_trace(trace, 2, 1)
	for trace in traces3: fig.append_trace(trace, 2, 2)


	fig['layout'].update(height=1000, width=1000, showlegend=False, 
					title='Sexual Assault per 100,000 of population: '+region,  
					xaxis=dict(domain=[0, 0.47], title='Year'), yaxis=dict(domain=[0.55, 0.93], title='Assault per 100,000', range=[0,70]),
				    xaxis2=dict(domain=[0.53, 1.0], title='Year'), yaxis2=dict(domain=[0.55, 0.93], range=[0,70]),
				    xaxis3=dict(domain=[0.0, 0.47], title='Year'), yaxis3=dict(domain=[0.0, 0.4], title='Assault per 100,000', range=[0, 10]),    
				    xaxis4=dict(domain=[0.53, 1.0], title='Year'), yaxis4=dict(domain=[0.0, 0.4], range=[0, 10])
				)

	py.iplot(fig, filename='Sexual-Assault-'+region)


#--------------------------------------------------------#
#		 	Produce plots of stats over time
#
#				  Now the Americas
#
if region=='Americas':
	traces0 = make_traces(region, 'Northern America', master_data)
	traces1 = make_traces(region, 'Caribbean', master_data)
	traces2 = make_traces(region, 'Central America', master_data)
	traces3 = make_traces(region, 'South America', master_data)


	fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Northern America', 'Caribbean',
	                                                          'Central America', 'South America'))

	for trace in traces0: fig.append_trace(trace, 1, 1)
	for trace in traces1: fig.append_trace(trace, 1, 2)
	for trace in traces2: fig.append_trace(trace, 2, 1)
	for trace in traces3: fig.append_trace(trace, 2, 2)


	fig['layout'].update(height=1000, width=1000, showlegend=False, 
					title='Sexual Assault per 100,000 of population: '+region,  
					xaxis=dict(domain=[0, 0.47], title='Year'), yaxis=dict(domain=[0.55, 0.93], title='Assault per 100,000', range=[-0.09, 2], type='log'),
				    xaxis2=dict(domain=[0.53, 1.0], title='Year'), yaxis2=dict(domain=[0.55, 0.93], range=[-0.09, 2], type='log'),
				    xaxis3=dict(domain=[0.0, 0.47], title='Year'), yaxis3=dict(domain=[0.0, 0.4], title='Assault per 100,000', range=[0, 1.7], type='log'),    
				    xaxis4=dict(domain=[0.53, 1.0], title='Year'), yaxis4=dict(domain=[0.0, 0.4], range=[0, 1.7], type='log')
				)

	py.iplot(fig, filename='Sexual-Assault-'+region)

#--------------------------------------------------------#
#		 	Produce plots of stats over time
#
#				  	Now Asia
#
if region=='Asia':
	traces0 = make_traces(region, 'Central Asia', master_data)
	traces1 = make_traces(region, 'Eastern Asia', master_data)
	traces2 = make_traces(region, 'South-Eastern Asia', master_data)
	traces3 = make_traces(region, 'Southern Asia', master_data)
	traces4 = make_traces(region, 'Western Asia', master_data)
	traces5 = traces4


	fig = tools.make_subplots(rows=3, cols=2, subplot_titles=('Central Asia', 'Eastern Asia',
	                                                          'South-Eastern Asia', 'Southern Asia', 'Western Asia'))

	for trace in traces0: fig.append_trace(trace, 1, 1)
	for trace in traces1: fig.append_trace(trace, 1, 2)
	for trace in traces2: fig.append_trace(trace, 2, 1)
	for trace in traces3: fig.append_trace(trace, 2, 2)
	for trace in traces4: fig.append_trace(trace, 3, 2)
	for trace in traces5: fig.append_trace(trace, 3, 2)


	fig['layout'].update(height=1000, width=1000, showlegend=False, 
					title='Sexual Assault per 100,000 of population: '+region,  
					xaxis=dict(domain=[0, 0.47], title='Year'), yaxis=dict(domain=[0.75, 1.0], title='Assault per 100,000', range=log10([0.4, 30]), type='log'),
				    xaxis2=dict(domain=[0.53, 1.0], title='Year'), yaxis2=dict(domain=[0.75, 1.0], range=log10([0.4, 30]), type='log'),

				    xaxis3=dict(domain=[0.0, 0.47], title='Year'), yaxis3=dict(domain=[0.39, 0.66], title='Assault per 100,000', range=log10([0.1, 30]), type='log'),    
				    xaxis4=dict(domain=[0.53, 1.0], title='Year'), yaxis4=dict(domain=[0.39, 0.66], range=log10([0.1, 30]), type='log'),

				    xaxis5=dict(domain=[0.0, 0.47], title='Year'), yaxis5=dict(domain=[0.03, 0.30], title='Assault per 100,000', range=log10([0.1, 50]), type='log'),
				    xaxis6=dict(domain=[0.0, 0.47], title='Year'), yaxis6=dict(domain=[0.03, 0.30], range=log10([0.1, 50]), type='log')
				)

	py.iplot(fig, filename='Sexual-Assault-'+region)

#--------------------------------------------------------#
#		 	Produce plots of stats over time
#
#				  	Now Asia
#
if region=='Africa':
	traces0 = make_traces(region, 'Eastern Africa', master_data)
	traces1 = make_traces(region, 'Middle Africa', master_data)
	traces2 = make_traces(region, 'Northern Africa', master_data)
	traces3 = make_traces(region, 'Southern Africa', master_data)
	traces4 = make_traces(region, 'Western Africa', master_data)
	traces5 = traces4


	fig = tools.make_subplots(rows=3, cols=2, subplot_titles=('Eastern Africa', 'Middle Africa',
	                                                          'Northern Africa', 'Southern Africa', 'Western Africa'))

	for trace in traces0: fig.append_trace(trace, 1, 1)
	for trace in traces1: fig.append_trace(trace, 1, 2)
	for trace in traces2: fig.append_trace(trace, 2, 1)
	for trace in traces3: fig.append_trace(trace, 2, 2)
	for trace in traces4: fig.append_trace(trace, 3, 2)
	for trace in traces5: fig.append_trace(trace, 3, 2)


	fig['layout'].update(height=1000, width=1000, showlegend=False, 
					title='Sexual Assault per 100,000 of population: '+region,  
					xaxis=dict(domain=[0, 0.47], title='Year'), yaxis=dict(domain=[0.75, 1.0], title='Assault per 100,000' , range=log10([0.1, 50]), type='log'),
				    xaxis2=dict(domain=[0.53, 1.0], title='Year'), yaxis2=dict(domain=[0.75, 1.0]),

				    xaxis3=dict(domain=[0.0, 0.47], title='Year'), yaxis3=dict(domain=[0.39, 0.66], title='Assault per 100,000'),    
				    xaxis4=dict(domain=[0.53, 1.0], title='Year'), yaxis4=dict(domain=[0.39, 0.66]),

				    xaxis5=dict(domain=[0.0, 0.47], title='Year'), yaxis5=dict(domain=[0.03, 0.30], title='Assault per 100,000', range=log10([0.01, 50]), type='log'),
				    xaxis6=dict(domain=[0.0, 0.47], title='Year'), yaxis6=dict(domain=[0.03, 0.30], range=log10([0.01, 50]), type='log')
				)

	py.iplot(fig, filename='Sexual-Assault-'+region)	

