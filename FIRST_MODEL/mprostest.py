#import multiprocessing as mp
from multiprocessing import Process, Queue
import subprocess as sp
from math import floor
from pygsl import rng as rn
import Lffit, LffitB
import pdt
import argparse ###*
parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
""")) ###*
parser.add_argument("p",help="path to the main directory") ###*
parser.add_argument("r", type=int, help="number of runs")###*
parser.add_argument("j", type=int, help="number of jumps")###*
parser.add_argument("DT", type=int, help="time interval between jumps") ###*
parser.add_argument("-s","--seed", type=int, default=1239876514, help="seed for random number generation") ###*
parser.add_argument("-p1","--probability1", type=float, default=2e-4, help="probability of hgt for Eff") ###*
parser.add_argument("-p2","--probability2",type=float, default=1.5e-4, help="probability of hgt for TEs") ###*
parser.add_argument("-p3","--probability3",type=float, default=5e-6, help="probability of Eff recombination/mutation") ###*
parser.add_argument("-p4","--probability4", type=float, default=0.5e-7, help="probability of TE duplication") ###*
parser.add_argument("-p5","--probability5", type=float, default=1e-6, help="") ###*
parser.add_argument("-p6", "--probability6", type=float, default=1.0e-4, help="") ###*
parser.add_argument("-p7","--probability7", type=float, default=2.5e-4, help="") ###*
parser.add_argument("-p8","--probability8", type=float, default=6.5e-5, help="") ###*
args=parser.parse_args() ###*
pth=args.p ###*
RUNS=args.r ###*
tn=args.DT ###*
JMPS=args.j ###*
SEED=args.seed ###*
m1=args.probability1 ###*
m2=args.probability2 ###*
m3=args.probability3 ###*
m4=args.probability4 ###*
m5=args.probability5 ###*
m6=args.probability6 ###*
m7=args.probability7 ###*
m8=args.probability8 ###*
rxclr=[]
crinckler=[]
tes=[]
###*pth='../../'
rxclr=Lffit.loaddata(pth+'rxclr.dat')
crinckler=Lffit.loaddata(pth+'crinckler.dat')
tes=Lffit.loaddata(pth+'tes.dat')
print len(rxclr), len(crinckler), len(tes)
RXCLRPTS=[len(rxclr),min(rxclr),max(rxclr)]
CRKPTS=[len(crinckler),min(crinckler),max(crinckler)]
TES=[len(tes),min(tes),max(tes)]

tes= None
rxclr=None
crinckler=None
print RXCLRPTS, CRKPTS, TES

av1=0.5*(RXCLRPTS[2]-RXCLRPTS[1])
av2=0.5*(CRKPTS[2]-CRKPTS[1])
av3=0.5*(TES[2]-TES[1])
Lth=floor((RXCLRPTS[0]+CRKPTS[0]+TES[0])*(1.0/3.0)*(av1+av2+av3))
PL1=[TES[1],TES[2]]
PL2=[CRKPTS[1],RXCLRPTS[2]]
Ntot=RXCLRPTS[0]+CRKPTS[0]+TES[0]
###*SEED=1239876514
#rk=rn.rng()
#rk.set(SEED)
nte=5
neff=10
###*tn=5000
Np=1e6
###*m1=2e-4#1e-5 #hgt effs
###*m2=1.5e-4#hgt te
###*m3=5e-6 #m3=0.02 #eff recomb
###*m4=0.5e-7  #te dup
###*=1e-6  #3.5 #10.50 #eff dup+te
###*m6=1.0e-4 #m6=0.0013  #eff->null
###*m7=2.5e-4 #1e-7 #10*1e-5 #null ->0
###*m8=6.5e-5 #1e-7 #m8=1.0001##eff->0
kn=0.0
beta1=1e-5
beta2=0.001
wo=1.0
################################################################################
def evolx(P,tn,PL1,PL2,gold,rk,nj,Qi,ptj,qij,rnz):

    #print P,tn,PL1,PL2,gold,rk,nj,Qi,ptj
    MU=[P[0],P[1],P[2],P[3],P[4],P[5],P[6],P[7],P[8],P[9],P[10],P[11],P[12]]
    #MU=[Np,m1,m2,m3,m4,m5,m6,m7,m8,Lth,beta1,beta2,wo]
    Ntot=P[13]
    pqr={}
    ltn=[]
    nefft=[]
    lnefft=[]
    ntest=[]
    lntest=[]
    lth=[]
    ngt=[]
    fitn=[]
    trns=[]
    flg='all-good'
    gen={}
    trs={}

    k=0
    for i in gold.keys():
      gl=[]
      if gold[i][0]=='te':
        gl=[gold[i][0],gold[i][1]]
        gen[k]=gl
        k+=1
      if gold[i][0]=='eff':
        if nj==0:
            gl=[gold[i][0],gold[i][1],gold[i][2]]
        else:
            qj=rk.uniform_pos()
            snew=gold[i][2]+(0.01*( 1.0-2.0*rk.uniform_pos() ))
            if ((qj<Qi) and (snew>0.0)):
                gl=[gold[i][0],gold[i][1],snew]
            else:
                gl=[gold[i][0],gold[i][1],0.0]
        gen[k]=gl
        k+=1

    gold=None

    for nk in range(tn):
        trs=Lffit.trates(gen,MU)
        rij,sr =Lffit.montec(trs,rk)
        trns.append(rij)
        if sr!='TRUE':
            pqr[nk]=[rij[0],rij[1],gen]
            ltn.append(Lffit.lent(gen))
            lth.append(Lth)
            wq=Lffit.ft(gen)
            fitn.append(1.0-(wq/(wq+wo)))
            ngt.append(len(gen.keys()))
            n1x=0.0
            n2x=0.0
	    m1x=0.0
            m2x=0.0
            for gk in gen.keys():
                if gen[gk][0]=='eff':
                    n1x+=1
                    m1x+=gen[gk][1]
                if gen[gk][0]=='te':
                    n2x+=1
                    m2x+=gen[gk][1]

            nefft.append(n1x)
            lnefft.append(m1x)
            ntest.append(n2x)
            lntest.append(m2x)

            gu={}
            gu=LffitB.transform(rij,gen,rk, PL1, PL2)
            gen={}
            for i in gu.keys():
                gen[i]=gu[i]
      #gc.collect()
        else:
            flg='sumzero'
            break

        if len(gen.keys())>2000:
            flg='limit-reached'
            break


    ####################
    import os
    po='../RUN'
    nx=str(rnz)+'/n'+str(ptj)
    if not os.path.exists(po+nx):
        os.makedirs(po+nx)
    efflens, telens =Lffit.splitgen(gen)
    print len(efflens), len(telens)
    pthl=po+nx
    #pdt.savedata(lth,ltn,ngt,efflens,telens,P,SEED,pthl,wfitn)
    if telens or efflens:
        #[lth,ltn,ngt,pqr,gen,flg,fitn,trns]
        #lth,ltn,ngt,pqr, gen,info,wfitn,trns
        #print("HELLO")
        #***********add below tn and number of jumps
        pdt.savedata(lth,ltn,ngt,efflens,telens,P,SEED,pthl,fitn,trns,nefft,ntest,lnefft,lntest,tn,JMPS)
        ###*if telens and efflens:
        ###*    pdt.datadisplay(lth,ltn,ngt,efflens,telens,500,50,P,SEED,pthl,fitn,Qi,)
            #del lth,ltn,ngt,pqr,info,wfitn,trns
            #gc.collect()
        ###*else:
        ###*    print("NOT-DATA-TO-SHOW")
    ####################

    qij.put(gen)
    #return gen
###############################################################################
RO=0
###*RUNS=1
for rnz in range(RO,RUNS):
    ###*JMPS=40
    PAR=9
    NUM_PROCESSES = 3*3
    rk=rn.rng()
    rk.set(SEED-rnz)
    Qi=0.1
    gno=Lffit.inigenome(nte,neff,rk,PL1,PL2)
    for i in range(PAR):

        P1=[Np,m1,m2,m3,m4,m5,m6,m7,m8,Lth,beta1,beta2,wo,Ntot]

        for j in range(JMPS):
            qij=Queue()

            if j==0:
                gn={}
                pj=Process(target=evolx, args=(P1,tn, PL1,PL2,gno,rk,j,Qi,i,qij,rnz,))
                pj.start()
                gn=qij.get()

            else:
                gnx={}
                pj=Process(target=evolx, args=(P1,tn, PL1,PL2,gn,rk,j,Qi,i,qij,rnz,))
                pj.start()
                gnx=qij.get()
                gn={}
                for muk in gnx.keys():
                    ak=[]
                    for nuk in gnx[muk]:
                        ak.append(nuk)
                    gn[muk]=ak
        Qi+=0.1
