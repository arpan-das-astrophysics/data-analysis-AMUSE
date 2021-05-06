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
lagrange10=np.array(df['lagrange10'])
lagrange50=np.array(df['lagrange50'])
lagrange90=np.array(df['lagrange90'])

fig1=plt.figure(dpi=72,figsize=(35, 31))
ax1= fig1.add_subplot(111)



plt.plot(time,lagrange10, linewidth=12, color='blue', linestyle = '-',label=r'${\rm 10\%}$')
plt.plot(time,lagrange50, linewidth=12, color='green', linestyle = '-',label=r'${\rm 50\%}$')
plt.plot(time, lagrange90, linewidth=12, color='red', linestyle = '-',label=r'${\rm 90\%}$')




ax1.set_yscale("log")
#ax1.set_xscale("log")
ax1.set_xlim(0,5)
ax1.set_ylim(1.e-2,1.0)
ax1.xaxis.set_label_text(r'$ {\rm time[Myr]}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm Lagrange\,Radii (pc)}$', fontsize = 120, color='black')

ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)
ax1.tick_params('both', length=25, width=1, which='minor')

plt.legend(fancybox=True, shadow=True, fontsize=70,loc='lower right')
plt.tight_layout()
plt.savefig('lagrange.pdf')
