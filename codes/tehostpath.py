#!/usr/bin/env python
#INITIALIZATION
import sys
sys.path.append('../codes/')
from pygsl import rng as rn
import math as mth
import numpy as np
import modA as mda
import pickle
import copy
##############################
#Constants and Parameters
SEED=987654320
rk=rn.rng()
rk.set(SEED)
LH=30 #HOST LENGTH
Kh=1000 # Host Urn Size
Kp=100 # Pathoghen Urn Size
C=0.15
tessij=0.75
sohill=0.5
nhill=5
hlpt=[sohill,nhill]
lnsigma=0.702693602048
lnmean=1177.42231142
LNPRT=[lnsigma,lnmean]
lohilleff=8000
lohilltes=5*lohilleff
lohills=[lohilleff,lohilltes]
Ngen=5000
#####################################
mua=1e-5
mub=mua
muc=mua
mud=mua
mue=mua
muf=mua
mug=mua
muh=mua
MU=[mua,mub,muc,mud,mue,muf,mug,muh]
#####################################
bnh=1.0 #Saturation Parameter, check an tune this
Nh=1e6
NJMPS=10
Njmin=1e3
No=1.0

Ngo=10 #number of genes
Tefrac=0.2 #fraction of tes

##############################
#Arrays
Nr={} #Pops
Gr={} #Genomes
Fr={} #Rep Rates
Tr={} #Transition Rates
Lr={} #Lengths
#Neff={} #Number of effs
#Nte={}  #Number of tes
#Nrloc={}
##############################
print("DONE-v")
#Hosts Arrays!!!!
ho=mda.newhost.NEWHOST(LH,Kh,rk) #Creates a new host
HSTa={} #UNCORR
HSTb={} #CORR
HSTc={} #UEVENLENGTH
HSTa[0]=ho
HSTb[0]=ho
HSTc[0]=ho

#print HSTa[0]
#print HSTb[0]
#print HSTc[0]

for j in range(1,NJMPS):
    #print j
    HSTa[j]=mda.newhost.NEWHOST(LH,Kh,rk)
    HSTb[j]=mda.newhostcorr.NEWHOSTCORR(HSTb[j-1],Kh,rk)
    HSTc[j]=mda.newhostvarl.NEWHOSTVARL(LH,Kh,rk)
    #print HSTa[j]
    #print HSTb[j]
    #print HSTc[j]

#raw_input()
##############################
Hx=HSTa[0]
Go=[]
Go=mda.inigenomete.INIGENOMETE(Ngo,Tefrac,rk,C,Kh,tessij,Hx,hlpt,lohills)
Gox=Go[1]
Fo=Go[0]
#for i in Gox.keys():
    #print i, Gox[i][0]
    #print Gox[i][1]
    #print Gox[i][2]
    #print Gox[i][3]
    #print Gox[i][4]
    #raw_input()
#print Fo
#Wo=mda.getwksumte.GETWKSUMTE(Gox,C*LH)
#Fn=mth.exp(Wn)-1.0
#print Fn
print C*Kh, C*LH, Fo
LNSo=mda.getlengthste.GETLENGTHSTE(Gox)
Lg=LNSo[4]
###############################
#################
#Jumps Loop     #
#################
#Arrays
Nr={} #Pops
Gr={} #Genomes
Fr={} #Rep Rates
Tr={} #Transition Rates
Lr={} #Lengths

