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
Mstar=np.array(df['M_star[MSun]'])/1.e+5
Mgas=np.array(df['M_gas[MSun]'])/1.e+5

fig1=plt.figure(dpi=72,figsize=(35, 31))
ax1= fig1.add_subplot(111)

plt.plot(time,Mgas, linewidth=30, color='red', alpha=0.5, linestyle = '-', label=r'${\rm Gas\, Mass}$')
plt.plot(time,Mstar, linewidth=10, color='blue', linestyle = '-', label=r'${\rm Star\, Mass}$')


#ax1.set_yscale("log")
#ax1.set_xscale("log")
#ax1.set_ylim(,)
ax1.set_xlim(0,5)
ax1.xaxis.set_label_text(r'$ {\rm time[Myr]}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm dE_{total}/E_{total}}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm Mass (10^5\,M_\odot)}$', fontsize = 120, color='black')
ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)
ax1.tick_params('both', length=25, width=1, which='minor')
plt.legend(fancybox=True, shadow=True, fontsize=70,loc='upper left')
plt.tight_layout()
plt.savefig('mass.pdf')
