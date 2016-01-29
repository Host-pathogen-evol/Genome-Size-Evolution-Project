#!usr/bin/python
import pickle
import matplotlib.pyplot as plt
import matplotlib.lines as lns
import matplotlib.ticker as mtick
from matplotlib.pyplot import cm
import numpy as np
import argparse
import os
plt.style.use('bmh')
parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
provide DT5000, 10000, 15000, 20000 and infinity in this order
"""))
parser.add_argument("p1",help="path to the right directory")
parser.add_argument("p2",help='path to 2nd directory')
parser.add_argument("p3",help='path to 3rd directory')
parser.add_argument("p4",help='path to 4th directory')
parser.add_argument("p5",help='path to 5th directory')
parser.add_argument("r", type=int, help="number of runs")
args=parser.parse_args()
pth1=args.p1
pth2=args.p2
pth3=args.p3
pth4=args.p4
pth5=args.p5
RUNS=args.r

def frequenze(dati,larghezza):
    val_min=0
    val_max=max(dati)
    d_func={}
    tot=(val_max/larghezza)+1
    for x in range(int(tot+1)):
        d_func[x]=0
    for el in dati:
        for x in d_func:
            if el<x*larghezza+larghezza and el>=x*larghezza:
                d_func[x]+=1
                pass
    classi=[]
    occorrenze=[]
    for x in d_func:
        classi.append(x*larghezza)
        occorrenze.append(d_func[x])
    return classi, occorrenze

nX=['n0/','n1/','n2/','n3/','n4/','n5/','n6/','n7/','n8/']
diz_pths={pth1:[nX],pth2:[nX],pth3:[nX],pth4:[nX],pth5:[['n0/']]}
diz_labels={pth1:"$\Delta T=5.0\\times 10^3$",pth2:"$\Delta T= 1.0\\times 10^4$",pth3:"$\Delta T= 1.5 \\times 10^4$",pth4:"$\Delta T= 2.0\\times 10^4$",pth5:"$\Delta T=\infty$"}
diz_name={pth1:'5000',pth2:'10000',pth3:'15000',pth4:'20000',pth5:'infin'}

for key in diz_pths:
    rnX=[]
    for mu in range(RUNS): #not considering extinctions
        if all(os.listdir(key+'RUN'+str(mu)+'/'+x)==[] for x in diz_pths[key][0]):
            pass
        else:
            rnX.append('RUN'+str(mu)+'/')
    diz_pths[key].append(rnX)

#plotting distribution of len for each c value comparing different DTs
for c_value in nX:

    for time_gap in [pth41,pth2,pth3,pth4,pth5]:

        fig, axesa = plt.subplots(1,figsize=(16, 8))
        if time_gap==pth1:
            jumps=40
        elif time_gap==pth2:
            jumps=20
        elif time_gap==pth3:
            jumps=13
        elif time_gap==pth4:
            jumps=10
        elif time_gap==pth5:
            jumps=10
        color=iter(cm.rainbow(np.linspace(0,1,jumps)))
        labels=[]
        line2d=[]

        if time_gap!=pth5:
            for run in diz_pths[time_gap][1]:
                j=1
                fin=time_gap+run+c_value+'pts'+str(j)+'plotdata.p'
                while os.path.exists(fin):
                    print fin
                    f=open(fin,"rb")
                    A=pickle.load(f)
                    f.close()
                    efflen=A[5]
                    j+=1
                    fin=time_gap+run+c_value+'pts'+str(j)+'plotdata.p'

                    histval=frequenze(efflen,100)
                    classi=histval[0]
                    occorrenze=histval[1]

                    axesa.set_ylabel("$Frequency$", fontsize=40)
                    axesa.set_xlabel("$Lengths$",fontsize=40)
                    axesa.xaxis.set_tick_params(labelsize=20)
                    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
                    axesa.yaxis.set_tick_params(labelsize=20)
                    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
                    plt.ticklabel_format(style='sci', scilimits=(0,0))

                    print j-1
                    col=next(color)
                    plt.scatter(classi,occorrenze, color=col,label=diz_labels[time_gap],alpha=.5)
                    plt.plot(classi, occorrenze, color=col, ls='--', alpha=.2)

                    line2d.append(lns.Line2D(range(len(efflen)),efflen,color=col,ls='solid'))
                    labels.append(j-1)
                else:
                    break
        else:
            for run in diz_pths[time_gap][1]:
                j=1
                fin=time_gap+run+'n0/'+'pts'+str(j)+'plotdata.p'
                while os.path.exists(fin):
                    print fin
                    f=open(fin,"rb")
                    A=pickle.load(f)
                    f.close()
                    efflen=A[5]
                    j+=1
                    fin=time_gap+run+'n0/'+'pts'+str(j)+'plotdata.p'

                    histval=frequenze(efflen,100)
                    classi=histval[0]
                    occorrenze=histval[1]

                    axesa.set_ylabel("$Frequency$", fontsize=40)
                    axesa.set_xlabel("$Lengths$",fontsize=40)
                    axesa.xaxis.set_tick_params(labelsize=20)
                    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
                    axesa.yaxis.set_tick_params(labelsize=20)
                    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
                    plt.ticklabel_format(style='sci', scilimits=(0,0))

                    print j-1
                    col=next(color)
                    plt.scatter(classi,occorrenze, color=col,label=diz_labels[time_gap],alpha=.5)
                    plt.plot(classi, occorrenze, color=col, ls='--', alpha=.2)

                    line2d.append(lns.Line2D(range(len(efflen)),efflen,color=col,ls='solid'))
                    labels.append(j-1)

                else:
                    break

    box = axesa.get_position()
    axesa.set_position([box.x0, box.y0 + box.height * 0.1,box.width, box.height * 0.9])
    axesa.set_xlim([-100,2500])

    # Put a legend below current axis
    leg=axesa.legend(tuple(line2d),tuple(labels),loc='best',fancybox=True, shadow=True, ncol=5)
    #leg.get_frame().set_alpha(0.5)
    axesa.legend(tuple(line2d),tuple(labels),loc='upper center', bbox_to_anchor=(0.5, -0.15),fancybox=True, shadow=True, ncol=8)

    titstr=diz_labels[time_gap]+'$, c='+str((int(c_value[-2])+1)/10.0)+'$'
    print titstr
    plt.suptitle(titstr, fontsize=40)
    plt.legend(tuple(line2d),tuple(labels),loc='bottom center')
    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'lendistribution_plot_eff'+str((int(c_value[-2])+1)/10.0)+'_'+diz_name[time_gap]+'.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'lendistribution_plot_eff'+str((int(c_value[-2])+1)/10.0)+'_'+diz_name[time_gap]+'.svg', bbox_inches='tight')
