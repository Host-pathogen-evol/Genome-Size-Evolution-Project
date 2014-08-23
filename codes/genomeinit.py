def GENOMEINIT(Neff,Kp,rk,LNPRT,HP,HST,HILLPAR,HILLLI):

  import neweffectorlist
  import scoresinit
  import calcwij
  go={}
  #print("fix for the genome list")
  hx=neweffectorlist.NEWEFFECTORLIST(Neff,Kp,rk)
  #print hx
  #raw_input()
  import newpathogenunita
  for i in range(len(hx)):
    go[i]=newpathogenunita.NEWPATHOGENUNITA(i,rk,LNPRT,hx)

  gox={}
  for i in go.keys():
    z=go[i]
    qj=go[i][1]-1
    mu=scoresinit.SCORESINIT(HP[qj],rk)
    wn=calcwij.CALCWIJ(mu,HST,HILLPAR,go[i][2],HILLLI)
    z.append(mu)
    z.append(wn)
    gox[i]=z
    #print wn
    #del go
  return gox
