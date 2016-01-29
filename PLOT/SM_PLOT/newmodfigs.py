#!usr/bin/python

import matplotlib.pyplot as plot
import pickle
import numpy as np
import matplotlib.ticker as mtick
import argparse

parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
"""))
parser.add_argument("p",help="path to the right directory")
parser.add_argument("r", type=int, help="number of runs")
parser.add_argument("j", type=int, help="number of jumps")
parser.add_argument("g",type=int, help="time gap between jumps")
args=parser.parse_args()
pna='jump'
pnb='testpops.p'

NJMP=args.j
DT=args.g
process=args.r
pth=args.p

for nproc in xrange(process):
    for nj in xrange(NJMP):
        fin=str(nproc)+pna+str(nj)+pnb
        print fin

        f=open(pth+fin,"rb")
        A=pickle.load(f)
        f.close()

        fig, axes = plot.subplots(1, 1, figsize=(20, 8))

        titstr='Population sizes evolution jump='+str(nj)
        print titstr
        axes.set_title(titstr, fontsize=35)
        axes.set_ylabel("$N_j(t)$",fontsize=30)
        axes.set_xlabel("Time t (Generations)",fontsize=30)

        axes.xaxis.set_tick_params(labelsize=10)
        axes.yaxis.set_tick_params(labelsize=10)

        tij=[]

        for i in A.keys():
            ti=range(A[i][0],A[i][0]+len(A[i][1]))
            axes.plot(ti,A[i][1],'-',label=str(i))
            tij.append(A[i][0])

        #plot.ylim(0.0, 150000)
        plot.xlim(min(tij),min(tij)+DT)
        axes.tick_params(labelsize=30)

        fig.patch.set_alpha(0.5)
        namefig='typevol'+str(nj)+'.png'
        fig.savefig(pth+str(nproc)+namefig,dpi=100, bbox_inches='tight')
        plot.savefig(pth+str(nproc)+'typevol'+str(nj)+'.svg', bbox_inches='tight')
        plot.close(fig)

    fig, axes = plot.subplots(1, 1, figsize=(20, 8))

    titstr='Population sizes evolution after several host jumps'
    print titstr
    axes.set_title(titstr, fontsize=35)
    axes.set_ylabel("$N_j(t)$",fontsize=30)
    axes.set_xlabel("Time t (Generations)",fontsize=30)

    ts=[]
    Rs=[]

    for nj in xrange(NJMP):
        fin=str(nproc)+pna+str(nj)+pnb
        print fin

        f=open(pth+fin,"rb")
        A=pickle.load(f)
        f.close()

        tij=[]
        for i in A.keys():
            ti=range(A[i][0],A[i][0]+len(A[i][1]))
            axes.plot(ti,A[i][1],'-',label=str(i))
            tij.append(A[i][0])
        Rs.append(150000)
        ts.append(min(tij))

        #plot.ylim(0.0, 150000)

    markerline, stemlines, baseline=axes.stem(ts,Rs,linefmt='--', markerfmt='.', basefmt='',stemlineswidth=0.1)
    plot.setp(stemlines, 'linewidth', 1)
    axes.tick_params(labelsize=30)

    fig.patch.set_alpha(0.5)
    namefig='typevol.png'

    plot.savefig(pth+str(nproc)+namefig, dpi=100, bbox_inches='tight')
    plot.savefig(pth+str(nproc)+'typevol.svg', bbox_inches='tight')
    plot.close(fig)

    fig, axes = plot.subplots(1, 1, figsize=(20, 8))

    titstr='Evolution of $r_{j,n}$ after several host jumps\n'
    print titstr
    axes.set_title(titstr, fontsize=35)
    axes.set_ylabel("$r_{j,n}(t)$",fontsize=30)
    axes.set_xlabel("Strain label",fontsize=30)
    #axesb.set_xlim([0, 15])
    axes.xaxis.set_tick_params(labelsize=10)
    axes.yaxis.set_tick_params(labelsize=10)
    tsmin=[]
    tsmax=[]
    Rs=[]

    for nj in xrange(NJMP):
        fin=str(nproc)+pna+str(nj)+"r.p"

        f=open(pth+fin,"rb")
        R=pickle.load(f)
        f.close()

        colors = list("rgbcmyk")
        x=[]
        y=[]
        for k in R.keys():
            x.append(k)
        x.sort()
        for k in x:
            y.append(R[k])
        axes.plot(x,y,"-o")
        tsmin.append(min(x))
        tsmax.append(max(x))
        Rs.append(1.0)
        axes.tick_params(labelsize=30)

        plot.xlim(0.0,max(x)+5)

    rects=[]
    for j in xrange(0,len(tsmin)-2):
        rects.append([tsmin[j+1],tsmax[j]])
    print rects

    for q in rects:
         axes.fill_between(q, [0,0], [1,1], facecolor='blue', alpha=0.5)

    fig.patch.set_alpha(0.5)
    namefig='rratestyp.png'

    plot.savefig(pth+str(nproc)+namefig, dpi=100, bbox_inches='tight')
    plot.savefig(pth+str(nproc)+'rratestyp.svg', bbox_inches='tight')
    plot.close(fig)

    fig, axes = plot.subplots(1, 1, figsize=(20, 8))
    titstr='Typical evolutionary trajectory of the number of EGs\n'
    print titstr
    axes.set_title(titstr, fontsize=35)
    axes.set_ylabel("$n_{e,j}(t)$",fontsize=39)
    axes.set_xlabel("Strain label",fontsize=30)
    axes.xaxis.set_tick_params(labelsize=30)
    axes.yaxis.set_tick_params(labelsize=30)
    tsmin=[]
    tsmax=[]
    Rs=[]

    for nj in xrange(NJMP):
        fin=str(nproc)+pna+str(nj)+"genomes.p"
        print fin

        f=open(pth+fin,"rb")
        gr=pickle.load(f)
        f.close()

        x=[]
        y=[]
        for k in gr.keys():
            x.append(k)
        x.sort()
        for k in x:
            y.append(len(gr[k]))

        axes.plot(x,y,"-o")

    fig.patch.set_alpha(0.5)
    namefig='typngenevol.png'

    plot.savefig(pth+str(nproc)+namefig, dpi=100, bbox_inches='tight')
    plot.savefig(pth+str(nproc)+'typngenevol.svg', bbox_inches='tight')
    plot.close(fig)

    Gn={}
    for nj in xrange(NJMP):
        fin=str(nproc)+pna+str(nj)+"genomes.p"

        f=open(pth+fin,"rb")
        Gn[nj]=pickle.load(f)
        f.close()

    fin=str(nproc)+"Hosts.p"
    f=open(pth+fin,"rb")
    Hn=pickle.load(f)
    f.close()
    for q in Hn.keys():
        print Hn[q]

    print len(Gn.keys())
    import numpy as np

    K={}
    Kb={}
    for j in Gn.keys():
        Kj={}
        Kk={}
        print("JMP: %d"%j)
        print Gn[j].keys()
        for k in Gn[j].keys():
            print("HOST:")
            print Hn[j]
            print("GENOME: %d"%k)
            print("----------")
            print Gn[j][k].keys()
            nkx=[]
            nka=[]
            nkb=[]
            nkc=[]
            for l in Gn[j][k].keys():
                print("GENE: %d"%l)
                print Gn[j][k][l].keys()
                nkx.append(len(Gn[j][k][l].keys()))
                for zj in Gn[j][k][l].keys():
                    if zj not in nka:
                        nka.append(zj)
                u=set(Gn[j][k][l]).intersection(Hn[j])
                v=list(u)
                print v
                for zj in v:
                    if zj not in nkc:
                        nkc.append(zj)
                nkb.append(len(v))
            nkxb=np.mean(nkx)
            nkbb=np.mean(nkb)
            nkab=float(len(nka))/float(len(Hn[j]))
            nkcb=float(len(nkc))/float(len(Hn[j]))
            print nkx,nkxb #genes degree
            print nkb,nkbb #degree targets in the host
            print nka,nkab #full target set
            print nkc,nkcb #targets present in host
            Kj[k]=[nkx,nkb,nka,nkc]
            Kk[k]=[nkxb,nkbb,nkab,nkcb]
            print("===========")
        K[j]=Kj
        Kb[j]=Kk

    print len(K.keys())
    with open('degslists.pickle', 'wb') as kdict:
        pickle.dump(K, kdict)
    print len(Kb.keys())
    with open('degs.pickle', 'wb') as kdict:
        pickle.dump(Kb, kdict)

    fig, axes = plot.subplots(1, 1, figsize=(20, 8))

    titstr='Interactome Patterns'
    print titstr
    axes.set_title(titstr, fontsize=35)
    axes.set_xlabel("Strain label",fontsize=30)
    axes.tick_params(labelsize=30)

    axes.set_xlim([0, 280])
    N=len(K.keys())
    rectsa=[]
    rectsb=[]

    for j in xrange(0,N):
        ypta=[]
        yptb=[]
        yptc=[]
        yptd=[]

        print K[j].keys()
        print Hn[j]
        for k in K[j].keys():
            ypta.append(np.mean(K[j][k][0]))
            yptb.append(np.mean(K[j][k][1]))
        axes.plot(K[j].keys(),ypta,'p')#,label=str(i))
        axes.plot(K[j].keys(),yptb,'*')#,label=str(i))

        rectsa.append(max(K[j].keys()))
        rectsb.append(min(K[j].keys()))

    rectsa=rectsa[:-1]
    rectsb.pop(0)
    for k in xrange(len(rectsa)):
         axes.fill_between([rectsb[k],rectsa[k]], [0,0], [12,12], facecolor='blue', alpha=0.5)

    axes.plot([-5], [5], 'p', color='black',label="strain EG's mean degree")
    axes.plot([-5], [4], '*', color='black',label="strain EG's mean degree present in host")

    leg=plot.legend(loc="best", markerscale=2., numpoints=1, fontsize=20)
    leg.get_frame().set_alpha(0.5)
    namefig='degpatterns'
    fig.savefig(pth+str(nproc)+namefig+'.png',dpi=100, bbox_inches='tight')
    plot.savefig(pth+str(nproc)+namefig+'.svg', bbox_inches='tight')

    fig, axes = plot.subplots(1, 1, figsize=(20, 8))

    titstr='Promiscousity Patterns'
    print titstr
    axes.set_title(titstr, fontsize=35)
    axes.set_xlabel("Strain label",fontsize=30)

    axes.tick_params(labelsize=30)

    N=len(K.keys())
    rectsa=[]
    rectsb=[]

    for j in xrange(0,N):
        ypta=[]
        yptb=[]
        yptc=[]
        yptd=[]

        print K[j].keys()
        print Hn[j]
        for k in K[j].keys():

            yptc.append( float (len(K[j][k][2]))/float(len(Hn[j]))  )

        axes.plot(K[j].keys(),yptc,'o-')#,label=str(i))

        rectsa.append(max(K[j].keys()))
        rectsb.append(min(K[j].keys()))

    rectsa=rectsa[:-1]
    rectsb.pop(0)
    for k in xrange(len(rectsa)):
         axes.fill_between([rectsb[k],rectsa[k]], [0,0], [100,100], facecolor='blue', alpha=0.5)

    axes.plot([-5], [3], 'o', color='black',label="relative number of targets present")
    axes.plot([-5], [2], 's', color='black',label="relative number of targets in host")
    axes.set_yscale('log')

    leg=plot.legend(loc="best", markerscale=2., numpoints=1, fontsize=20)
    leg.get_frame().set_alpha(0.5)
    namefig='prompatterns'
    fig.savefig(pth+str(nproc)+namefig+'.png',dpi=100, bbox_inches='tight')
    plot.savefig(pth+str(nproc)+namefig+'.svg', bbox_inches='tight')
