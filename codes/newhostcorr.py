def NEWHOSTCORR(Hstold,Kh,rk):
  #print Hstold
  #for i in range(10):
  #print i
  Zn=Hstold
  tst=0
  while tst==0:
    zx=1+rk.uniform_int(Kh)
    if zx not in Zn:
      tst=1.0
  jn=rk.uniform_int(len(Zn))
  Znx=[]
  for jx in Zn:
    if jx!=Zn[jn]:
      Znx.append(jx)
  Znx.append(zx)
  Hnew=sorted(Znx)
  return Hnew
