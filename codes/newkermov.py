import pickle
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
from pylab import *

pth='newkerneltest/'

JMP=3

#for k in range(JMPS):
#if k==(JMPS):
      #spops=pth+"PopsJMP"+str(k)+".p"
tpops=pth+"tPopsJMP"+str(JMP)+".p"
      #A=pickle.load(open(spops,"rb"))
B=pickle.load(open(tpops,"rb"))
print("LOADED")

#########################################
#DT=0
#tsx=[]
#tmx=0
#nz=A.keys()[0]
#for ni in A.keys():
#    tx=len(A[ni])
#    tsx.append(tmx)
#    if tx>tmx:
#        tmx=tx

#        nz=ni
#Tmx=max(tsx)

#print tmx, Tmx, nz
#NQ={}
#print("PROCEEDING")
#x1=Tmx
#for i in A.keys():
#    x2=len(A[i])
#    qz=[]
#    dx=x1-x2
#    for ix in range(dx):
#        qz.append(0.0)
#    for ix in range(x2):
#        qz.append(A[i][ix])
#
#    NQ[i]=qz

#print len(NQ.keys())

#print("PROCEEDING2")
#raw_input()

#SN=[]
#for j in range(Tmx):
#    avpopj=0.0
#    for i in NQ.keys():
#        xj=NQ[i][j]
        #print xj, type(xj)
#        avpopj+=xj
        #print i, NQ[i][1:4]
        #raw_input()
#    SN.append(avpopj)

#print len(SN)

#NORMSN=[]
#for i in SN:
#    NORMSN.append(i/len(NQ.keys()))

print("PROCEEDING3")
#raw_input()
##########################################
#print len(A.keys())
#print len(A[A.keys()[0]])
#print len(SN)
#print A.keys()
#raw_input()

##############################################################
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
        comment='Movie support!')
writer = FFMpegWriter(fps=24, metadata=metadata)
fig = plt.figure()
#fig.set_size_inches(5, 4, True)
To=0
Tmx=1001#len(SN)
Tf=Tmx-1
y1=0.0
y2=10000.0

plt.style.use('fivethirtyeight')
movname="NCodeTest"+str(JMP)+".mp4"
with writer.saving(fig,movname, 500):

    plt.plot(B[B.keys()[0]][0:0],linewidth=1.0)
    #plt.ylim((y1,y2))
    plt.xlabel("time  (generations)",fontsize=25)
    plt.ylabel("Pop sizes",fontsize=25)
    formatter = ScalarFormatter()
    formatter.set_powerlimits((-3, 4))
    gca().yaxis.set_major_formatter(formatter)
    #plt.yticks(fontsize=25,style='sci',scilimits=(-20,20))
    fig.suptitle('T= '+str(To), fontsize=24, fontweight='bold')
    writer.grab_frame()
    plt.clf()
    for i in range(1+To,1+Tf):
        print i
        for j in B.keys():
        #    if(B[j][0]>=i):
          plt.plot(B[j][0:i],linewidth=1.0)
            #plt.ylim((y1,y2))

        #plt.plot(SN[0:i],'-',color='b',linewidth=3.0)
        plt.xlabel("time  (generations)",fontsize=25)
        plt.ylabel("Pop sizes",fontsize=25)
        formatter = ScalarFormatter()
        formatter.set_powerlimits((-3, 4))
        gca().yaxis.set_major_formatter(formatter)
        fig.suptitle('T= '+str(i), fontsize=14, fontweight='bold')
        writer.grab_frame()
        plt.clf()
