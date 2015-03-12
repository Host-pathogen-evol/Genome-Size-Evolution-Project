def INIGENOMETE(Ngo,Tefrac,rk,C,Kh,tessij,Hx,hlpt,lohills):

#Inital number of genes Ngo, Fraction of transposons Tefrac
#rk rngenerator instance
#C connectivity, tessij-initial scores
#Hx host, nlpt and lohills hill parameters
  import inigenome
  import inigenomew
  import getwksumte
  import math as mth
  INISETUP=[]
  Gini={}
  Fo=0.0
  LH=len(Hx)
  while Fo<1.0:
    Go={}
    Go=inigenome.INIGENOME(Ngo,Tefrac,rk,C,Kh,tessij)
    Gini=inigenomew.INIGENOMEW(Go,Hx,hlpt,lohills)
    Wo=getwksumte.GETWKSUMTE(Gini,C*LH)
    Fo=mth.exp(Wo)-1.0

  INISETUP.append(Fo)
  INISETUP.append(Gini)
  return INISETUP
