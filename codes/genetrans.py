def GENETRANS(ng,nt,Gk,H,hll,hllb,rk):
  import calcwij
  #print ng
  #print nt
#rn 0 ei->ei'
#rn 1 ei->ei+ei
#rn 2 ei->eo
  Gnmod={}
  if nt==0:
    for mu in Gk.keys():
      if (mu<ng) or (mu>ng):
        Gnmod[mu]=Gk[mu]
      if mu==ng:
        sigl=0.001 ####this is a std for the scores move  s'=s+ds !!!!
        skx=Gk[ng][3]
        sijn={}
        for sj in skx.keys():
          if skx[sj]==0.0:
            sijn[sj]=0.0
          if skx[sj]!=0.0:
            dsj=rk.gaussian(sigl)
            if (skx[sj]+dsj)>0:
              sijn[sj]=skx[sj]+dsj
            if (skx[sj]+dsj)<=0:
              sijn[sj]=0.00001
        nugen=[]
        nugen.append(Gk[ng][0])
        nugen.append(Gk[ng][1])
        ql=rk.uniform_pos()
        dlen=10.0
        if ql<=0.5:
          qq=rk.uniform_pos()
          nlen=Gk[ng][2]+dlen*qq
        if ql>0.5:
          qq=rk.uniform_pos()
          nlen=Gk[ng][2]-dlen*qq
          if nlen<0.0:
            nlen=0.0
        nugen.append(nlen)
        nugen.append(sijn)
        lij=nlen
        wijm=calcwij.CALCWIJ(sijn,H,hll,lij,hllb)
        nugen.append(wijm)
        Gnmod[ng]=nugen
      #print dsj

  if nt==1:
  #print("UNO")
    for mu in Gk.keys():
      if mu<ng:
        Gnmod[mu]=Gk[mu]
      if mu==ng:
        Gnmod[mu]=Gk[mu]
        Gnmod[mu+1]=Gk[mu]
      if mu>ng:
        Gnmod[mu+1]=Gk[mu]
  if nt==2:
    #print("DOS")
    for mu in Gk.keys():
      if mu<ng or mu>ng:
        Gnmod[mu]=Gk[mu]
      if mu==ng:
        gx=[]
        gx.append('SL'+Gk[ng][0])
        gx.append(Gk[ng][1])
        lij=rk.uniform()*Gk[ng][2]
        gx.append(lij)
        snu={}
        for ik in Gk[ng][3].keys():
          snu[ik]=0.000001
        gx.append(snu)
        wijm=calcwij.CALCWIJ(snu,H,hll,lij,hllb)
        gx.append(wijm)
        Gnmod[ng]=gx
#print Gnmod
  return Gnmod
