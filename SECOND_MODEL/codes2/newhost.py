import itertools as itr
from numpy import random as rk

def NEWHOST(L,K): #length,universe of target, state of random
    hx=set()
    while len(hx)<L:
        zx=rk.randint(1,K+1)
        if not zx in hx:
            hx.add(zx)
    hx=list(hx)
    hx.sort()
    return hx

def NEWPATHOGEN(k,neo,nto):#itr): #neo is max number of effectors at time 0,nto max numb of targeted genes for each effector
    pth={}
    n=rk.randint(1,neo+1) #initial number of effector
    for j in xrange(n):
        pth[j]={}
        lj=rk.randint(1,nto+1) #number of targeted genes
        pth[j]=dict(itr.izip(NEWHOST(lj,k),rk.random(lj)))
    return pth
#d={effector:{target:score,target:score}}
