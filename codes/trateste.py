def TRATESTE(Mr,Gn,Np,Prms,Fn):
  import math as mth
  import trpste as pw

  mu1=Np*Mr[0]
  ps=pw.TRPSTE(Fn)
  #print ps
  #raw_input()
  mu2=Np*Mr[1]*ps
  mu3=Np*Mr[2]*ps
  mu4=Np*Mr[3]*ps
  mu5=Np*Mr[4]
  mu6=Np*Mr[5]
  mu7=Np*(Mr[6]*(1.0+ps))
  mu8=Np*Mr[7]

  Tr={}
  cx=Prms[0] #C
  lh=Prms[1] #Lhost
  C=cx
  Kh=Prms[2] #Kh
  Lg=Prms[3] #Genome length
  Ls=Prms[4] #Genome length threshold

  for i in Gn.keys():
    Rk=[]
    if Gn[i][0]=="EFFON":
      we=(sum(Gn[i][4]))/(cx*lh)
      nk=len(Gn[i][2])
      ek=0.0
      for ji in Gn[i][4].keys():
        if Gn[i][4][ji]>0.0:
          ek+=1
      degek=ek/nk

      tr1=mu1*Gn[i][1]*mth.exp(1.0-we)##S->S'
      tr2=mu2*mth.exp(1.0-we)*(C*Kh-nk)##Add link
      tr3=mu3*mth.exp(1.0-we)*(1.0-degek)##Replace
      tr4=mu4*mth.exp(1.0-we)*(1.0-degek)##Remove one
      tr5=mu5*(1-(Lg/Ls)) #repeat
      tr6=mu6*mth.exp(-we) #remove
      Rk.append(tr1) #s-s'
      Rk.append(tr2) #add link
      Rk.append(tr3) #replace link
      Rk.append(tr4) #remove link
      Rk.append(tr5) #repeat
      Rk.append(tr6) #remove
      Rk.append(0.0) #----
      Rk.append(0.0) #----

    if Gn[i][0]=="TE":
      if (Ls-Lg)>0:
        tr7=mu7*(1-(Lg/Ls))
      else:
        tr7=0.0
        
      tr8=mu8
      Rk.append(0.0) #--
      Rk.append(0.0) #--
      Rk.append(0.0) #--
      Rk.append(0.0) #--
      Rk.append(0.0) #--
      Rk.append(0.0)  #--
      Rk.append(tr7)  #repeat te
      Rk.append(tr8)  #remove te

    Tr[i]=Rk
  return Tr
