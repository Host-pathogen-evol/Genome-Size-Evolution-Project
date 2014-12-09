def GETLENGTHSTE(gk):
  lnx=0.0
  lnte=0.0
  lneff=0.0
  nte=0.0
  neff=0.0

  for i in gk.keys():
    lnx+=gk[i][1]
    if gk[i][0]=="TE":
      nte+=1.0
      lnte+=gk[i][1]
    if gk[i][0]=="EFFON":
      neff+=1.0
      lneff+=gk[i][1]
  LST=[lnte,nte,lneff,neff,lnx,lneff+lnte,len(gk.keys()),nte+neff]
  return LST
