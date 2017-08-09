import sunpy
import sunpy.map
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pdb
from os import listdir
from os.path import isfile, join
from scipy import stats


path_a = '/Users/eoincarley/Data/elevate_db/2014-04-18/SDO/AIA/211/'
path_b = '/Users/eoincarley/Data/elevate_db/2014-04-18/SDO/AIA/193/'
path_c = '/Users/eoincarley/Data/elevate_db/2014-04-18/SDO/AIA/171/'
files_a = [f for f in listdir(path_a) if isfile(join(path_a, f))]
files_b = [f for f in listdir(path_b) if isfile(join(path_b, f))]
files_c = [f for f in listdir(path_c) if isfile(join(path_c, f))]

#pdb.set_trace()
#aia_171_map = sunpy.map.Map(join(path_ba, files_a[1]))
#aia_map.plot()
#aia_map.draw_grid()
#plt.show()

aia_171_map = sunpy.map.Map(join(path_a, files_a[1]))
aia_193_map = sunpy.map.Map(join(path_b, files_b[1]))
aia_211_map = sunpy.map.Map(join(path_c, files_c[1]))

#--------------------------------#
#	   Normalise the arrays
#
data_a = np.array(aia_171_map.data/aia_171_map.exposure_time)
data_a = data_a - np.ndarray.min(data_a)
data_a = log10(data_a)
data_a = (data_a/np.ndarray.max(data_a))

data_b = np.array(aia_193_map.data/aia_193_map.exposure_time)
data_b = data_b - np.ndarray.min(data_b)
data_b = log10(data_b)
data_b = (data_b/np.ndarray.max(data_b))

data_c = np.array(aia_211_map.data/aia_211_map.exposure_time)
data_c = data_c - np.ndarray.min(data_c)
data_c = log10(data_c)
data_c = (data_c/np.ndarray.max(data_c))

rgbArray = np.zeros((4096, 4096, 3))
rgbArray[..., 0] = data_a
rgbArray[..., 1] = data_b
rgbArray[..., 2] = data_c

plt.imshow(rgbArray, vmin=0.1, vmax=1.0)
plt.show()
