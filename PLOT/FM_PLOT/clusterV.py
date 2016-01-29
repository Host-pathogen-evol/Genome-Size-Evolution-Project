#usr/bin/python
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.pyplot import cm
import pickle
import matplotlib.ticker as mtick
import argparse
parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
"""))
parser.add_argument("p",help="path to the right directory")
parser.add_argument("r", type=int, help="number of runs")
parser.add_argument("j", type=int, help="number of jumps")
parser.add_argument("-s","--singlerun", type=int, default=0, help="single run to plot, choose one without extinctions / default 0")
args=parser.parse_args()
pth=args.p
folder=''
subf=''
runsx='RUN'+str(args.singlerun)+'/'
nx='n0/'
jumps=args.j
xi=range(1,jumps+1) #jumps
dbina=500
dbinb=50
#plt.style.use('bmh')

nX=['n0/','n1/','n2/','n3/','n4/','n5/','n6/','n7/','n8/']
rnX=[]
for mu in range(args.r): ###*changed the number of runs
    if all(os.listdir(pth+'RUN'+str(mu)+'/'+x)==[] for x in nX):
        pass
    else:
        rnX.append('RUN'+str(mu)+'/')                           #RUNS R0,R1,...,
ltj={}
nhj={}
xtj=[]
ytj=[]
ztj=[]
n=0
for j in xi:

    fin=pth+folder+subf+runsx+nx+'pts'+str(j)+'plotdata.p'
    f=open(fin,"rb")
    A=pickle.load(f)
    f.close()
    lj=A[1]
    nj=A[2]
    tj=[]
    for i in range(len(nj)):
        tj.append(i+n*len(nj))

    xtj.append(n*len(nj))
    ytj.append(nj[0])
    ztj.append(lj[0])
    n+=1
    ltj[j]=[tj,lj]
    nhj[j]=[tj,nj]

fig, axesa = plt.subplots(1,figsize=(10, 8))

for i in ltj.keys():
    axesa.plot(ltj[i][0],ltj[i][1],".-", markersize=2, linewidth=1.1)

fig, axesb = plt.subplots(1,figsize=(10, 8))

for i in nhj.keys():
    axesb.plot(nhj[i][0],nhj[i][1],".-", markersize=2, linewidth=1.1)

print xi
ltj={}
ltja={}
ltjb={}
nhj={}
nhja={}
nhjb={}
xtj=[]
ytj=[]
ztj=[]
n=0
for j in xi:

    fin=pth+folder+subf+runsx+nx+'pts'+str(j)+'plotdata.p'
    f=open(fin,"rb")
    A=pickle.load(f)
    f.close()
    lj=A[1]
    lja=A[10]
    ljb=A[11]
    nj=A[2]
    nja=A[3]
    njb=A[4]
    tj=[]
    for i in range(len(nj)):
        tj.append(i+n*len(nj))

    xtj.append(n*len(nj))
    ytj.append(nj[0])
    ztj.append(lj[0])
    n+=1
    ltj[j]=[tj,lj]
    ltja[j]=[tj,lja]
    ltjb[j]=[tj,ljb]
    nhj[j]=[tj,nj]
    nhja[j]=[tj,nja]
    nhjb[j]=[tj,njb]
fig, axesa = plt.subplots(1,figsize=(10, 10))

xtjl=[xtj[1]+i for i in xtj]

axesa.set_ylabel("$Length$ $(bp)$", fontsize=40)
axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
axesa.xaxis.set_tick_params(labelsize=20)
axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
axesa.yaxis.set_tick_params(labelsize=20)
axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
plt.ticklabel_format(style='sci', scilimits=(0,0))
ms=0.1
kn=0

for i in ltj.keys():
    if kn==0:
        axesa.plot(ltj[i][0],ltj[i][1],marker=".",color='black',alpha=0.85,markersize=0.1,label="total length")
        axesa.plot(ltja[i][0],ltja[i][1],marker=".",color='red',alpha=0.85,markersize=0.1,label="Eff length")
        axesa.plot(ltjb[i][0],ltjb[i][1],marker=".",color='blue',alpha=0.85,markersize=0.1,label="T.E. length")
        kn=1
    else:
        axesa.plot(ltj[i][0],ltj[i][1],marker=".",color='black',alpha=0.85,markersize=0.1)
        axesa.plot(ltja[i][0],ltja[i][1],marker=".",color='red',alpha=0.85,markersize=0.1)
        axesa.plot(ltjb[i][0],ltjb[i][1],marker=".",color='blue',alpha=0.85,markersize=0.1)

axesa.legend(loc='best', fancybox=True, framealpha=0.5)

fout=pth+folder+subf
namepth=fout+"typrunlength"

fig.patch.set_alpha(0.5)

fig.savefig(namepth+'.png',format='png' ,dpi=100, bbox_inches='tight')
fig.savefig(namepth+'.svg',format='svg',bbox_inches='tight')

fig, axesb = plt.subplots(1,figsize=(10, 10))

axesb.set_ylabel("$Number$ $of$ $units$", fontsize=40)
axesb.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
axesb.xaxis.set_tick_params(labelsize=20)
axesb.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
axesb.yaxis.set_tick_params(labelsize=20)
axesb.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
plt.ticklabel_format(style='sci', scilimits=(0,0))

ms=1
kn=0

for i in nhj.keys():

    if kn==0:
        axesb.plot(nhj[i][0],nhj[i][1],marker='.',color='black',alpha=0.85,markersize=1.0,label="total number")
        axesb.plot(nhj[i][0],nhja[i][1],marker='.',color='red',alpha=0.85,markersize=1.0,label="Eff number")
        axesb.plot(nhj[i][0],nhjb[i][1],marker='.',color='blue',alpha=0.85,markersize=1.0,label="T.E. number")
        kn=1

    else:
        axesb.plot(nhj[i][0],nhj[i][1],marker='.', color='black',alpha=0.85,markersize=1.0)
        axesb.plot(nhj[i][0],nhja[i][1],marker='.',color='red',alpha=0.85,markersize=1.0)
        axesb.plot(nhj[i][0],nhjb[i][1],marker='.',color='blue',alpha=0.85,markersize=1.0)

axesb.legend(loc='best', fancybox=True, framealpha=0.5)
namepth=fout+"typrunnumbers"
fig.patch.set_alpha(0.5)

fig.savefig(namepth+'.png',format='png' ,dpi=100, bbox_inches='tight')
fig.savefig(namepth+'.svg',format='svg', bbox_inches='tight')

fig, axesb = plt.subplots(1,figsize=(10, 10))
axesb.set_ylabel("$Number$ $of$ $TE's$", fontsize=40)
axesb.set_xlabel("$Number$ $of$ $EG's$",fontsize=40)
axesb.xaxis.set_tick_params(labelsize=20)
axesb.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
axesb.yaxis.set_tick_params(labelsize=20)
axesb.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
plt.ticklabel_format(style='sci', scilimits=(0,0))

color=iter(cm.rainbow(np.linspace(0,1,jumps)))
for i in nhj.keys():
    col=next(color)
    axesb.plot(nhjb[i][1],nhja[i][1],".",color=col,fillstyle='full',markersize=2)

fout=pth+folder+subf
namepth=fout+"randomwalk"

fig.patch.set_alpha(0.5)
fig.savefig(namepth+'.png', dpi=100, bbox_inches='tight')
fig.savefig(namepth+'.svg', bbox_inches='tight')

plt.gcf().canvas.get_supported_filetypes()

n=0
M=0
t=[]

NAV={}
NAVa={}
NAVb={}

LAV={}
LAVa={}
LAVb={}

STDN={}
STDNa={}
STDNb={}

STDL={}
LSTDa={}
LSTDb={}

for pc in nX: #n0, n1, etc
    AVN={}
    AVNa={}
    AVNb={}

    AVL={}
    AVLa={}
    AVLb={}

    for rj in rnX: #R0, R1, R2, ...
        L=[]
        N=[]
        Na=[]
        Nb=[]
        La=[]
        Lb=[]

        for ji in xi: #j1, j2, j2,j3
            fin=pth+folder+subf+ rj + pc +'pts'+str(ji)+'plotdata.p'
            try:
                f=open(fin,"rb")
                A=pickle.load(f)
                f.close()
                lz=A[1]
                nz=A[2]
                nza=A[3]
                nzb=A[4]

                lza=A[10]
                lzb=A[11]

                for k in lz:
                    if M==0:
                        t.append(n)
                        n+=1.0
                    L.append(k)
                for k in nz:
                    N.append(k)
                for k in nza:
                    Na.append(k)
                for k in nzb:
                    Nb.append(k)
                for k in lza:
                    La.append(k)
                for k in lzb:
                    Lb.append(k)
            except IOError:
                pass


        M=1
        AVN[rj]=N
        AVNa[rj]=Na
        AVNb[rj]=Nb
        AVL[rj]=L
        AVLa[rj]=La
        AVLb[rj]=Lb

    avl=[]
    stdl=[]
    avn=[]
    stdn=[]

    avna=[]
    stdna=[]
    avnb=[]
    stdnb=[]

    avla=[]
    stdnla=[]
    avlb=[]
    stdnlb=[]

    print(AVN.keys())

    rj=0
    for tr in t:
        avx=[]
        avx2=[]
        avxa=[]
        avxb=[]
        avx2a=[]
        avx2b=[]

        for mu in AVN.keys():
            try:
                avx.append(AVN[mu][rj])
                avxa.append(AVNa[mu][rj])
                avxb.append(AVNb[mu][rj])
                avx2.append(AVL[mu][rj])
                avx2a.append(AVLa[mu][rj])
                avx2b.append(AVLb[mu][rj])
            except IndexError:
                pass

        avl.append(np.mean(avx2))
        stdl.append(np.std(avx2))

        avn.append(np.mean(avx))
        stdn.append(np.std(avx))

        avna.append(np.mean(avxa))
        stdna.append(np.std(avxa))

        avnb.append(np.mean(avxb))
        stdnb.append(np.std(avxb))


        avla.append(np.mean(avx2a))
        stdnla.append(np.std(avx2a))

        avlb.append(np.mean(avx2b))
        stdnlb.append(np.std(avx2b))

        rj+=1
    NAV[pc]=avn
    NAVa[pc]=avna
    NAVb[pc]=avnb
    LAV[pc]=avl
    LAVa[pc]=avla
    LAVb[pc]=avlb

    STDN[pc]=stdn
    STDL[pc]=stdl
    STDNa[pc]=stdna
    STDNb[pc]=stdnb
    LSTDa[pc]=stdnla
    LSTDb[pc]=stdnlb


print len(t)

fig1, axesa = plt.subplots(1,figsize=(10, 8))
axesa.set_ylabel("$< Lengths >_{Ens}$", fontsize=40)
axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
axesa.xaxis.set_tick_params(labelsize=20)
axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
axesa.yaxis.set_tick_params(labelsize=20)
axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
plt.ticklabel_format(style='sci', scilimits=(0,0))

fig2, axesb = plt.subplots(1,figsize=(10, 10))
axesb.set_ylabel("$<Number$ $of$ $units>_{Ens}$", fontsize=40)
axesb.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
axesb.xaxis.set_tick_params(labelsize=20)
axesb.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
axesb.yaxis.set_tick_params(labelsize=20)
axesb.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
plt.ticklabel_format(style='sci', scilimits=(0,0))

ltn=0

for ck in NAV.keys():

    ytjb=[]
    ytjba=[]
    ytjbb=[]
    ytja=[]
    for i in xtj:
        try:
            ytjb.append(NAV[ck][i])
            ytjba.append(NAV[ck][i])
            ytjbb.append(NAV[ck][i])
            ytja.append(LAV[ck][i])
        except IndexError:
            pass

    if ltn==0:
        axesb.plot(t,NAV[ck],color="black",label="Average Num of Units")
    else:
        axesb.plot(t,NAV[ck],color="black")


    yrrminus=[]
    yrrplus=[]
    l=0
    for sj in NAV[ck]:
        yrrminus.append(sj-STDN[ck][l])
        yrrplus.append(sj+STDN[ck][l])
        l+=1

    axesb.fill_between(t, yrrminus, yrrplus,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

    if ltn==0:
        axesb.plot(t,NAVa[ck],color="red",label="Average Num of E. Units")
    else:
        axesb.plot(t,NAVa[ck],color="red")

    yrrminusa=[]
    yrrplusa=[]
    l=0
    for sj in NAVa[ck]:
        yrrminusa.append(sj-STDNa[ck][l])
        yrrplusa.append(sj+STDNa[ck][l])
        l+=1

    axesb.fill_between(t, yrrminusa, yrrplusa,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

    if ltn==0:
        axesb.plot(t,NAVb[ck],color="blue",label="Average Num of TE's")
    else:
        axesb.plot(t,NAVb[ck],color="blue")

    yrrminusb=[]
    yrrplusb=[]
    l=0
    for sj in NAVb[ck]:
        yrrminusb.append(sj-STDNb[ck][l])
        yrrplusb.append(sj+STDNb[ck][l])
        l+=1

    axesb.fill_between(t, yrrminusb, yrrplusb,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

    yrrminus=[]
    yrrplus=[]
    l=0
    for sj in LAV[ck]:

        yrrminus.append(sj-STDL[ck][l])
        yrrplus.append(sj+STDL[ck][l])
        l+=1
    axesa.fill_between(t, yrrminus, yrrplus,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

    if ltn==0:
        axesa.plot(t,LAV[ck],color="black",label="Average Length")
    else:
        axesa.plot(t,LAV[ck],color="black")

    if ltn==0:
        axesa.plot(t,LAVa[ck],color="red",label="Average EGs Length")
    else:
        axesa.plot(t,LAVa[ck],color="red")

    lyrrminusa=[]
    lyrrplusa=[]
    l=0
    for sj in LAVa[ck]:
        lyrrminusa.append(sj-LSTDa[ck][l])
        lyrrplusa.append(sj+LSTDa[ck][l])
        l+=1

    axesa.fill_between(t, lyrrminusa, lyrrplusa, alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

    if ltn==0:
        axesa.plot(t,LAVb[ck],color="blue",label="Average TEs Length")
        ltn=1
    else:
        axesa.plot(t,LAVb[ck],color="blue")

    lyrrminusb=[]
    lyrrplusb=[]
    l=0
    for sj in LAVb[ck]:
        lyrrminusb.append(sj-LSTDb[ck][l])
        lyrrplusb.append(sj+LSTDb[ck][l])
        l+=1

    axesa.fill_between(t, lyrrminusb, lyrrplusb,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

axesb.legend(loc='best', fancybox=True, framealpha=0.5)
fout=pth+folder+subf
namepth=fout+"averagesl"
fig1.patch.set_alpha(0.5)
fig1.savefig(namepth+'.png', dpi=100, bbox_inches='tight')
fig1.savefig(namepth+'.svg', bbox_inches='tight')

axesa.legend(loc='best', fancybox=True, framealpha=0.5)

namepth=fout+"averagesn"

fig2.patch.set_alpha(0.5)
fig2.savefig(namepth+'.png', dpi=100, bbox_inches='tight')
fig2.savefig(namepth+'.svg', bbox_inches='tight')

for ck in LAV.keys():

    fig, axesa = plt.subplots(1,figsize=(10, 8))
    axesa.plot(t,LAV[ck])
    axesa.stem(xtj,ytja,linefmt='--', markerfmt='bo', basefmt='r-')
    yrrminus=[]
    yrrplus=[]
    l=0
    for sj in LAV[ck]:

        yrrminus.append(sj-STDL[ck][l])
        yrrplus.append(sj+STDL[ck][l])
        l+=1
    axesa.fill_between(t, yrrminus, yrrplus,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

    axesa.plot(t,LAVa[ck])

    lyrrminusa=[]
    lyrrplusa=[]
    l=0
    for sj in LAVa[ck]:
        lyrrminusa.append(sj-LSTDa[ck][l])
        lyrrplusa.append(sj+LSTDa[ck][l])
        l+=1

    axesa.fill_between(t, lyrrminusa, lyrrplusa, alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

    axesa.plot(t,LAVb[ck])
    lyrrminusb=[]
    lyrrplusb=[]
    l=0
    for sj in LAVb[ck]:
        lyrrminusb.append(sj-LSTDb[ck][l])
        lyrrplusb.append(sj+LSTDb[ck][l])
        l+=1

    axesa.fill_between(t, lyrrminusb, lyrrplusb,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

print nX
print rnX
print xi
print LAV.keys()
print folder, subf

ALLSERIES={}
kt=0
n=0
tj=[]
for prt in nX:
    fig, axesa = plt.subplots(1,figsize=(10, 8))
    fig, axesb = plt.subplots(1,figsize=(10, 8))

    axesb.plot(t,NAV[prt],'black')

    yerrminus=[]
    yerrplus=[]
    l=0
    for sj in NAV[prt]:
        yerrminus.append(sj-STDN[prt][l])
        yerrplus.append(sj+STDN[prt][l])
        l+=1

    axesb.fill_between(t, yerrminus, yerrplus,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

    yerrminusb=[]
    yerrplusb=[]
    l=0
    for sj in LAV[prt]:
        yerrminusb.append(sj-STDL[prt][l])
        yerrplusb.append(sj+STDL[prt][l])
        l+=1

    axesa.plot(t,LAV[ck],'black')

    axesa.fill_between(t, yerrminusb, yerrplusb,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

    for rn in rnX:
        nz=[]
        lz=[]
        for jp in xi:
            file= pth+folder+subf+rn+prt+'pts'+str(jp)+'plotdata.p'
            f=open(file,"rb")
            A=pickle.load(f)
            f.close()
            lz.extend(A[1])
            nz.extend(A[2])
            if kt==0:
                for i in range(len(A[1])):
                    tj.append(i+n*len(A[1]))
                n+=1
        kt=1
        print len(tj), len(lz), len(nz)

        axesa.plot(tj,lz)
        axesb.plot(tj,nz)

par=[args.p,args.r,args.j]
name2=pth+"CDATAV_par.p"
pickle.dump(par,open(name2,"wb"), protocol=2)

Data=[t,LAV,NAV,STDN,STDL,NAVa,NAVb,STDNa,STDNb,LAVa,LAVb,LSTDa,LSTDb]
name="CDATAV.p"
pickle.dump(Data,open(name,"wb"), protocol=2)

Data=[t,LAV,NAV,STDN,STDL]
name="CDATAVcomp.p"
pickle.dump(Data,open(name,"wb"), protocol=2)
