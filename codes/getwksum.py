def GETWKSUM(gn):
  wnsum=0
  for i in gn.keys():
    if len(gn[i][4])>0:
      wnsum=wnsum+sum(gn[i][4].values())
      #wnsum=wnsum+sum()
  return wnsum
