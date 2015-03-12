def DCTCPY(dold):
  import copy
  dnew={}
  for j in dold.keys():
    dnew[j]=copy.deepcopy(dold[j])
    #dnew[j].append([2,3,5])

  return dnew
