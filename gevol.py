#!/usr/bin/env python
from pygsl import rng 

rng=rng.rng()
#print rng.name()
i=0	
SEED=987654321-i
mu=rng.set(SEED)

LH=100 #Host lenght
LP=10  #Initial Pathogen Length
LF={}

for i in range (0,100):
	y=1+rng.uniform_int(1000)
	print y
	
	



