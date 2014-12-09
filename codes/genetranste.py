def GENETRANSTE(ng,nt,Gk,H,hll,hllb,rk,Kh,tesij):
#ng gene "number"
#nt transformation number
#Gk
#H
#hll
#hllb
#rk random number generation handle
  from math import floor as flr
  import copy as lcp
  Gnmod={} #New genome

  #print("GEN: %d\n"%ng)

  if nt==0: #A

    for i in Gk.keys():
      if((i<ng) or (i>ng)):
        Gnmod[i]=Gk[i]
      if i==ng:
        sigl=0.01 ####this is a std for the scores move  s'=s+ds !!!!
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
        #nugen.append(Gk[ng][1])
        ql=rk.uniform_pos()
        dlen=10.0
        if ql<=0.5:
          qq=rk.uniform_pos()
          nlen=Gk[ng][1]+dlen*qq
        if ql>0.5:
          qq=rk.uniform_pos()
          nlen=Gk[ng][1]-dlen*qq
          if nlen<0.0:
            nlen=0.0
        nugen.append(flr(nlen))
        nugen.append(Gk[ng][2])
        nugen.append(sijn)
        lij=nlen
        import calcwijtes
        wijm=calcwijtes.CALCWIJTES(sijn,H,hll,lij,hllb)
        nugen.append(wijm)
        Gnmod[ng]=nugen

  #return Gnmod

  if nt==1: #B
    for i in Gk.keys():
      if (i!=ng):
        Gnmod[i]=Gk[i]

      if i==ng:
        nugen=[]
        nugen.append(Gk[i][0])
        nugen.append(Gk[i][1])
        nlk=len(Gk[i][2])
        fx=0
        nlklst=[]
        nlklst=lcp.deepcopy(Gk[i][2])
        #print Gk[i][2]
        #raw_input()
        while fx==0:
          #jo=rk.uniform_int(nlk)
          #nk=nlklst[jo]+1
          nk=1+rk.uniform_int(Kh)
          if (nk not in Gk[i][2]) and (nk<=Kh):
            nlklst.append(nk)
            fx=1
        nlklst.sort()
        print nlklst
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
        Gnmod[ng]=nugen
        #raw_input()

  if nt==2: #C
    for i in Gk.keys():
      if (i!=ng):
        Gnmod[i]=Gk[i]

      if i==ng:
        nugen=[]
        nugen.append(Gk[i][0])
        nugen.append(Gk[i][1])
        nlklst=[]
        nlklst=lcp.deepcopy(Gk[i][2])
        nlk=len(Gk[i][2])
        #print Gk[i][2]
        #print nlk
        #raw_input()
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
          Gnmod[ng]=nugen

        if nlk==1:
          #print("HOLA")
          nugen=[]
          nugen.append("TE")
          nugen.append(Gk[i][1])
          nugen.append(tesij)
          import calcwijtes
          wnu=calcwijtes.CALCWIJTES(tesij,H,hll,nugen[1],hllb)
          nugen.append(wnu)
          Gnmod[ng]=nugen

  if nt==3: #D
      for i in Gk.keys():
        if (i!=ng):
          Gnmod[i]=Gk[i]

        if i==ng:
          nugen=[]
          nugen.append(Gk[i][0])
          nugen.append(Gk[i][1])
          nlklst=lcp.deepcopy(Gk[i][2])
          nlk=len(Gk[i][2])
          fx=0
          while fx==0:
            jo=rk.uniform_int(nlk)
            #nk=nlklst[jo]+1
            nk=1+rk.uniform_int(Kh)
            if (nk not in Gk[i][2]) and (nk<=Kh):
              nlklst[jo]=nk
              #nlklst.append(nk)
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
          Gnmod[ng]=nugen

  if nt==4: #E
    for i in Gk.keys():
      if i<ng:
        Gnmod[i]=Gk[i]
      if i==ng:
        Gnmod[ng]=Gk[ng]
        Gnmod[ng+1]=Gk[ng]
      if i>ng:
        Gnmod[i+2]=Gk[i]

  if nt==5: #F
    mu=0
    for i in Gk.keys():
      if i<ng:
        Gnmod[i]=Gk[i]
      if i>ng:
        Gnmod[i-1]=Gk[i]

  if nt==6: #G
    for i in Gk.keys():
      if i<ng:
        Gnmod[i]=Gk[i]
      if i==ng:
        Gnmod[ng]=Gk[ng]
        Gnmod[ng+1]=Gk[ng]
      if i>ng:
        Gnmod[i+2]=Gk[i]

  if nt==7: #H
    for i in Gk.keys():
      Gnmod[i]=Gk[i]

    ngn=len(Gk.keys())
    #print ngn, max(Gk.keys())
    nugen=[]
    lte=8000.0*rk.uniform_pos()
    nugen.append("TE")
    nugen.append(flr(lte))
    nugen.append(tesij)
    import calcwijtes
    wnu=calcwijtes.CALCWIJTES(tesij,H,hll,nugen[1],hllb)
    nugen.append(wnu)
    Gnmod[ngn]=nugen

  return Gnmod
