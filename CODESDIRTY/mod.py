#!/usr/bin/env python
from pygsl import rng as rn
import math as mth
import numpy as np
import hpmodule as hpm

#######################
#Parameters
SEED=987654320 #RNG SEED
rk=rn.rng()
rk.set(SEED)
K1=100 #EFFECTORS "NEUTRAL" NETWORK SIZE
K=1000#INTERACTION URN SIZE
Cn=0.5 #VIRULENCE INDEX
hio=5  #Initial Number of units in pathogens genome
Nhi=1  #Initial Pathogen's populations
PTH={} #Pathogen's dictionary
#lr=100 #Units length upper bound

#Rate constants
mu1=0.000001#mutation rate effectors
mu2=0.95#fraction of neutral mutations effectors
mu3=0.000001#mutation rate coding
mu4=0.99#fraction of neutral mutations coding
mu5=0.5*(1177.42231142)#selective advantage of removing lengths of noncoding regions
mu6=0.0000001 #repetitive parameter
RT=[mu1,mu2,mu3,mu4,mu5,mu6]

#Len parameters taken from fasta file p.infestans
muln=np.log(1177.42231142)
sigmaln=0.702693602048
LNLEN=[muln,sigmaln]
print LNLEN
#raw_input()
#print RT
################
HP=hpm.HPMATRIX(K1,K,Cn,rk) #Effector interaction list
#hpm.prtmat(HP)
#gplen=hpm.PMINLENS(K1,LNLEN,rk) #Initial lengths vector
#print gplen
#raw_input()
PTH=hpm.INIPATHGEN(hio,K1,rk,LNLEN)
#hpm.prtmat(HP)
#print("sampling from a dist obtained from a fasta file of p.infestans")
#muln=np.log(1177.42231142)
#sigmaln=0.702693602048
#Lo=np.random.lognormal(mean=muln, sigma=sigmaln, size=1)
#print Lo
#print("here we are!")
#raw_input()
print PTH
print("RET TO GLEN")
raw_input()
GNL=hpm.GETGENOMELENGTH(PTH)
print GNL
raw_input()

Lh=100 #HOST LENGTH
H=hpm.NEWHOST(Lh,K,rk)
print H

Wi=hpm.HPINTERACTION(H,PTH,HP)
Awi=hpm.HPSCORES(H,PTH,HP,Cn)
print Wi
print ("Coding units:%f\n"%Awi[0])
print ("NON-Coding units:%f\n"%Awi[1])
print ("Effector units:%f\n"%Awi[2])
print ("HOST UNITS:%f\n"%Awi[3])
print ("PREDAVW:%f\n"%Awi[4])
raw_input()
GEN={}

Gn1=hpm.reactions(PTH,RT,rk,Wi,HP,H,Cn)
print Gn1
   
    
