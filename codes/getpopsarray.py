#ls codes/EXPERIMENTS/data/
import pickle
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import *

pth='newkerneltest/'
k=3
spops=pth+"PopsJMP"+str(k)+".p"
A=pickle.load(open(spops,"rb"))
print("LOADED")

print len(A.keys())
pns=[]
kys=[]
n=0
lmx=0
lmn=len(A[A.keys()[0]])
nx=0
mx=0
for z in A:
    pns.append(len(A[z]))
    kys.append(z)
    if lmx<len(A[z]):
        lmx=len(A[z])
        nx=n
    if lmn>len(A[z]):
        lmn=len(A[z])
        mx=n
    n+=1

print max(pns),nx, pns[nx],kys[nx]
print min(pns),mx, pns[mx],kys[mx]

tsn={}
nk=0
#AT={}
for i in A.keys():
    #if (nk%10) ==0:
    #    print nk
    a=[]
    #b=[]
    mu1=len(A[i])
    mu2=lmx
    for j in range(mu2):
        if j<mu2-mu1:
            a.append(0.0)
        else:
            n=mu2-mu1
            a.append(A[i][j-n])

        #a.append((mu2-mu1)+j)
        #b.append(A[j])
    #print len(a), mu1
    tsn[i]=a
    nk+=1

timepops=pth+"tPopsJMP"+str(k)+".p"
pickle.dump(tsn,open(timepops,"wb"))
print("done")
