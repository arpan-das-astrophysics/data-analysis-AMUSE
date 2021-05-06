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

df=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/eddington/properties.csv')
df0=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/eddington/output.csv')

df1=pandas.read_pickle('/home/adas45/scratch/bondicollision/properties.csv')
df2=pandas.read_pickle('/home/adas45/scratch/bondicollision/output.csv')

df3=pandas.read_pickle('/home/adas45/properties.csv')
df4=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/imfbondi/output.csv')

time=np.array(df0['t[Myr]'])
mdot=np.array(df['mdot'])

time1=np.array(df2['t[Myr]'])
mdot1=np.array(df1['mdot'])

time2=np.array(df4['t[Myr]'])
mdot2=np.array(df3['mdot'])
mass=np.array(df3['mass'])


maxedd=[]
avgedd=[]
for i in range(len(mdot)):
    maxedd.append(np.amax(mdot[i]))
    avg=np.sum(mdot[i])/len(mdot[i])
    avgedd.append(avg)
    
maxedd=np.array(maxedd)
avgedd=np.array(avgedd)

maxbondi=[]
avgbondi=[]
for i in range(len(mdot1)):
    maxbondi.append(np.amax(mdot1[i]))
    avg2=np.sum(mdot1[i])/len(mdot1[i])
    avgbondi.append(avg2)
    
maxbondi=np.array(maxbondi)
avgbondi=np.array(avgbondi)

maxbondi2=[]
avgbondi2=[]
for i in range(len(mdot2)):
    maxmass=np.amax(mass[i])*5.02785e-31
    rate=1.e-9*(maxmass**2.0)
    maxbondi2.append(rate)
    rate2=1.e-9*mass[i]*mass[i]*5.02785e-31*5.02785e-31
    avg=np.sum(rate2)/len(rate2)
    avgbondi2.append(avg)
    
maxbondi2=np.array(maxbondi2)
avgbondi2=np.array(avgbondi2)

print(np.amax(maxbondi2))

fig1=plt.figure(dpi=72,figsize=(35, 31))
ax1= fig1.add_subplot(111)
plt.plot(time,avgedd, linewidth=12, color='blue', linestyle = '--',label=r'${\rm (\dot{M}_{edd})_{avg}}$')
plt.plot(time2,avgbondi2, linewidth=12, color='red', linestyle = '--',label=r'${\rm (\dot{M}_{BH})_{avg}}$')
plt.plot(time,maxedd, linewidth=12, color='blue', linestyle = '-',label=r'${\rm (\dot{M}_{edd})_{max}}$')
plt.plot(time2,maxbondi2, linewidth=12, color='red', linestyle = '-',label=r'${\rm (\dot{M}_{BH})_{max}}$')

ax1.set_yscale("log")
#ax1.set_xscale("log")
ax1.set_ylim(1.e-7,100)
ax1.set_xlim(0,5)
ax1.xaxis.set_label_text(r'$ {\rm time[Myr]}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm \dot{M} (M_\odot/yr)}$', fontsize = 120, color='black')
ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)
ax1.tick_params('both', length=25, width=1, which='minor')
plt.legend(fancybox=True, shadow=True, fontsize=100,loc='upper left')
plt.tight_layout()
plt.savefig('average.pdf')