jmp=0
for i in HSTa:

    Hx=HSTa[i]
    qx='FALSE'
    tk=0

    if jmp==0:
        ##initial state
        Go=[]
        Go=mda.inigenomete.INIGENOMETE(Ngo,Tefrac,rk,C,Kh,tessij,Hx,hlpt,lohills)
        Gox=Go[1]
        Fo=Go[0]
        LNSo=mda.getlengthste.GETLENGTHSTE(Gox)
        strn=0
        sn="jmp"+str(jmp)+"gen"+str(tk)+"strn"+str(strn)
        Gr[sn]=Gox
        Fr[sn]=Fo
        Lr[sn]=LNSo
        Nr[sn]=No
        Nall={}
        popx=[]
        popx.append(No)
        Nall[sn]=popx

    if jmp>0:
        lbjmp=[]
        sxb=0
        Njmin=max(N)
        for i in Nr.keys():
            if Nr[i]>Njmin:
                lbjmp.append(i)
                sxb=1

        if sxb==0:
            print("JUMP UNSUCCESFULL-A")
            break
        else:
            Nall={}
            strn=0
            Gnewx={}
            Fnewx={}
            Nnewx={}
            for lk in lbjmp:
                sn="jmp"+str(jmp)+"gen"+str(tk)+"strn"+str(strn)
                Zn={}
                Zn=mda.jumpchangete.JUMPCHANGETE(Gr[lk],Hx,hlpt,lohills)
                Wnx=mda.getwksumte.GETWKSUMTE(Zn,C*LH)
                Fnx=mth.exp(Wnx)-1.0
                Gnewx[sn]=Zn
                Fnewx[sn]=Fnx
                Nnewx[sn]=Nr[lk]
                Gr={}
                Fr={}
                Nr={}
                for jn in Gnewx.keys():
                    x=[]
                    x=copy.deepcopy(Gnewx[jn])
                    y=[]
                    y=copy.deepcopy(Fnewx[jn])
                    z=[]
                    z=copy.deepcopy(Nnewx[jn])
                    Gr[jn]=x
                    Fr[jn]=y
                    Nr[jn]=z
                    LNSo=mda.getlengthste.GETLENGTHSTE(Gr[jn])
                    Lr[jn]=LNSo

    qx='FALSE'
    tk=0

    #########################
    #In between jumps loop  #
    #########################
    while qx=='FALSE':

        ################
        #Evol Processes
        ################
        Gnew={}
        Fnew={}
        Nnew={}
        flx=0
        Fmax=max(Fr.values())
        sxa=0

        for qi in Nr.keys():

            Trx={}#Rates
            Tux={}#Bool
            Rkx={}#Trans
            Gnx={}#genome
            LNSo=mda.getlengthste.GETLENGTHSTE(Gr[qi])
            Lg=LNSo[4]
            PRTS=[C,LH,Kh,Lg,10e6]



            if(Nr[qi]>0.0):
                sxa=1
                Trx=mda.trateste.TRATESTE(MU,Gr[qi],Nr[qi],PRTS,Fr[qi])#rates
                Tux=mda.taugente.TAUGENTE(Trx,Nr[qi],rk)#yes/no
                Rkx=mda.gsprte.GSPRTE(Trx,Tux,rk)#which
                Gnx=mda.nutegnome.NUTEGNOME(Tux,Rkx,Gr[qi],Hx,hlpt,lohills,rk,Kh,tessij)
                Wox=mda.getwksumte.GETWKSUMTE(Gnx,C*LH)
                Fox=mth.exp(Wox)-1.0
                if (Fox>=Fmax) and (Nr[qi]-No)>1.0:
                    strn+=1
                    flx=1
                    sn="jmp"+str(jmp)+"gen"+str(tk)+"strn"+str(strn)
                    Gnew[sn]=Gnx
                    Fnew[sn]=Fox
                    Nnew[sn]=No
                    Nr[qi]=Nr[qi]-No

        if(sxa==0):
            print("EXTINCTION")
            break

        if flx==1:
            for jn in Gnew.keys():
                x=[]
                x=copy.deepcopy(Gnew[jn])
                y=[]
                y=copy.deepcopy(Fnew[jn])
                z=[]
                z=copy.deepcopy(Nnew[jn])
                Gr[jn]=x
                Fr[jn]=y
                Nr[jn]=z
                LNSo=mda.getlengthste.GETLENGTHSTE(Gr[jn])
                Lr[jn]=LNSo

        for jn in Nr.keys():
            if jn in Nall.keys():
                Nall[jn].append(Nr[jn])
            else:
                x=[]
                x.append(Nr[jn])
                Nall[jn]=x

        ################
        #Pop Update
        ################
        Nold={}
        Nold=mda.dctcpy.DCTCPY(Nr)
        Nr=mda.popteupdate.POPTEUPDATE(Fr,Nold,Nh,bnh)

        if tk%1000==0:
            print tk
        tk+=1.0

        if tk>Ngen:# or DNt<0.01:
            qx='TRUE'
        ###############
    #sreacts="datakerneltest/Rhistory"+str(jmp)+".p"
    spops="newkerneltest/PopsJMP"+str(jmp)+".p"
    spops2="newkerneltest/NtJMP"+str(jmp)+".p"
    slens="newkerneltest/LenJMP"+str(jmp)+".p"
    sfns="newkerneltest/RatesJMP"+str(jmp)+".p"
    sgens="newkerneltest/GenesJMP"+str(jmp)+".p"
    sumpops="newkerneltest/SUMPOPJMP"+str(jmp)+".p"
    pickle.dump(Nall,open(spops,"wb"))
    pickle.dump(Lr,open(slens,"wb"))
    pickle.dump(Fr,open(sfns,"wb"))
    pickle.dump(Gr,open(sgens,"wb"))
    ##pickle.dump(Tr,open(sreacts,"wb"))
    pickle.dump(Nr,open(spops2,"wb"))
    pickle.dump(SN,open(sumpops,"wb"))

    jmp+=1
    ############################
print ("COMPLETED")
