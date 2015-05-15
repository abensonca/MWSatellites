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

How to formulate our goal:
(AP) I think there are (at least!!!) two different types of strategies.  First, we could try to model individual galaxies.  E.g., with which set of physics could you get a satellite with the orbit and SFH of Carina.  Each galaxy would have a multidimensional posterior.  The posteriors of the galaxies (both satellite and field objects) could be multiplied together for a population-driven model for star formation.  Second, we can do realizations of Milky Way systems and see under which circumstances we get something that looks like ours.  The advantage of the former is that we can worry only about one galaxy at a time.  Getting the Milky Way exactly right (I want a Carina and a Segue I but not a NGC 205) is hard, and probably not a good strategy.  However, we'll probably have to generate a ton of merger trees with different physics for this.  I am not sure on first glace how to come up with a "goodness of fit" metric for this.  The advantage of the latter is that it is closer to what's currently done.  The problem is that the Local Group is a sample of one.

Bits of physics that need to be thought about:
'---RPS
---Something to model SN/radiative feedback
---orbits of satellites
---star-formation criterion
---figure out how to code physics into something appropriate for a SAM.
---how much to play with the mass of the Milky Way?  How much do we need to worry about the build-up of the stellar disk and gas halo?  How would we model the gas halos as a function of time?

Considerations
---what can we get out of existing simulations vs. simulations we need to run?"'
---which packages already exist in Galacticus?  Can we identify which ones need tweaking?  Which things need to be added?
---can we split the workload in terms of physics modules?