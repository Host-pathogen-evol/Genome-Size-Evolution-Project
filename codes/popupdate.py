def POPUPDATE(Fn,Nn,Nh):
  NUP={}
  Snk=0.0
  for i in Fn.keys():
    Snk+=(Fn[i]*Nn[i])

  for i in Nn.keys():
    nu=(Nn[i]*Fn[i]*Nh)/(Nh+Snk)
    NUP[i]=nu

  return NUP
