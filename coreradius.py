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
Nencl=np.array(df['Nenc'])
Ncol=np.array(df['Ncol'])
Mstar=np.array(df['M_star[MSun]'])/1.e+5
Mgas=np.array(df['M_gas[MSun]'])/1.e+5
Mmax=np.array(df['M_max[MSun]'])#/1.e+4



potential_star_gas=np.array(df['potential_star_gas'])
kineticstar=np.array(df['kineticstar'])
potentialstar=np.array(df['potentialstar'])
dEkacc=np.array(df['dEkacc'])
dEpacc=np.array(df['dEpacc'])
dEgasacc=np.array(df['dEgasacc'])
dEkcoll=np.array(df['dEkcoll'])
dEpcoll=np.array(df['dEpcoll'])
dEgascoll=np.array(df['dEgascoll'])
lagrange10=np.array(df['lagrange10'])
lagrange50=np.array(df['lagrange50'])
lagrange90=np.array(df['lagrange90'])
rcore=np.array(df['radiuscore'])
densitycore=np.array(df['densitycore'])


df1=pandas.read_pickle('properties.csv')
mass=np.array(df1['mass'])


numberofstars=[]
for i in range(len(mass)):
	numberofstars.append(len(mass[i]))

numberofstars=np.array(numberofstars,dtype=float)
escapers=(numberofstars-Nencl)
print Nencl
# escapers=np.diff(escapers,prepend=0)
# for i in range(len(escapers)):
# 	if escapers[i]<0.:
# 		escapers[i]=0.

# virial=2*kinetic+potential+potentialgas
total=kineticstar+potentialstar+potential_star_gas+dEkcoll+dEpcoll#+dEgascoll#+dEkacc+dEpacc+dEgasacc
fig1=plt.figure(dpi=72,figsize=(35, 31))
ax1= fig1.add_subplot(111)

# plt.plot(time,Mgas, linewidth=12, color='red', linestyle = '-', label=r'${\rm Gas\, Mass}$')
# plt.plot(time,Mstar, linewidth=12, color='blue', linestyle = '-', label=r'${\rm Star\, Mass}$')
#plt.plot(time,Mmax, linewidth=12, color='blue', linestyle = '-')

#plt.plot(time,Ncol, linewidth=12, color='blue', linestyle = '-')
#plt.plot(time,Nencl, linewidth=12, color='blue', linestyle = '-')
#plt.plot(time, escapers/numberofstars, linewidth=12, color='black', linestyle = '-')

#plt.plot(time,lagrange50, linewidth=12, color='blue', linestyle = '-')
#plt.plot(time,lagrange10, linewidth=12, color='blue', linestyle = '-')
#plt.plot(time, lagrange90, linewidth=12, color='blue', linestyle = '-')
plt.plot(time, rcore, linewidth=12, color='blue', linestyle = '-')
#plt.plot(time, densitycore, linewidth=12, color='blue', linestyle = '-')

# plt.plot(time,kineticstar/1.e+45, linewidth=12, color='red', linestyle = '-', label=r'${\rm KE}$')
# plt.plot(time,potentialstar/1.e+45, linewidth=12, color='blue', linestyle = '-', label=r'${\rm PE}$')
# plt.plot(time,potential_star_gas/1.e+45, linewidth=12, color='green', linestyle = '-', label=r'${\rm PE_{gas}}$')
# plt.plot(time,total/1.e+45, linewidth=12, color='black', linestyle = '-', label=r'${\rm Total}$')

# plt.plot(time,totalkinetic, linewidth=12, color='red', linestyle = '-', label=r'${\rm KE}$')
# plt.plot(time,totalpotential, linewidth=12, color='blue', linestyle = '-', label=r'${\rm PE}$')
# plt.plot(time,totalcluster, linewidth=12, color='black', linestyle = '-', label=r'${\rm Total}$')
# plt.plot(time,virialtotal, linewidth=12, color='brown', linestyle = '-', label=r'${\rm 2\times E_K+E_p}$')


#plt.plot(time,dE/total, linewidth=12, color='black', linestyle = '-', label=r'${\rm Total}$')
#plt.plot(time, Q, linewidth=12, color='black', linestyle = '-', label=r'${\rm Total}$')




#ax1.set_yscale("log")
#ax1.set_xscale("log")
#ax1.set_ylim(-0.5,0.5)
ax1.set_xlim(0,1)
ax1.xaxis.set_label_text(r'$ {\rm time[Myr]}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm dE_{total}/E_{total}}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm Mass[10^5 M_\odot]}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm Number\,of\,collisions}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm M_{max}(10^4M_\odot)}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm Half-Mass\, Radius[pc]}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm 10\%\,Lagrange\,Radius[pc]}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm 90\%\,Lagrange\,Radius[pc]}$', fontsize = 120, color='black')
ax1.yaxis.set_label_text(r'${\rm Core\,Radius[pc]}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm Core\,Density[kg/pc^{-3}]}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm Energy(10^{45} J)}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm Number\, of\, escapers}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm N_{esc}/N_{total}}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm \sigma(km.s^{-1})}$', fontsize = 120, color='black')
#ax1.yaxis.set_label_text(r'${\rm Number\, of\, Stars}$', fontsize = 120, color='black')

#ax1.text(0.04, 200, r'${\rm M_{init}=0.1M_\odot}$',fontsize=80)
#ax1.text(0.05, 1, r'${\rm M_{init}=0.1M_\odot}$',fontsize=80)
ax1.tick_params('both', labelsize=90, length=40, width=3, which='major',pad=40)
#ax1.tick_params('both', length=25, width=1, which='minor')
#ax1.set_xticks([0.1,1,10])
#ax1.set_yticks([1.e+51,2.e+51])
#ax1.get_xaxis().get_major_formatter()
#ax1.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
#ax1.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0e'))
#ax1.get_yaxis().get_major_formatter()

#f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
#g = lambda x,pos : "${}$".format(f._formatSciNotation('%1.10e' % x))
#plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))

#plt.legend(fancybox=True, shadow=True, fontsize=70,loc='center right')
plt.tight_layout()
plt.savefig('rcore.pdf')
