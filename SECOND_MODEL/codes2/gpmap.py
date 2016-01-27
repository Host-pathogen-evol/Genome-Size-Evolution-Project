def g_p_mapa(host,path):
    dic_tar={}
    for target in host:
        sn=0.0
        for effector in path:
            if target in path[effector]:
                sn+=path[effector][target]
                if sn>1:
                    sn=1.0
                    break
        dic_tar[target]=sn
    return dic_tar

def g_p_mapa2(host,path,so):
    dic_tar={}
    for target in host:
        sn=0.0
        for effector in path:
            if target in path[effector]:
                sn+=path[effector][target]
        dic_tar[target]=sn/(sn+so)
    return dic_tar

def g_p_mapb(host,path):
    dic_eff={}
    for effector in path:
        sn=0.0
        for target in path[effector]:
            if target in host:
                sn+=path[effector][target]
        dic_eff[effector]=sn
    return dic_eff
