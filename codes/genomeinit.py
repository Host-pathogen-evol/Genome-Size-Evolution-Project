def GENOMEINIT(Neff,Kp,rk,LNPRT,HP,HST,HILLPAR,HILLLI):

  import neweffectorlist
  import scoresinit
  import calcwij
  go={}

  hx=neweffectorlist.NEWEFFECTORLIST(Neff,Kp,rk)
  #print hx
  import newpathogenunita
  for i in hx:
    go[i]=newpathogenunita.NEWPATHOGENUNITA(i,rk,LNPRT)

  gox={}
  for i in go.keys():
    z=go[i]
    mu=scoresinit.SCORESINIT(HP[i-1],rk)
    wn=calcwij.CALCWIJ(mu,HST,HILLPAR,go[i][2],HILLLI)
    z.append(mu)
    z.append(wn)
    gox[i]=z
    #print wn
    #del go
  return gox
