from math import floor
from pygsl import rng as rn
import gc, sys, Lffit, LffitB, os, time
import pdt
rxclr=[]
crinckler=[]
tes=[]
pth='../../'
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

SEED=987654320
rk=rn.rng()
rk.set(SEED)

nte=5
neff=10
tn=5000
Np=1e6
m1=0.001 #hgt effs
m2=0.01#hgt te
m3=0.1 #m3=0.02 #eff recomb
m4=0.01  #te dup
m5=3.00  #3.5 #10.50 #eff dup+te
m6=0.01 #m6=0.0013  #eff->null
m7=0.0000 #10*1e-5 #null ->0
m8=0.0000 #m8=1.0001##eff->0
kn=0.0
beta1=1e-5
beta2=0.001
wo=1.0
################################################################################
def evolx(P,tn,PL1,PL2,gold,rk,nj,Qi,ptj):

    MU=[P[0],P[1],P[2],P[3],P[4],P[5],P[6],P[7],P[8],P[9],P[10],P[11],P[12]]
    #MU=[Np,m1,m2,m3,m4,m5,m6,m7,m8,Lth,beta1,beta2,wo]
    Ntot=P[13]
    pqr={}
    ltn=[]
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
    po='../'
    nx='n'+str(ptj)
    if not os.path.exists(po+nx):
        os.makedirs(po+nx)
    efflens, telens =Lffit.splitgen(gen)
    print len(efflens), len(telens)
    pthl=po+nx
    #pdt.savedata(lth,ltn,ngt,efflens,telens,P,SEED,pthl,wfitn)
    if telens or efflens:
        #[lth,ltn,ngt,pqr,gen,flg,fitn,trns]
        #lth,ltn,ngt,pqr, gen,info,wfitn,trns
        pdt.savedata(lth,ltn,ngt,efflens,telens,P,SEED,pthl,fitn,trns)
        if telens and efflens:
            pdt.datadisplay(lth,ltn,ngt,efflens,telens,500,50,P,SEED,pthl,fitn)
            #del lth,ltn,ngt,pqr,info,wfitn,trns
            #gc.collect()
        else:
            print("NOT-DATA-TO-SHOW")
    ####################
    return gen
################################################################################
JMPS=5
PAR=9
NUM_PROCESSES = 3*3
rk=rn.rng()
rk.set(SEED)
#gn={}
Qi=0.1
m5=1000.0*(m5/2.0)
m4=2.0*m4
m3=m3/1000.0
gno=Lffit.inigenome(nte,neff,rk,PL1,PL2)

for i in range(PAR):

    start_time = time.time()
    #gno=Lffit.inigenome(nte,neff,rk,PL1,PL2)
    P1=[Np,m1,m2,m3,m4,m5,m6,m7,m8,Lth,beta1,beta2,wo,Ntot]
    pid= os.fork()
    if pid>0:
        child=pid
    else:

        for j in range(JMPS):
            if j==0:
                gn={}
                gn = evolx(P1,tn, PL1,PL2,gno,rk,j,Qi,i)
            else:
                gnx={}
                q=0
                for si in gn.keys():
                    if gn[si][0]=='eff':
                        gnx[q]=[gn[si][0],gn[si][1],gn[si][2]]
                        q+=1
                    if gn[si][0]=='te':
                        gnx[q]=[gn[si][0],gn[si][1]]
                        q+=1
                #del gn
                gn={}
                gn = evolx(P1,tn, PL1,PL2,gnx,rk,j,Qi,i)
        del gn
        os._exit(0)

    os.waitpid(child,0)
    print time.time()- start_time

    Qi+=0.1
    m8+=0.0001
    #m5=10.0*m5
    #del gn
