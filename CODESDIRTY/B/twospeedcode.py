#!/usr/bin/env python
from pygsl import rng as rn
import math as mth
import numpy as np
import TwoSpeedMods as hpm
import pickle
#######################
#Parameters
SEED=987654321 #RNG SEED
rk=rn.rng()
rk.set(SEED)
K1=100 #EFFECTORS "NEUTRAL" NETWORK SIZE
K=500#INTERACTION URN SIZE
Cn=0.75 #VIRULENCE INDEX
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
Lh=5 #HOST LENGTH Lh<<K CHECK THIS ALWAYS!!!!
Neff=3 #INITIAL NUMBER OF EFFECTORS
Ncodgnes=0 #NUMBER OF TRANSPOSONS (ADD LENGHT AND MAY BE OF SOME USE)
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
  print gp2
#raw_input()
Gr={}
Nr={}
Wr={}
Lr={}
Wi=[]
Nr[0]=10000.0
Gr[0]=gp2
Wr[0]=Wn
Lr[0]=hpm.GETGENOMELENGTH(Gr[0])
del gp2, Wi, wl, Wo
#print("Initial Pathoghen:")
print Wn
#hpm.prtgenomes(Gr[0])
print("Initial Setup Done")
#*********************************************************
#raw_input()
JMPNUM=10
#for taun in range(JMPNUM):
#muk=0
#Nt=Nr[0]
#AVW=[]
#AVN=[]
#AVL=[]
HSTS={}
#HSTS[0]=H
over=0
for jn in range(JMPNUM):
  HSTS[jn]=H
  for ngen in range(500):
    print jn, ngen
    for n in Nr.keys():
      wmax=max(Wr.values())
      Nt=Nr[n]
      Wn=Wr[n]
      lk=rk.uniform_pos()
      Lo=Lr[n] #
      Tr=hpm.reactions(RT,Gr[n],Nr[n],Lo,PRTMS,rk)
      alpha=hpm.GETALPHARATE(Tr)
      tnr=(1.0/alpha)*mth.log(1.0/lk)
      #print ngen
      #print tnr
      #print Nt
      #print alpha
      if tnr<Nt:
        #print("THERE IS SOMETHING AGAINST YOU")
        #raw_input()
        nrpair=hpm.WHICHREACTION(alpha,Tr,rk)
        i=nrpair[0]
        j=nrpair[1]
        gkx=hpm.TRANSFORMATIONS(i,j,Gr[n],H,rk)
        Wi=hpm.GETWI(gkx)
        wl=len(Wi)
        Wo=(sum(Wi)/(Cn*Lh*wl))
        Wn=mth.exp(Wo)-1.0
        if (Wn>wmax):
          lm=len(Nr.keys())
          #print lm
        #Nr[n]=Nt-1.0
          Nr[lm]=1.0
          Wr[lm]=Wn
          Gr[lm]=gkx
          Lr[lm]=hpm.GETGENOMELENGTH(gkx)
          #Nt=Nt-1.0
          wmax=Wn
        #raw_input()
      Nr[n]=Wn*Nt
    extinct=[]
    for n1 in Nr.keys():
      if Nr[n1]<1.0:
        extinct.append(n1)
    if len(extinct)<len(Nr.keys()):
      for i in extinct:
        del Nr[i]
        del Wr[i]
        del Lr[i]
        del Gr[i]
    else:
        print("THE WORLD IS OVER")
        over=1
        break
  if over==1:
   print("BYE-NO MORE JUMPS")
   break
        #print Nr
        #print Wr
      #AVN.append(sum(Nr)/len(Nr))
      #AVW.append(sum(Wr)/len(Wr))
      #AVL.append(sum(Lr)/len(Lr))

  spops="data/PopsJMP"+str(jn)+".p"
  slens="data/LenJMP"+str(jn)+".p"
  swns="data/RatesJMP"+str(jn)+".p"
  sgens="data/GenesJMP"+str(jn)+".p"
  pickle.dump(Nr,open(spops,"wb"))
  pickle.dump(Lr,open(slens,"wb"))
  pickle.dump(Wr,open(swns,"wb"))
  pickle.dump(Gr,open(sgens,"wb"))
  print jn
  #raw_input()
###JUMP!
#CHOOSE SOME RANDOM SUBPOPS AND MIGRATE THEM
  H=hpm.NEWHOST(Lh,K,rk)
  Grx={}
  Lrx={}
  Nrx={}
  Wrx={}
  nGN=len(Gr.keys())
  if(nGN>1):
    print("jump bit")
    for kn in range(1,3):
      print("migrates selection bit")
      qk=3-kn
      print qk
      print("about to jump!")
      print Gr[nGN-qk]
      grn=hpm.JUMP(Gr[nGN-qk],H,HP,rk)
      print("jump performed!")
      #raw_input()
      Grx[kn-1]=grn
      Nrx[kn-1]=1000.0
      Lrx[kn-1]=Lr[kn-1]
      Wi=hpm.GETWI(grn)
      wl=len(Wi)
      Wo=(sum(Wi)/(Cn*Lh*wl))
      Wn=mth.exp(Wo)-1.0
      Wrx[kn-1]=Wn
    Gr={}
    Nr={}
    Wr={}
    Lr={}
    Gr=Grx
    Nr=Nrx
    Wr=Wrx
    Lr=Lrx
    del Grx, Nrx, Wrx
    print("jump completed")
    #raw_input()
  else:
    print("THE END BY EXT")
    break
print("completed")

shosts="data/Hosts.p"
pickle.dump(HSTS,open(shosts,"wb"))
