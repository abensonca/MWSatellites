# Milky Way Satellites Star Formation Histories Project: Strategy #

## Goals ##

* Determine what constraints Milky Way satellite star formation histories places on the physics controlling satellite formation/evolution

## Plan ##

*Italics* indicate steps that we could work on immediately.

1. Calibration
   1. Find a viable SAM (with minimal environmental physics) constrained to match some set of data on the global galaxy population
   2. Find a viable SAM (with minimal environmental physics) which also matches Local Group constraints:
      * Cumulative stellar mass function;
      * *Metallicities?*
   3. *Calibrate SAM subhalo orbital model to N-body simulation data*
	  * *Which simulations should we use?*
   4. Calibrate SAM ram pressure model(s) to hydro simulation data
2. Physics testing
   1. *Extract star formation histories from SAM and define some quantitative measure of how well they match observed histories*
   2. Repeat SAM calibration adding in additional physical processes
      1. Ram pressure stripping of hot atmosphere;
      2. Ram pressure stripping of disk ISM;
      3. Pressure-modulated star formation rates?

## Potential Problems ##

* Hydro simulations of ram pressure stripping of satellites are proving difficult to set up with stable initial conditions
* The speed of Galacticus makes it currently **very** time consuming to do full MCMC for all of these cases
    * This will get worse if we want to track full orbital evolution
    * Possible solutions:
        * Develop approximations which allow it to run sufficiently fast (without degrading the accuracy of the results too badly?)
    	* Use Yu Lu's SAM which is faster but does not incorporate the same treatment of orbits or ram pressure stripping (yet)
        * Don't do full MCMC 

