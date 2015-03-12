def TRATES(RK,Gn,Np,Prms,Lg):

  import math as mth
  ngi=0
  fnei=1.0
  Tr={}
  B=Prms[0]
  LhCn=Prms[1]
  Lav=Prms[2]
  r2=Np*RK[1]*(fnei)*(0.5)*(1+mth.tanh(Lg-Lav))

  for i in Gn.keys():
    RR=[]
    wi=sum(Gn[i][4].values())/LhCn
    fnei=0.8
    r1=Np*RK[0]*(Gn[i][2]/Lg)*(mth.exp((mth.fabs(1-wi)))-1.0)
    r3=Np*RK[2]*(fnei*Gn[i][2]/Lg)*(mth.exp(-B*wi))
    RR.append(r1)
    RR.append(r2)
    RR.append(r3)
    Tr[i]=RR
    #raw_input()
  return Tr
