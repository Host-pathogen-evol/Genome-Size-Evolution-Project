def CALCWIJTES(sij,H,hll,lx,hllb):
  import hilla
  import hillb

  import types
  if type(sij) is dict:
    wn={}
    #s=Go[k][3][sij]
    so=hll[0]
    hn=hll[1]
    l=lx
    lo=hllb[0]

    for si in sij.keys():
      s=sij[si]
      if si in H:
        wij=hilla.HILLA(s,so,hn,1.0)#*hillb.HILLB(l,lo,2)
        wn[si]=wij
      else:
        wn[si]=0.0

  if type(sij) is float:
    s=sij
    so=hll[0]
    hn=hll[1]
    l=lx
    lo=hllb[1]
    wn=hilla.HILLA(s,so,hn,1.0)#*hillb.HILLB(l,lo,2)

  return wn
