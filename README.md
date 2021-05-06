## data-analysis-AMUSE 

This reposatory contains the codes to read the big data output from [AMUSEingBlackHole](https://github.com/arpan-das-astrophysics/AMUSEingBlackHole) and [GoneWithTheWind](https://github.com/arpan-das-astrophysics/GoneWithTheWind) codes. 
---
### Packages:
* numpy
* scipy
* astropy
* matplotlib
* pandas
---
#### File details:
* average.py - average accretion rate
* mass.py - evolution of the gas mass and stellar mass
* mmax.py - evolution of the black hole seed 
* ncol.py - evolution of the number of collisions
* collision.py - effect of mass loss due to collision
* coredensity.py - evolution of density of the core of the cluster
* coreradius.py - evolution of the radius of the core of the cluster
* energy.py- evolution of different energy input and output in the cluster
* lagrange.py - evolution of the lagrange radii of the cluster
* maxacc.py - maximum accretion rate
* sigma.py - evolution of the dispersion
* timescaleratio.py - evolution of the ratio of accretion and collision timescale
---

The codes could be run individually by using:
```Python
python filename.py
```
or they could be run alltogether using:
```Python
python batch.py
```
