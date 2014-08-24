def POPUPDATE(Fn,Nn,Nh,bn):
  NUP={}
  Snk=0.0
  for i in Fn.keys():
    Snk+=(Fn[i]*Nn[i])

  for i in Nn.keys():
    nu=(Nn[i]*Fn[i]*Nh)/(bn*Nh+Snk)
    NUP[i]=nu

  return NUP
