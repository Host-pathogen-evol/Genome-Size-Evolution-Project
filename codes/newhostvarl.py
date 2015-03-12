def NEWHOSTVARL(L,K,rk):
  hx=[]
  q=1
  zx=1+rk.uniform_int(K)
  hx.append(zx)
  while q<L:
    mu=0
    zx=1+rk.uniform_int(K)
    for j in hx:
      if j==zx:
        mu=1
        break

    if mu==0:
      hx.append(zx)
      q=q+1

  hx.sort()
  nx=0
  cn=rk.uniform_pos()
  while nx<(L*cn):
    jn=rk.uniform_int(L)
    hx[jn]=0
    nx=nx+1

  return hx
