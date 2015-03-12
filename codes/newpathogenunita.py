
def NEWPATHOGENUNITA(ng,rk,lr,ptj):
  PTHU=[]
  import numpy as np
  import math as mth
  lnmu=mth.log(lr[1])
  lnsigma=lr[0]
  PTHU.append('E'+str(ptj[ng]))
  PTHU.append(ptj[ng])
  lc=np.random.lognormal(mean=lnmu,sigma=lnsigma,size=1)
  PTHU.append(lc[0])

  return PTHU
