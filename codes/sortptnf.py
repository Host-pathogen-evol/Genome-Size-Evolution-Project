def SORTPTNF(Pt,jmp):
  #print len(Pt.keys())
  #tn=list(range()
  #sn="jmp"+str(jmp)+"gen"+str(cnt)
  #tmax=len(Pt[Pt.keys()[0]])
  tmax=len(Pt[Pt.keys()[0]])
  #print tmax
  for i in Pt.keys():
    if len(Pt[i])>tmax:
      tmax=len(Pt[i])

  print tmax
  tn=[]
  RPR={}
  tn=range(tmax)
  for i in Pt.keys():
    yt=[]
    m=tmax-len(Pt[i])
    for j in range(m):
      yt.append(0.0)
    for j in range(len(Pt[i])):
      yt.append(Pt[i][j])

    print len(yt)
    RPR[i]=yt

  return RPR
