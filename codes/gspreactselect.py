def GSPREACTSELECT(gnsum,rk,TRALL):

  rctpr=[]
  lk=gnsum*rk.uniform_pos()
  sumtr=0.0
  brkflg=0

  for i in TRALL.keys():
    for j in TRALL[i].keys():
      cnt=0.0
      for k in TRALL[i][j]:
        sumtr+=k
        if sumtr>=lk:
          rctpr.append(i)
          rctpr.append(j)
          rctpr.append(cnt)
          brkflg=1
          break
        cnt+=1
      if(brkflg==1):
        break

  return rctpr
