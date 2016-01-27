def job(PT,SEED,nte,neff,tn,RXCLRPTS,CRKPTS,TES):
  from math import floor
  from pygsl import rng as rn
  import sys
  sys.path.append('../LNKMODEL/')
  import Lf
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

  #print("parameter vector:"% PT)
  av1=0.5*(RXCLRPTS[2]-RXCLRPTS[1])
  av2=0.5*(CRKPTS[2]-CRKPTS[1])
  av3=0.5*(TES[2]-TES[1])
  Lth=floor((RXCLRPTS[0]+CRKPTS[0]+TES[0])*(1.0/3.0)*(av1+av2+av3))
  #print Lth
  MU=[Np,m1,m2,m3,m4,m5,m6,m7,m8,Lth,beta1,beta2]

  #SEED=987654320
  rk=rn.rng()
  rk.set(SEED)

################
  gen={}
  trs={}
#  nte=10
#  neff=10
  gen=Lf.inigenome(nte,neff,rk,[TES[1],TES[2]],[CRKPTS[1], RXCLRPTS[2]])
################
  Ntot=RXCLRPTS[0]+CRKPTS[0]+TES[0]
  pqr={}
  ltn=[]
  lth=[]
  ngt=[]
  flg='all-good'
  for nk in range(tn):#Ntot):
    trs=Lf.trates(gen,MU)
    rij,sr =Lf.montec(trs,rk)
    if sr!='TRUE':
      pqr[nk]=[rij[0],rij[1],gen]
      ltn.append(Lf.lent(gen))
      lth.append(Lth)
      ngt.append(len(gen.keys()))
      gu={}
      gu=Lf.transform(rij,gen,rk,[TES[1],TES[2]],[CRKPTS[1], RXCLRPTS[2]])
      gen={}
      for i in gu.keys():
        gen[i]=gu[i]
    else:
      flg='sumzero'
      break

    if len(gen.keys())>2000:
      flg='limit-reached'
      break

  #print("JOB COMPLETED")
  #print flg
  return [lth,ltn,ngt,pqr,gen,flg]
