from math import floor
from pygsl import rng as rn
import sys
import gc
sys.path.append('../LNKMODEL/')
import Lffit
import LffitB
import os


Np=PT[0]
m1=PT[1] #hgt effs
m2=PT[2] #hgt te
m3=PT[3] #eff recomb
m4=PT[4] #te dup
m5=PT[5] #eff dup+te
m6=PT[6]  #eff->null
m7=PT[7] #null ->0
m8=PT[8]  ##eff->0
beta1=PT[9]
beta2=PT[10]
wo=PT[11]
#print("parameter vector:"% PT)
av1=0.5*(RXCLRPTS[2]-RXCLRPTS[1])
av2=0.5*(CRKPTS[2]-CRKPTS[1])
av3=0.5*(TES[2]-TES[1])
Lth=floor((RXCLRPTS[0]+CRKPTS[0]+TES[0])*(1.0/3.0)*(av1+av2+av3))
 #print Lth
MU=[Np,m1,m2,m3,m4,m5,m6,m7,m8,Lth,beta1,beta2,wo]
Qj=Qi
  #SEED=987654320
rk=rn.rng()
rk.set(SEED)

for nj in range(2):
################
  if nj==0:
    gen={}
    trs={}
    gen=Lffit.inigenome(nte,neff,rk,[TES[1],TES[2]],[CRKPTS[1], RXCLRPTS[2]])

    #print gen
    #raw_input()
################
  if nj>0:
    gen={}
    trs={}
    k=0
    for i in gold.keys():
      gl=[]
      if gold[i][0]=='te':
        gl=[gold[i][0],gold[i][1]]
        gen[k]=gl
        k+=1
      if gold[i][0]=='eff':
        qj=rk.uniform_pos()
        snew=gold[i][2]+(0.01*( 1.0-2.0*rk.uniform_pos() ))
        if ((qj>Qj) and (snew>0.0)):
          gl=[gold[i][0],gold[i][1],snew]
        else:
          gl=[gold[i][0],gold[i][1],0.0]
        gen[k]=gl
        k+=1

  #  print gen
  #  raw_input()
################
  Ntot=RXCLRPTS[0]+CRKPTS[0]+TES[0]
  pqr={}
  ltn=[]
  lth=[]
  ngt=[]
  fitn=[]
  trns=[]
  flg='all-good'
  for nk in range(tn):

    trs=Lffit.trates(gen,MU)
    rij,sr =Lffit.montec(trs,rk)
    trns.append(rij)
    if sr!='TRUE':
      pqr[nk]=[rij[0],rij[1],gen]
      ltn.append(Lffit.lent(gen))
      lth.append(Lth)
      #fitn.append(Lffit.ft(gen))
      wq=Lffit.ft(gen)
      fitn.append(1.0-(wq/(wq+wo)))
      ngt.append(len(gen.keys()))
      #del gu
      gu={}
      gu=LffitB.transform(rij,gen,rk,[TES[1],TES[2]],[CRKPTS[1], RXCLRPTS[2]])
      del gen
      gen={}
      for i in gu.keys():
        gen[i]=gu[i]
      #gc.collect()
    else:
      flg='sumzero'
      break

    if len(gen.keys())>2000:
      flg='limit-reached'
      break

  #print("JOB COMPLETED")
  #print flg
  #gc.collect()
  #return [lth,ltn,ngt,pqr,gen,flg,fit
