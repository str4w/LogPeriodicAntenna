LogPeriodicAntenna
==================

Small program to work out the positions of the arms on a log-periodic antenna based on description of logperiodic antenna here.
http://www.antenna-theory.com/antennas/wideband/log-periodic-dipole.php

Given the starting element size, the distance from the first to the second element, the expansion factor k, and the number of elements, it is possible to work out the length and placement of all elements.  The last number in the list is the frequency in MHz for which the dipole is a half wavelength.  This frequency is calculated using the speed of light in a vacuum, no velocity factor is applied. 

 
     Usage: logperiodic.py l_1 d_1 k N
            where: l_1 is length of first element in cm
                   d_1 is distance from first element to second in cm
                   k   is ratio between successive lengths and distances
                   N   is the number of elements
     
     rupert@morrigan:~/development/antenna$ ./logperiodic.py 12 4.8 1.13 12
     Computing parameters for a log periodic dipole antenna
     0: 12.000000 cm ( 4.724409 ) in  :  0.000000 cm ( 0.000000 ) in  :  0.000000 cm ( 0.000000 ) in  :  1250.0
     1: 13.560000 cm ( 5.338583 ) in  :  4.800000 cm ( 1.889764 ) in  :  4.800000 cm ( 1.889764 ) in  :  1106.19469027
     2: 15.322800 cm ( 6.032598 ) in  :  10.224000 cm ( 4.025197 ) in  :  5.424000 cm ( 2.135433 ) in  :  978.933354217
     3: 17.314764 cm ( 6.816836 ) in  :  16.353120 cm ( 6.438236 ) in  :  6.129120 cm ( 2.413039 ) in  :  866.312702847
     4: 19.565683 cm ( 7.703025 ) in  :  23.279026 cm ( 9.164971 ) in  :  6.925906 cm ( 2.726734 ) in  :  766.648409599
     5: 22.109222 cm ( 8.704418 ) in  :  31.105299 cm ( 12.246181 ) in  :  7.826273 cm ( 3.081210 ) in  :  678.449919999
     6: 24.983421 cm ( 9.835993 ) in  :  39.948988 cm ( 15.727948 ) in  :  8.843689 cm ( 3.481767 ) in  :  600.398159291
     7: 28.231266 cm ( 11.114672 ) in  :  49.942356 cm ( 19.662345 ) in  :  9.993368 cm ( 3.934397 ) in  :  531.325804683
     8: 31.901330 cm ( 12.559579 ) in  :  61.234863 cm ( 24.108214 ) in  :  11.292506 cm ( 4.445869 ) in  :  470.199827153
     9: 36.048503 cm ( 14.192324 ) in  :  73.995395 cm ( 29.132045 ) in  :  12.760532 cm ( 5.023832 ) in  :  416.106041728
     10: 40.734809 cm ( 16.037326 ) in  :  88.414796 cm ( 34.808975 ) in  :  14.419401 cm ( 5.676930 ) in  :  368.235435158
     11: 46.030334 cm ( 18.122179 ) in  :  104.708719 cm ( 41.223905 ) in  :  16.293923 cm ( 6.414931 ) in  :  325.872066511
     
     Total Dipole Material Length Required: 307.802132325

