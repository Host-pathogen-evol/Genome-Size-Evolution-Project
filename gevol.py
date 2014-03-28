#!/usr/bin/env python
from pygsl import rng 
import math as mth

rng=rng.rng()
#print rng.name()
i=0	
SEED=987654321-i
mu=rng.set(SEED)

LH=100 #Mean number of hosts lengths.
VHT=50 #SIGMA.

#Generate N hosts 
N=1000 #Number of hosts/jumps
lhh=[]

#initial pathohen  initial population
Np=1

for i in range(0,N):	
	#z=LH+rng.gaussian(VHT) #variable version gaussian
	z=LH #fixed version	
	
print lhh
print len(lhh)
raw_input()

#LP=1 #Initial Pathogen units.
#LF={}

#for i in range (0,100):
#	y=1+rng.uniform_int(1000)
#	print y
def newhost(Lh):
	nhx={}
	att=[]
	for i in range (0,Lh):
		att.append('')