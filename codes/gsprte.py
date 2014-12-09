def GSPRTE(TR,TAUS,rk):
  rtx={}
  for i in TAUS.keys():
    if TAUS[i]==0:
      rtx[i]=-1
    else:
      #tq=[]
      sn=sum(TR[i])
      lk=sn*rk.uniform_pos()
      cnt=0
      sntr=0.0
      for tk in TR[i]:
        sntr+=tk
        if sntr>=lk:
          rtx[i]=cnt
          break
        cnt+=1
  return rtx
