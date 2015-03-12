def GSPTIME(gsum,rk):
  from math import log as mlog
  lk=rk.uniform_pos()
  tnr=(1.0/gsum)*mlog(1.0/lk)
  return tnr
