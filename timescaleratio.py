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

df1=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/plot/constant.csv')
df2=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/plot/eddington.csv')
df3=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/plot/bondi.csv')


time1=np.array(df1['t[Myr]'])
time2=np.array(df2['t[Myr]'])
time3=np.array(df3['t[Myr]'])

ratio1=np.array(df1['ratio'])
ratio2=np.array(df2['ratio'])
ratio3=np.array(df3['ratio'])



fig1=plt.figure(dpi=72,figsize=(35, 31))
ax1= fig1.add_subplot(111)



plt.plot(time1, ratio1, linewidth=12, color='blue', linestyle = '-',label=r'${\rm 10^{-5}\,M_\odot/yr}$')
plt.plot(time2, ratio2, linewidth=12, color='green', linestyle = '-',label=r'${\rm \dot{m}_{Edd}}$')
plt.plot(time3, ratio3, linewidth=12, color='red', linestyle = '-',label=r'${\rm \dot{m}_{BH}}$')




ax1.set_yscale("log")
#ax1.set_xscale("log")                                                                                                                                                                                      
ax1.set_xlim(0,5)
#ax1.set_ylim(1.e-2,1.0)
ax1.xaxis.set_label_text(r'$ {\rm time[Myr]}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm t_{coll}/t_{acc}}$', fontsize = 120, color='black')

ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)
ax1.tick_params('both', length=25, width=1, which='minor')

plt.legend(fancybox=True, shadow=True, fontsize=70,loc='upper left')
plt.tight_layout()
plt.savefig('ratio.pdf')
