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

df0=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/constant1.e-5/output.csv')
# df1=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/collision/constantcollision/output.csv')
# df2=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/collision/constantcollision0.3/output.csv')
# df3=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/collision/constantcollision0.5/output.csv')

# #df0=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/constant1.e-5/output.csv')
# #df1=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/collision/constantcollision/output.csv')
# #df2=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/collision/constantcollision0.5/output.csv')

# #df0=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/constant1.e-5/output.csv')
# #df1=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/collision/constantcollision/output.csv')
# #df2=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/collision/constantcollision0.5/output.csv')

time0=np.array(df0['t[Myr]'])
Mmax0=np.array(df0['M_max[MSun]'])


# time1=np.array(df1['t[Myr]'])
# Mmax1=np.array(df1['M_max[MSun]'])

# time2=np.array(df2['t[Myr]'])
# Mmax2=np.array(df2['M_max[MSun]'])

# time3=np.array(df3['t[Myr]'])
# Mmax3=np.array(df3['M_max[MSun]'])

fig1=plt.figure(dpi=72,figsize=(35, 31))
ax1= fig1.add_subplot(111)

plt.plot(time0,Mmax0, linewidth=12, color='blue', linestyle = '-', label=r'${\rm No\, Mass\, Loss}$')
# plt.plot(time1,Mmax1, linewidth=12, color='red', linestyle = '-', label=r'${\rm Katz\,et\,al.\,2015}$')
# plt.plot(time2,Mmax2, linewidth=12, color='green', linestyle = '-', label=r'${\rm 3\%\,Mass\,Loss}$')
# plt.plot(time3,Mmax3, linewidth=12, color='orange', linestyle = '-', label=r'${\rm 5\%\,Mass\,Loss}$')
#plt.plot(time0,Mmax0, linewidth=12, color='blue', linestyle = '-', label=r'${\rm 1.0\, pc}$')
#plt.plot(time3,Mmax3, linewidth=12, color='darkorange', linestyle = '-', label=r'${\rm 2.0\, pc}$')
#plt.plot(time4,Mmax4, linewidth=12, color='purple', linestyle = '-', label=r'${\rm 5.0\, pc}$')

plt.title(r'${\rm \dot{m}=10^{-5} \, M_\odot/yr}$',fontsize = 80, pad=30)
ax1.set_yscale("log")
ax1.set_xlim(0,5)
ax1.set_ylim(80,1.e+6)
ax1.xaxis.set_label_text(r'$ {\rm time[Myr]}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm M_{max}(M_\odot)}$', fontsize = 120, color='black')
ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)
ax1.tick_params('both', length=25, width=1, which='minor')
plt.legend(fancybox=True, shadow=True, fontsize=70,loc='upper left')
plt.tight_layout()
plt.savefig('constant.pdf')
