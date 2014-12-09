def JUMPCHANGETE(Go,Hx,hillpta,hillptb):

  import hilla
  import hillb

  GJMP={}

  for k in Go.keys():

    Gjump=[]
    Gjump[0].append(Go[k][0])
    Gjump[1].append(Go[k][1])
    Gjump[2].append(Go[k][2])
    Gjump[3].append(Go[k][3])

    if Go[k][0]=="EFFON":
      wn={}
      for sij in Go[k][3].keys():
        if sij in Hx:
          so=hillpta[0]
          hn=hillpta[1]
          l=Go[k][1]
          lo=hillptb[0]
          wij=hilla.HILLA(sij,so,hn,1.0)#*hillb.HILLB(l,lo,2)
          wn[sij]=wij
          else:
            wn[sij]=0.0
          #wij=hilla.HILLA(s,so,hn,1.0)*hillb.HILLB(l,lo,2)
      Gjump[4].append(wn)

    GJMP[k]=Gjump

  return GJMP



#for k in Go.keys():
#  if Go[k][0]=="TE":
    #print ("transposon")
#    s=Go[k][2]
#    so=hillpta[0]
#    hn=hillpta[1]
#    l=Go[k][1]
#    lo=hillptb[1]
#    wite= hilla.HILLA(s,so,hn,1.0)*hillb.HILLB(l,lo,2)
#    Gn[k].append(wite)
#  if Go[k][0]=="EFFON":

#    wn={}
    #ln=len(sij.keys())
    #sn1=0.0
    #sn2=0.0

#    for sij in Go[k][3].keys():
#      if sij in Hx:
#        #sn1+=Go[k][3][sij]
#        #sn2+=1.0
#        so=hillpta[0]
#        hn=hillpta[1]
#        l=Go[k][1]
#        lo=hillptb[0]
#        wij=hilla.HILLA(sij,so,hn,1.0)#*hillb.HILLB(l,lo,2)
#        wn[sij]=wij
#      else:
#        wn[sij]=0.0
    #wij=hilla.HILLA(s,so,hn,1.0)*hillb.HILLB(l,lo,2)
#    Gn[k].append(wn)
#return Gn
    #print ("EFFECTOR")
