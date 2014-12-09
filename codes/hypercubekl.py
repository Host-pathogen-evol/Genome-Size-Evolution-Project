def HYPERCUBEKL(Lg,KL):
  #print Lg
  Gn={}
  Gnx={}
  Gnx[0]=[0]
  Gnx[1]=[1]
  #print("zero set")
  #print Gnx
  #raw_input()

  for z in range(1,Lg):
    #print("iteration:%d"%z)
    mu=0
    for i in range(2):
      ng=[]
      ng.append(i)
      for j in Gnx.keys():
        nugene=[]
        nugene=ng+Gnx[j]
        nones=0.0
        for zn in nugene:
          if zn==1:
            nones+=1
        if (nones<=KL) and (nones>0):
          Gn[mu]=nugene
          mu=mu+1
    #print Gn
    Gnx={}
    Gnx=Gn
    if(z<(Lg-1)):
      Gn={}

    #raw_input()
  #print Gn
  return Gn
