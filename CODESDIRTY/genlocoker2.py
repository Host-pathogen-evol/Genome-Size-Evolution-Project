#!/usr/bin/env python
from pygsl import rng as rn
import math as mth
import numpy as np
import TwoSpeedMods as hpm
#######################
#Parameters
SEED=987654320 #RNG SEED
rk=rn.rng()
rk.set(SEED)
K1=100 #EFFECTORS "NEUTRAL" NETWORK SIZE
K=500#INTERACTION URN SIZE
Cn=0.5 #VIRULENCE INDEX
hio=5  #Initial Number of units in pathogens genome
Nhi=1  #Initial Pathogen's populations
PTH={} #Pathogen's dictionary
#Rate constants
mu1=0.000001#mutation rate effectors
mu2=0.000001#mutation rate repeats
mu3=0.000001#removal rate
#mu4=0.99#transversal gene rate gain
RT=[mu1,mu2,mu3]#,mu4]
#Len parameters taken from fasta file p.infestans
muln=np.log(1177.42231142)
sigmaln=0.702693602048
LNLEN=[muln,sigmaln]
#print LNLEN
#########################################################
####INITIAL VALUES ETC
A1=1.0 #W strenght parameter
Lh=20 #HOST LENGTH Lh<<K CHECK THIS ALWAYS!!!!
Neff=3 #INITIAL NUMBER OF EFFECTORS
Ncodgnes=3 #NUMBER OF TRANSPOSONS (ADD LENGHT AND MAY BE OF SOME USE)
Nncod=3
PRTMS=[Lh*Cn,muln]
Wn=0.0
while Wn<1.0:
  H=hpm.NEWHOST(Lh,K,rk)
  print("INITIAL HOST")
  print H
  HP=hpm.HPMATRIX(K1,K,Cn,rk) #Effector interaction list
  ni=1+rk.uniform_int(K1)
  li=np.random.lognormal(mean=LNLEN[0],sigma=LNLEN[1],size=1)[0] #length
#Creates a non repeated array to label the effectors
  elb=[]
  elb.append(ni)
  i=1
  while i<Neff:
    ni=1+rk.uniform_int(K1)
    jk=0
    for si in elb:
      if si==ni:
        jk=1
      if jk==0:
        elb.append(ni)
      i=i+1
    #raw_input()
  gp={}
  n=0
  for i in elb:
    gp[n]=hpm.NEWPATHOGENUNIT(i,rk,LNLEN)
    n=n+1
#print gp
#############################################################################


  gp2=hpm.INIASSEMBLE(gp,H,HP,rk)
  Wi=hpm.GETWI(gp2)
  wl=len(Wi)
  Wo=(sum(Wi)/(Cn*Lh*wl))
  Wn=mth.exp(Wo)-1.0
  print Wn
raw_input()
Gr={}
Nr={}
Wr={}
Wi=[]
Nr[0]=10000.0
Gr[0]=gp2
Wr[0]=Wn
del gp2, Wi, wl, Wo
#print("Initial Pathoghen:")
print Wn
#hpm.prtgenomes(Gr[0])
print("Initial Setup Done")
#*********************************************************
raw_input()
JMPNUM=0
#for taun in range(JMPNUM):
muk=0
Nt=Nr[0]
while muk==0:
  lk=rk.uniform_pos()
  Lo=hpm.GETGENOMELENGTH(Gr[0])
  Tr=hpm.reactions(RT,Gr[0],Nr[0],Lo,PRTMS,rk)
  alpha=hpm.GETALPHARATE(Tr)
  tnr=(1.0/alpha)*mth.log(1.0/lk)
  nrpair=hpm.WHICHREACTION(alpha,Tr,rk)
  print alpha, tnr
  print nrpair
  if tnr<Nt:
    break
  Nt=Wn*Nt
  print("New Pop")
  print Nt
  raw_input()

#raw_input()
print("**********************************************")
for i in Gr[0].keys():
  for j in range(3):
    print("gene:%d reaction:%d"%(i,j))
    gkx=hpm.TRANSFORMATIONS(i,j,Gr[0],H,rk)
    print("SUMMARY\n")
    print("***************************\n")
    print Gr[0]
    print gkx
    print("****************************")
    print("CARRY ON")
    raw_input()


###JUMP!
HSTS={}
HSTS[0]=H
H1=hpm.NEWHOST(Lh,K,rk)
HSTS[1]=H1
print H
print H1

grn=hpm.JUMP(Gr[0],H1,HP,rk)
print grn
