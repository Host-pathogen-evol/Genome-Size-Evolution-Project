
def NEWHOST(L,K,rk):

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

  return hx
