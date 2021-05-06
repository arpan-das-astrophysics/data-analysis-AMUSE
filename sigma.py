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

df1=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/constant1.e-5/output.csv')
time1=np.array(df1['t[Myr]'])
sigma1=np.array(df1['std'])

df2=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/imfbondi/output.csv')
time2=np.array(df2['t[Myr]'])
sigma2=np.array(df2['std'])

df3=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/eddington/output.csv')
time3=np.array(df3['t[Myr]'])
sigma3=np.array(df3['std'])

fig1=plt.figure(dpi=72,figsize=(35, 31))
ax1= fig1.add_subplot(111)
plt.plot(time1,sigma1, linewidth=12, color='blue', linestyle = '-', label=r'${\rm \dot{m}=10^{-5}\,M_\odot yr^{-1}}$')
plt.plot(time2,sigma2, linewidth=12, color='red', linestyle = '-', label=r'${\rm \dot{m}=\dot{m}_{BH}\,M_\odot yr^{-1}}$')
plt.plot(time3,sigma3, linewidth=12, color='green', linestyle = '-',label=r'${\rm \dot{m}=\dot{m}_{Edd}\,M_\odot yr^{-1}}$')
#ax1.set_yscale("log")
#ax1.set_xscale("log")
ax1.set_ylim(10,65)
ax1.set_xlim(0,5)
ax1.xaxis.set_label_text(r'$ {\rm time[Myr]}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm \sigma_{cl}(km.s^{-1})}$', fontsize = 120, color='black')
ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)
ax1.tick_params('both', length=25, width=1, which='minor')
plt.legend(fancybox=True, shadow=True, fontsize=80,loc='upper left')
plt.tight_layout()
plt.savefig('sigma.pdf')
