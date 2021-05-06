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

df1=pandas.read_pickle('/home/adas45/properties.csv')
df2=pandas.read_pickle('/home/adas45/projects/def-basu/adas45/results/imfbondi/output.csv')

time=np.array(df0['t[Myr]'])
mdot=np.array(df['mdot'])

time1=np.array(df2['t[Myr]'])
mdot1=np.array(df1['mdot'])
mass=np.array(df1['mass'])

maxedd=[]
eddavg=[]
for i in range(len(mdot)):
    maxedd.append(np.amax(mdot[i]))
    avg=np.sum(mdot[i])/len(mdot[i])
    eddavg.append(avg)

maxedd=np.array(maxedd)
eddavg=np.array(eddavg)
print(eddavg)


maxbondi=[]
bondiavg=[]
for i in range(len(mdot1)):
    maxmass=np.amax(mass[i])*5.02785e-31
    rate=math.pow(5000,0.6)*1.e-9*maxmass
    maxbondi.append(rate)
    avg2=np.sum(mdot1[i])/len(mdot1[i])
    bondiavg.append(avg2)
    
maxbondi=np.array(maxbondi)
bondiavg=np.array(bondiavg)

fig1=plt.figure(dpi=72,figsize=(35, 31))
ax1= fig1.add_subplot(111)
plt.plot(time,eddavg, linewidth=12, color='blue', linestyle = '-',label=r'${\rm Eddington}$')
plt.plot(time1,bondiavg, linewidth=12, color='red', linestyle = '-',label=r'${\rm Bondi-Hoyle}$')
ax1.set_yscale("log")
#ax1.set_xscale("log")
#ax1.set_ylim(10,100)
ax1.set_xlim(0,5)
ax1.xaxis.set_label_text(r'$ {\rm time[Myr]}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm \dot{M}_{avg}\, (M_\odot/yr)}$', fontsize = 120, color='black')
ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)
ax1.tick_params('both', length=25, width=1, which='minor')
plt.legend(fancybox=True, shadow=True, fontsize=60,loc='upper left')
plt.tight_layout()
plt.savefig('average.pdf')
