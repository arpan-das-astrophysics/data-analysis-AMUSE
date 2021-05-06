import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy
from scipy.stats import norm
import pandas
import matplotlib.ticker as mticker
from pandas.compat.pickle_compat import _class_locations_map

_class_locations_map.update({
    ('pandas.core.internals.managers', 'BlockManager'): ('pandas.core.internals', 'BlockManager')
})

df=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/constant1.e-6/output.csv')
time=np.array(df['t[Myr]'])
Mmax=np.array(df['M_max[MSun]'])

fig1=plt.figure(dpi=72,figsize=(35, 31))
ax1= fig1.add_subplot(111)
plt.plot(time,Mmax, linewidth=12, color='blue', linestyle = '-')

ax1.set_yscale("log")
#ax1.set_xscale("log")
#ax1.set_ylim(10,100)
ax1.set_xlim(0,5)
ax1.xaxis.set_label_text(r'$ {\rm time[Myr]}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm M_{max} (M_\odot)}$', fontsize = 120, color='black')
ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)
ax1.tick_params('both', length=25, width=1, which='minor')

plt.tight_layout()
plt.savefig('maximummass.pdf')
