
def LSTDST(S1,S2):
  #import numpy as np
  d=0
  #print("caquita")
  #assert len(S1) == len(S2)
  for i in range(len(S1)):
    #print S1[i]
    #print S2[i]
    if S1[i]!=S2[i]:
      d=d+1
  return d
