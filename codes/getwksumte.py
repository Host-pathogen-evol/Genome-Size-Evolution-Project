def GETWKSUMTE(gn,ck):
  wnsum=0
  n=0
  #print("CALCULATING")
  #print wnsum
  for i in gn.keys():#
    if gn[i][0]=="EFFON":
      if len(gn[i][4])>0:
        an=sum(gn[i][4].values())
        if an>0:
          #print i, gn[i][4]
          wnsum=wnsum+an
      n=n+1
          #raw_input()
        #wnsum=wnsum+sum()
  #print wnsum
  wnsumx=wnsum/(ck*n)
  return wnsumx
