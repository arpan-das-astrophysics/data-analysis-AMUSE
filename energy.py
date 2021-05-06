from scipy.interpolate import interp1d
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import scipy
from scipy.stats import norm
import pandas
import matplotlib.ticker as mticker
from scipy import interpolate

df=pandas.read_pickle('output.csv')

time=np.array(df['t[Myr]'])

potential_star_gas=np.array(df['potential_star_gas'])
kineticstar=np.array(df['kineticstar'])
potentialstar=np.array(df['potentialstar'])
#selfgravity=np.array(df['selfgravity'])

dEkacc=np.array(df['dEkacc'])
dEpacc=np.array(df['dEpacc'])
dEgasacc=np.array(df['dEgasacc'])
dEkcoll=np.array(df['dEkcoll'])
dEpcoll=np.array(df['dEpcoll'])
dEgascoll=np.array(df['dEgascoll'])


virial=abs(kineticstar/(potentialstar+potential_star_gas))


#dE=dEkcoll+dEpcoll
total=kineticstar+potentialstar+potential_star_gas
dE=np.cumsum(np.diff(total))
dE=np.insert(dE,0,0)
totalnew=total-dE

fig1=plt.figure(dpi=72,figsize=(35, 31))
ax1= fig1.add_subplot(111)

plt.plot(time,kineticstar/1.e+45, linewidth=12, color='red', linestyle = '-', label=r'${\rm KE}$')
plt.plot(time,potentialstar/1.e+45, linewidth=12, color='blue', linestyle = '-', label=r'${\rm PE}$')
plt.plot(time,potential_star_gas/1.e+45, linewidth=12, color='green', linestyle = '-', label=r'${\rm PE_{\phi}}$')
plt.plot(time,total/1.e+45, linewidth=12, color='black', linestyle = '-', label=r'${\rm Total}$')
plt.plot(time,totalnew/1.e+45, linewidth=12, color='black', linestyle = '--', label=r'${\rm Total+dE}$')
#plt.plot(time,virial, linewidth=12, color='brown', linestyle = '-', label=r'${\rm Virial}$')
#plt.plot(time,np.diff(dE,prepend=0)/total, linewidth=12, color='red', linestyle = '-', label=r'${\rm KE}$')





#ax1.set_yscale("log")
#ax1.set_xscale("log")
#ax1.set_ylim(-0.4,0.3)
ax1.set_xlim(0,5)
ax1.xaxis.set_label_text(r'$ {\rm time[Myr]}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm Cluster\, Energy(10^{45} J)}$', fontsize = 120, color='black')

ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)


plt.legend(fancybox=True, shadow=True, fontsize=70,loc='lower left')
plt.tight_layout()
plt.savefig('energy.pdf')
