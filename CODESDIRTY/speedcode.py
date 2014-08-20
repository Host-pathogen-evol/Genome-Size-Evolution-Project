#!/usr/bin/env python

def getgenesl(Lg):
	#print Lg
	Gn={}
	Gnx={}
	Gnx[0]=[0]
	Gnx[1]=[1]
	#print("zero set")
	#print Gnx
	#raw_input()

	for z in range(1,Lg):
		#print("iteration:%d"%z)
		mu=1
		for i in range(2):
			ng=[]
			ng.append(i)
			for j in Gnx.keys():
				nugene=[]
				nugene=ng+Gnx[j]
				Gn[mu]=nugene
				mu=mu+1
		print Gn
		Gnx={}
		Gnx=Gn
		if(z<(Lg-1)):
			Gn={}

		#raw_input()
	#print Gn
	return Gn

def prteffset(EFFNODES):
	for j in EFFNODES.keys():
		print("%s %s\n"%(j,EFFNODES[j]))

def effgendist(S1,S2):
	import numpy as np
	assert len(S1) == len(S2)
	return np.sum(S1 != S2)
