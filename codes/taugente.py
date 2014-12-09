def TAUGENTE(Tr,Np,rk):
  import gsptime
  Tau={}
  for i in Tr.keys():
    sx=sum(Tr[i])
    taux=gsptime.GSPTIME(sx,rk)
    if taux<Np:
      Tau[i]=1
    else:
      Tau[i]=0

  return Tau
