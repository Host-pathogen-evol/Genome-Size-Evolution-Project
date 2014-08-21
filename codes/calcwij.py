def CALCWIJ(sij,H,hll):
  import hilla
  wij={}
  for i in H:
    if i in sij.keys():
      wij[i]=hilla.HILLA(sij[i],hll[0],hll[1],1.0)
      print i, sij[i], wij[i]

      #n=sij.keys().index(i)
      #print n
      #print sij.keys()[n]
  return wij
