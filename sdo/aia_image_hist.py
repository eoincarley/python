import sunpy
import sunpy.map
import numpy as np
import matplotlib.pyplot as plt
import pdb
from os import listdir
from os.path import isfile, join
from scipy import stats


path_a = '/Users/eoincarley/Data/elevate_db/2014-04-18/SDO/AIA/211/'
files_a = [f for f in listdir(path_a) if isfile(join(path_a, f))]

aia_171_map = sunpy.map.Map(join(path_a, files_a[1]))

#--------------------------------#
#	   Normalise the arrays
#
data_a = aia_171_map.data/aia_171_map.exposure_time
data_a = data_a/np.ndarray.max(data_a)
data_a = np.array(data_a)
hist, bins = np.histogram(data_a, bins=np.linspace(1e-4, 1e-1, 1000.))
width = 1.0 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, width=width)
plt.yscale('log', nonposy='clip')
plt.xscale('log', nonposy='clip')
plt.show()
