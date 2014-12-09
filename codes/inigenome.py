def INIGENOME(Ngen,tesfrac,rk,C,Kh,tessij):
  from math import floor as flr
  import numpy as np
  import newhost
  go={}
  seed=123456789
  ix=0
  for k in range(Ngen):
    genex=[]
    u=1.0*rk.uniform_pos()
    if u<tesfrac:
      genex.append("TE")
      l=8000.0*rk.uniform_pos()
      genex.append(flr(l))
      genex.append(tessij)
    else:
      genex.append("EFFON")
      l=500.0*rk.uniform_pos()
      genex.append(flr(l))
      adk=[]
      ##############################################
      rk2=np.random.RandomState(seed-ix).binomial(Kh,C)
      ix+=1
      #print rk2
      adkx=[]
      adkx=newhost.NEWHOST(rk2,Kh,rk)
      #print adkx
      #raw_input()
      ##############################################
      ####
      #kr=1+rk.uniform_int(tmax)
      #mix=0
      #while mix<=kr:
      #  zx=1+rk.uniform_int(Kh)
      #  if zx not in adk:
      #    adk.append(zx)
      #    mix+=1
      ##
      adkx.sort()
      Sk={}
      for i in adkx:
        Sk[i]=tessij
      genex.append(adkx)
      genex.append(Sk)

    go[k]=genex

  return go
