def NUTEGNOME(TBL,NRCT,Gk,H,hll,hllb,rk,Kh,tesij):
#TBL yes/no "number"
#NRCT transformation to be applied
#Gk
#H
#hll
#hllb
#rk random number generation handle
  from math import floor as flr
  import copy as lcp
  Gnmod={} #New genome

  #print("GEN: %d\n"%ng)
  mu=0

  for i in TBL.keys():
    nugen=[]

    if TBL[i]==0:
      for jk in Gk[i]:
        nugen.append(jk)
      Gnmod[mu]=nugen
      mu+=1

    if TBL[i]==1:
      rn=NRCT[i]
      ###########################
      if rn==0:
        sigl=0.01 ####this is a std for the scores move  s'=s+ds !!!!
        skx=Gk[i][3]
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

        nugen.append(Gk[i][0])
        #nugen.append(Gk[ng][1])
        ql=rk.uniform_pos()
        dlen=10.0
        if ql<=0.5:
          qq=rk.uniform_pos()
          nlen=Gk[i][1]+dlen*qq
        if ql>0.5:
          qq=rk.uniform_pos()
          nlen=Gk[i][1]-dlen*qq
          if nlen<0.0:
            nlen=0.0
        nugen.append(flr(nlen))
        nugen.append(Gk[i][2])
        nugen.append(sijn)
        lij=nlen
        import calcwijtes
        wijm=calcwijtes.CALCWIJTES(sijn,H,hll,lij,hllb)
        nugen.append(wijm)
        Gnmod[mu]=nugen
        mu+=1
      ##########################
      if rn==1:
        nugen.append(Gk[i][0])
        nugen.append(Gk[i][1])
        nlk=len(Gk[i][2])
        fx=0
        nlklst=[]
        nlklst=lcp.deepcopy(Gk[i][2])
        while fx==0:
          nk=1+rk.uniform_int(Kh)
          if (nk not in Gk[i][2]) and (nk<=Kh):
            nlklst.append(nk)
            fx=1
        nlklst.sort()
        snu={}
        wnu={}
        for zi in nlklst:
          if zi in Gk[i][3].keys():
            snu[zi]=Gk[i][3][zi]
          if zi not in Gk[i][3].keys():
            snu[zi]=0.5
        import calcwijtes
        wnu=calcwijtes.CALCWIJTES(snu,H,hll,nugen[1],hllb)
        nugen.append(nlklst)
        nugen.append(snu)
        nugen.append(wnu)
        Gnmod[mu]=nugen
        mu+=1    #raw_input()
      ##################################################################
      if rn==2:
        nugen.append(Gk[i][0])
        nugen.append(Gk[i][1])
        nlklst=lcp.deepcopy(Gk[i][2])
        nlk=len(Gk[i][2])
        fx=0
        while fx==0:
          jo=rk.uniform_int(nlk)
          nk=1+rk.uniform_int(Kh)
          if (nk not in Gk[i][2]) and (nk<=Kh):
            nlklst[jo]=nk
            fx=1
        nlklst.sort()
        snu={}
        wnu={}
        for zi in nlklst:
          if zi in Gk[i][3].keys():
            snu[zi]=Gk[i][3][zi]
          if zi not in Gk[i][3].keys():
            snu[zi]=0.5
        import calcwijtes
        wnu=calcwijtes.CALCWIJTES(snu,H,hll,nugen[1],hllb)
        nugen.append(nlklst)
        nugen.append(snu)
        nugen.append(wnu)
        Gnmod[mu]=nugen
        mu+=1
      ##################################################################
      if rn==3:
        nugen.append(Gk[i][0])
        nugen.append(Gk[i][1])
        nlklst=[]
        nlklst=lcp.deepcopy(Gk[i][2])
        nlk=len(Gk[i][2])
        if nlk>1:
          jo=rk.uniform_int(nlk)
          nj=nlklst[jo]
          nlklst.remove(nj)
          nusij={}
          for ki in nlklst:
            nusij[ki]=Gk[i][3][ki]
            wnu={}
          import calcwijtes
          wnu=calcwijtes.CALCWIJTES(nusij,H,hll,nugen[1],hllb)
          nugen.append(nlklst)
          nugen.append(nusij)
          nugen.append(wnu)
          Gnmod[mu]=nugen
          mu+=1

        if nlk==1:
          nugen.append("TE")
          nugen.append(Gk[i][1])
          nugen.append(tesij)
          import calcwijtes
          wnu=calcwijtes.CALCWIJTES(tesij,H,hll,nugen[1],hllb)
          nugen.append(wnu)
          Gnmod[mu]=nugen
          mu+=1
      ##################################################################
      if rn==4:
        Gnmod[mu]=Gk[i]
        Gnmod[mu+1]=Gk[i]
        mu=mu+2
      ##################################################################
      if rn==5:
        x=1
        #Do nothing!
      ##################################################################
      if rn==6:
        Gnmod[mu]=Gk[i]
        Gnmod[mu+1]=Gk[i]
        mu=mu+2
      ##################################################################
      if rn==7:
        x=0
        #Do nothing
      ##################################################################
      if rn==8: #HGT-NOT YET INCLUDED
        lte=8000.0*rk.uniform_pos()
        nugen.append("TE")
        nugen.append(flr(lte))
        nugen.append(tesij)
        import calcwijtes
        wnu=calcwijtes.CALCWIJTES(tesij,H,hll,nugen[1],hllb)
        nugen.append(wnu)
        Gnmod[mu]=nugen
        mu+=1

  return Gnmod
