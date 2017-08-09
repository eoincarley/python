import sunpy
import sunpy.map
import matplotlib.pyplot as plt
import pdb
from os import listdir
from os.path import isfile, join


path_a = '/Users/eoincarley/Data/elevate_db/2014-04-18/SDO/AIA/171/'
path_b = '/Users/eoincarley/Data/elevate_db/2014-04-18/SDO/AIA/193/'
path_c = '/Users/eoincarley/Data/elevate_db/2014-04-18/SDO/AIA/211/'
files_a = [f for f in listdir(path_a) if isfile(join(path_a, f))]
files_b = [f for f in listdir(path_b) if isfile(join(path_a, f))]
files_c = [f for f in listdir(path_c) if isfile(join(path_c, f))]

#pdb.set_trace()
aia_map = sunpy.map.Map(join(path_a, files_a[1]))
aia_map.plot()
aia_map.draw_limb()
aia_map.draw_grid()
plt.show()

#pdb.set_trace()