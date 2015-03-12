def GETWKSUM(gn,ck):
  wnsum=0
  for i in gn.keys():
    if len(gn[i][4])>0:
      wnsum=wnsum+sum(gn[i][4].values())
      #wnsum=wnsum+sum()
  wnsum=wnsum/(ck*len(gn.keys()))
  return wnsum
