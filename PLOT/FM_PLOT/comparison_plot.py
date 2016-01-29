#!usr/bin/python
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.pyplot import cm
import argparse
import os
plt.style.use('bmh')
parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
"""))
########each directory has a different DT
parser.add_argument("p1",help="path to the right directory")
parser.add_argument("p2", help="path to the second directory")
parser.add_argument("p3", help="path to the third directory")
parser.add_argument("p4", help="path to the last directory")
parser.add_argument("p5",help="path to the directory no jumps")
args=parser.parse_args()
pth1=args.p1
pth2=args.p2
pth3=args.p3
pth4=args.p4
pthno=args.p5
main_path=[pth1,pth2,pth3,pth4]
print pth1,pth2,pth3,pth4,pthno
##############files with data##########################
n1=pth1+"CDATAV.p"
n2=pth2+"CDATAV.p"
n3=pth3+"CDATAV.p"
n4=pth4+"CDATAV.p"
nno=pthno+"CDATAV.p"
print n1, n2, n3, n4
f1=open(n1,"rb")
NOPE1=pickle.load(f1)
f1.close()
f2=open(n2,"rb")
NOPE2=pickle.load(f2)
f2.close()
f3=open(n3,"rb")
NOPE3=pickle.load(f3)
f3.close()
f4=open(n4,"rb")
NOPE4=pickle.load(f4)
f4.close()
fno=open(nno,"rb")
NOJU=pickle.load(fno)
fno.close()

T1=NOPE1[0]
T2=NOPE2[0]
T3=NOPE3[0]
T4=NOPE4[0]
TNO=NOJU[0]

assert T1==T2==T4

pts1=NOPE1[1].keys()
pts2=NOPE2[1].keys()
pts3=NOPE3[1].keys()
pts4=NOPE4[1].keys()
ptsno=NOJU[1].keys()

assert pts1==pts2==pts3==pts4

d={}
d['DT5000']=["$\Delta T=5.0\\times 10^3$",NOPE1,T1]
d['DT10000']=["$\Delta T= 1.0\\times 10^4$",NOPE2,T2]
d['DT15000']=["$\Delta T= 1.5 \\times 10^4$",NOPE3,T3]
d['DT20000']=["$\Delta T= 2.0\\times 10^4$",NOPE4,T4]
def averaging(der_list):
    n=0
    to_plot=[]
    sn=0.0
    for x in der_list: #averaging
        sn+=x
        n+=1
        to_plot.append(sn/n)
    return to_plot

def sampling(lista):
    slices=[lista[i:i + 10] for i in range(0, len(lista), 10)]
    res=[]
    for x in slices:
        res.append(np.mean(x))
    return res

######################################################################################################
#plotting total length over time for same c and different DT (it miss the infinity and color map)
######################################################################################################
c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Lengths >$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    color=iter(cm.rainbow(np.linspace(0,1,5)))

    col=next(color)
    axesa.plot(T1,NOPE1[1][x],c=col,label="$\Delta T=5.0\\times 10^3$")
    col=next(color)
    axesa.plot(T2,NOPE2[1][x],c=col,label="$\Delta T= 1.0\\times 10^4$")
    col=next(color)
    axesa.plot(T3,NOPE3[1][x],c=col,label="$\Delta T= 1.5 \\times 10^4$")
    col=next(color)
    axesa.plot(T4,NOPE4[1][x],c=col,label="$\Delta T= 2.0\\times 10^4$")
    col=next(color)
    axesa.plot(TNO,NOJU[1]['n0/'],c=col, label="$\Delta T=\infty$")

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot'+str(c-0.1)+'.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot'+str(c-0.1)+'.svg',bbox_inches='tight')

####################################################################################################
#plotting len of eff and tes over time for same c and different DT
####################################################################################################
c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Lengths >_{Ens}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    color=iter(cm.rainbow(np.linspace(0,1,5)))

    col=next(color)
    axesa.plot(T1,NOPE1[9][x],c=col,ls='-',label="$\Delta T=5.0\\times 10^3$")
    axesa.plot(T1,NOPE1[10][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T2,NOPE2[9][x],c=col,ls='-',label="$\Delta T= 1.0\\times 10^4$")
    axesa.plot(T2,NOPE2[10][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T3,NOPE3[9][x],c=col,ls='-',label="$\Delta T= 1.5 \\times 10^4$")
    axesa.plot(T3,NOPE3[10][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T4,NOPE4[9][x],c=col,ls='-',label="$\Delta T= 2.0\\times 10^4$")
    axesa.plot(T4,NOPE4[10][x],c=col,ls='--')
    col=next(color)
    axesa.plot(TNO,NOJU[9]['n0/'],c=col,ls='-', label="$\Delta T=\infty$")
    position1=min([NOPE1[9][x][-100000],NOPE2[9][x][-100000],NOPE3[9][x][100000],NOPE4[10][x][-100000],NOJU[9]['n0/'][-100000]])-1000
    plt.annotate('effector genes',xy=(100000, position1),size='x-large',ha="center",va='top',bbox=dict(alpha=0.5,color='white',boxstyle='round'))
    axesa.plot(TNO,NOJU[10]['n0/'],c=col,ls='--')
    position2=min([NOPE1[10][x][-100000],NOPE2[10][x][-100000],NOPE3[10][x][-100000],NOPE4[10][x][-100000],NOJU[10]['n0/'][-100000]])-1000
    plt.annotate('TEs',xy=(100000,position2),size='x-large',ha="center",va='top',bbox=dict(alpha=0.5,color='white',boxstyle='round'))

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    axesa.set_title(titstr, fontsize=40)

    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_te'+str(c)+'.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_te'+str(c)+'.svg',bbox_inches='tight')

    c+=0.1

################################################################################################
#plotting total number of units over time for different c and same DT (it misses infinity and color map)
#################################################################################################
c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Number$ $of$ $units >_{Ens}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    color=iter(cm.rainbow(np.linspace(0,1,5)))

    col=next(color)
    axesa.plot(T1,NOPE1[2][x],c=col,label="$\Delta T=5.0\\times 10^3$")
    col=next(color)
    axesa.plot(T2,NOPE2[2][x],c=col,label="$\Delta T= 1.0\\times 10^4$")
    col=next(color)
    axesa.plot(T3,NOPE3[2][x],c=col,label="$\Delta T= 1.5 \\times 10^4$")
    col=next(color)
    axesa.plot(T4,NOPE4[2][x],c=col,label="$\Delta T= 2.0\\times 10^4$")
    col=next(color)
    axesa.plot(TNO,NOJU[2]['n0/'],c=col, label="$\Delta T=\infty$")

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot'+str(c-0.1)+'.png',format='png' ,dpi=100, bbox_inches='tight')#done
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot'+str(c-0.1)+'.svg',bbox_inches='tight')

################################################################################################
#plotting number of tes and eff over time for same c and different DT
#############################################################################################
c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Number$ $of$ $units >_{Ens}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    color=iter(cm.rainbow(np.linspace(0,1,5))) ###change 4 when adding new

    col=next(color)
    axesa.plot(T1,NOPE1[5][x],c=col,ls='-',label="$\Delta T=5.0\\times 10^3$")
    axesa.plot(T1,NOPE1[6][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T2,NOPE2[5][x],c=col,ls='-',label="$\Delta T= 1.0\\times 10^4$")
    axesa.plot(T2,NOPE2[6][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T3,NOPE3[5][x],c=col,ls='-',label="$\Delta T= 1.5 \\times 10^4$")
    axesa.plot(T3,NOPE3[6][x],c=col,ls='--')
    col=next(color)
    axesa.plot(T4,NOPE4[5][x],c=col,ls='-',label="$\Delta T= 2.0\\times 10^4$")
    axesa.plot(T4,NOPE4[6][x],c=col,ls='--')
    col=next(color)
    axesa.plot(TNO,NOJU[5]['n0/'],c=col,ls='-',label="$\Delta T=\infty$")
    position1=min([NOPE1[5][x][-100000],NOPE2[5][x][-100000],NOPE3[5][x][100000],NOPE4[5][x][-100000],NOJU[5]['n0/'][-100000]])-100
    plt.annotate('effector genes',xy=(100000, position1),size='x-large',ha="center",va='top',bbox=dict(alpha=0.5,color='white',boxstyle='round'))
    axesa.plot(TNO,NOJU[6]['n0/'],c=col,ls='--')
    position2=min([NOPE1[6][x][-100000],NOPE2[6][x][-100000],NOPE3[6][x][-100000],NOPE4[6][x][-100000],NOJU[6]['n0/'][-100000]])-100
    plt.annotate('TEs',xy=(100000,position2),size='x-large',ha="center",va='top',bbox=dict(alpha=0.5,color='white',boxstyle='round'))

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(c-0.1)+'.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(c-0.1)+'.svg',bbox_inches='tight')

####################################################################################################################################
#same DT different c value
###################################################################################################################################

for x in d:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Number$ $of$ $units >$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    c=0.1

    color=iter(cm.rainbow(np.linspace(0,1,len(pts1))))

    lis1=[]
    lis2=[]

    for y in pts1:

        print x, y
        col=next(color)
        axesa.plot(d[x][2],d[x][1][5][y],c=col,ls='-',label='$c='+str(c)+'$')
        axesa.plot(d[x][2],d[x][1][6][y],c=col,ls='--')
        lis1.append(d[x][1][5][y][-100000])
        lis2.append(d[x][1][6][y][-100000])

        c+=0.1

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    position1=min(lis1)-100
    plt.annotate('effector genes',xy=(100000, position1),size='x-large',ha="center",va='top',bbox=dict(alpha=0.5,color='white',boxstyle='round'))
    position2=min(lis2)-100
    plt.annotate('TEs',xy=(100000,position2),size='x-large',ha="center",va='top',bbox=dict(alpha=0.5,color='white',boxstyle='round'))

    titstr=d[x][0]
    print titstr
    axesa.set_title(titstr, fontsize=40)

    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(x)+'.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(x)+'.svg',bbox_inches='tight')

################################################################################################################
for x in d:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Lengths >$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    c=0.1

    color=iter(cm.rainbow(np.linspace(0,1,len(pts1))))

    lis1=[]
    lis2=[]

    for y in pts1:

        col=next(color)
        axesa.plot(d[x][2],d[x][1][9][y],c=col,ls='-',label='$c='+str(c)+'$')
        axesa.plot(d[x][2],d[x][1][10][y],c=col,ls='--')
        lis1.append(d[x][1][9][y][-100000])
        lis2.append(d[x][1][10][y][-100000])

        c+=0.1

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    position1=min(lis1)-1000
    plt.annotate('effector genes',xy=(100000, position1),size='x-large',ha="center",va='top',bbox=dict(alpha=0.5,color='white',boxstyle='round'))
    position2=min(lis2)-1000
    plt.annotate('TEs',xy=(100000,position2),size='x-large',ha="center",va='top',bbox=dict(alpha=0.5,color='white',boxstyle='round'))

    titstr=d[x][0]
    print titstr
    axesa.set_title(titstr, fontsize=40)

    axesa.set_xlim([0,200000])
    #axesa.set_xlim([0,80000])

    fig.patch.set_alpha(0.5)
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_Te'+str(x)+'.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_Te'+str(x)+'.svg',bbox_inches='tight')
