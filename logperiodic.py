#!/usr/bin/python
import sys

def cmAndInches(v):
   return "%f cm ( %f ) in"%(v,v/2.54)

def main(l_1,d_1,k,N):
   print "Computing parameters for a log periodic dipole antenna"
   theLengths   =[l_1*(k**i) for i in range(N)]
   theIndividualDistances=[0]+[d_1*(k**i) for i in range(N-1)]
   theDistances =[sum(theIndividualDistances[:(i+1)]) for i in range(N)]
   for i in range(N):
      print "%d:"%i,cmAndInches(theLengths[i])," : ",cmAndInches(theDistances[i]), " : ",cmAndInches(theIndividualDistances[i]), " : ", 15000./theLengths[i]
   print "\nTotal Dipole Material Length Required:",sum(theLengths)

if __name__ == "__main__":
   if(len(sys.argv) != 5):
      print """
Usage: logperiodic.py l_1 d_1 k N
       where: l_1 is length of first element in cm
              d_1 is distance from first element to second in cm
              k   is ratio between successive lengths and distances
              N   is the number of elements
"""
   else:
      main(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),int(sys.argv[4]))
       
