def GSPSUM(TRALL):

  sn=0.0;
  for i in TRALL.keys():
    for j in TRALL[i].keys():
          sn+=sum(TRALL[i][j])
          #print j, TRALL[i][j]
  return sn
