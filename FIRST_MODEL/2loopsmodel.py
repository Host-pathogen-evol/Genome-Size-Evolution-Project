from math import floor
from pygsl import rng as rn
import gc
import sys
#pth='../'
#sys.path.append(pth)
import Lffit
import os

rxclr=[]
crinckler=[]
tes=[]
pth='../../'
rxclr=Lffit.loaddata(pth+'rxclr.dat')
crinckler=Lffit.loaddata(pth+'crinckler.dat')
tes=Lffit.loaddata(pth+'tes.dat')
print len(rxclr), len(crinckler), len(tes)

#raw_input()

RXCLRPTS=[len(rxclr),min(rxclr),max(rxclr)]
CRKPTS=[len(crinckler),min(crinckler),max(crinckler)]
TES=[len(tes),min(tes),max(tes)]
print RXCLRPTS
print CRKPTS
print TES

import lmainjumps
import pdt
SEED=987654320
nte=5
neff=10
tn=15000

Np=1e6
m1=0.00 #hgt effs
m2=0.01#hgt te
m3=0.1 #m3=0.02 #eff recomb
m4=0.01  #te dup
m5=3.00  #3.5 #10.50 #eff dup+te
m6=0.01 #m6=0.0013  #eff->null
m7=0.0000 #10*1e-5 #null ->0
m8=0.0000 #m8=1.0001##eff->0
kn=0.0
beta1=1e-5
beta2=0.001
wo=1.0

Qi=0.1

po='../'
#dmu=0.5
#muk=8.0
PTHLIST=[]
LTT=[]

for i in range(1):
  #for j in range(1,6):
  nx='n'+str(i)
  LTT.append(nx)
  if not os.path.exists(po+nx):
    os.makedirs(po+nx)

for ch in LTT:
    pth=po+ch
    PTHLIST.append(pth)
    print pth

#raw_input()

print PTHLIST
#raw_input()
JMPS=2

####################
jx=1
jy=1
mo=m6
m5=m5/2.0
m4=2.0*m4
#m7=(5.0*m7)
m3=0.1*0.1*m3
m5=10.0*10.0*m5
####################
for pthk in PTHLIST:
    print pthk

    for n in range(JMPS):

      P=[Np,m1,m2,m3,m4,m5,m6,m7,m8,beta1,beta2,wo]

    ############
      if n==0:
        gold={}
      else:
        del gold
        gold={}
        for i in gen.keys():
            gl=[]
            kj=0
            for k in gen[i]:
                kj+=1
                gl.append(k)
                if kj==3:
                    gl[2]=0.0

            gold[i]=gl #[gen[i][0],gen[i][1]]
    ############
        del gen
      gen={}
      lth,ltn,ngt,pqr, gen,info,wfitn,trns =  lmainjumps.job(P,SEED,neff, nte,tn, RXCLRPTS, CRKPTS, TES, n, gold,Qi)
      efflens, telens =Lffit.splitgen(gen)
      print len(efflens), len(telens)
      pthl=pthk
   # pdt.savedata(lth,ltn,ngt,efflens,telens,P,SEED,pthl,wfitn)
      if telens or efflens:
        pdt.savedata(lth,ltn,ngt,efflens,telens,P,SEED,pthl,wfitn,trns)
        if telens and efflens:
          pdt.datadisplay(lth,ltn,ngt,efflens,telens,500,50,P,SEED,pthl,wfitn)
          del lth,ltn,ngt,pqr,info,wfitn,trns
          gc.collect()
      else:
        print("NOT-DATA-TO-SHOW")
      gc.collect()

      print("CARRY ON")
    del gen, gold
    gen={}
    #gc={}
    gold={}
    gc.collect()
    m3=0.1*m3
    m5=10.0*m5

    #import sys
    sys.modules[__name__].__dict__.clear()
    print("bye")
    raw_input()
    #Qi+=0.1
    #m8=10.0*m8
