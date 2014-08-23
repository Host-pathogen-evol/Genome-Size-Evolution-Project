def PRTGENOME(gn):
  for i in gn.keys():
    print("key:%d"%i)
    print("label:%s"%gn[i][0])
    print("gene:%s"%gn[i][1])
    print("length:%lf"%gn[i][2])
    print("length-wij:%lf"%len(gn[i][4]))
    for j in gn[i][4].keys():
      print("%d %lf %lf"%(j,gn[i][3][j],gn[i][4][j]))
