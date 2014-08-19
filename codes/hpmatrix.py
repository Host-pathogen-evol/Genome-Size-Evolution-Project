def HPMATRIX(Kn,Kx,kix,rk):
  #print rk.name()
  HPMT=[[0.0 for col in range(Kx)] for row in range(Kn)]

  for i in range(0,Kn):
    for j in range(0,Kx):
      l1=rk.uniform()
      if l1<kix:
        HPMT[i][j]=1.0
  #			l1x=rk.uniform()
  #			if l1x<0.5:
  #				HPMT[i][j]=1.0
  #			else:
  #				HPMT[i][j]=1.0
  #		HPMT[j][i]=HPMT[i][j]
  #	print i
  return HPMT
