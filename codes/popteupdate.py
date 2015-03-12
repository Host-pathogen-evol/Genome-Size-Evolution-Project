def POPTEUPDATE(Fn,Nn,Nh,bn):
  NUP={}
  Snk=0.0
  for i in Fn.keys():
    Snk+=(Fn[i]*Nn[i])

  for i in Nn.keys():
    nu=(Nn[i]*Fn[i]*Nh)/(bn*Nh+Snk)#-Nn[i]
    if nu<1.0:
      nup=0.0
    else:
      nup=nu
    #nup=nu

    NUP[i]=nup
  #print NUP
  return NUP
