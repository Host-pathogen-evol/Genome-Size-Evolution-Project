import pickle
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
from pylab import *

pth='newkerneltest/'

JMPS=0

#for k in range(JMPS):

#spops=pth+"PopsJMP"+str(k)+".p"
tpops=pth+"tPopsJMP"+str(JMPS)+".p"
#A=pickle.load(open(spops,"rb"))
B=pickle.load(open(tpops,"rb"))
print("LOADED")

##########################################
print("ADDING")
sn=len(B[B.keys()[0]])
print sn
SN=[]

for i in range(sn):
  snx=0.0
  for j in B.keys():
    snx+=B[j][i]
  SN.append(snx)
#    print mu

print("COMPLETED")
raw_input()
#########################################
print("PROCEEDING3")
##############################################################
FFMpegWriter = manimation.writers['ffmpeg']
metadata = dict(title='Movie Test', artist='Matplotlib',
        comment='Movie support!')
writer = FFMpegWriter(fps=24, metadata=metadata)
fig = plt.figure()
#fig.set_size_inches(5, 4, True)
To=0
Tmx=5001#len(SN)
Tf=Tmx-1
y1=0.0
y2=10000.0

plt.style.use('fivethirtyeight')
movname="TPALLNCodeTest"+str(JMPS)+".mp4"
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

        plt.plot(SN[0:i],'-',color='b',linewidth=3.0)
        plt.xlabel("time  (generations)",fontsize=25)
        plt.ylabel("Pop sizes",fontsize=25)
        formatter = ScalarFormatter()
        formatter.set_powerlimits((-3, 4))
        gca().yaxis.set_major_formatter(formatter)
        fig.suptitle('T= '+str(i), fontsize=14, fontweight='bold')
        writer.grab_frame()
        plt.clf()
