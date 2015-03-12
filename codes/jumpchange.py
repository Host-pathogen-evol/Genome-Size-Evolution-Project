def JUMPCHANGE(gn,nh,HILLPAR,HILLI):
  nwgn={}
  import calcwij
  for i in gn.keys():
    ngenu=[]
    for j in range(4):
      ngenu.append(gn[i][j])

    nwij=calcwij.CALCWIJ(gn[i][3],nh,HILLPAR,gn[i][2],HILLI)
    ngenu.append(nwij)
    nwgn[i]=ngenu
  return nwgn
