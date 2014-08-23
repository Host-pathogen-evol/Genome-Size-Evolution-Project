def SCORESINIT(adij,rk):
  sij={}
  n=1
  for i in adij:
    #if i==0.0:
    #  sij[n]=0.0
      #sij.append(0.0)
    if i==1:
      #sij.append(rk.uniform.pos())
      sij[n]=1.0*rk.uniform_pos()
    n=n+1

  return sij
