def CALCWIJ(sij,H,hll,lij,hllb):
  import hilla
  import hillb
  wij={}
  for i in H:
    if i in sij.keys():
      wij[i]=hilla.HILLA(sij[i],hll[0],hll[1],1.0)*hillb.HILLB(lij,hllb,2)
      print i, sij[i], wij[i]

      #n=sij.keys().index(i)
      #print n
      #print sij.keys()[n]
  return wij
