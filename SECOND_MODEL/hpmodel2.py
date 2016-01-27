#!usr/bin/python

'''
This is an implementation of the second model of pathogen evolution explained in the main website ()
and in the paper ().

You can have help and a full list of options with -h.
There are come more parameters you may want to tinker with directly in the code, i.e. eta and beta,
that affect the probability to have gain of a link, mutation or loss of a link.

Also, you may want to change the way the fitness score is calculated, from linear to Hill function.
In our trials this had lead to approximately the same results, but way more computational effort.
The function is already implemented, just change g_p_mapa with g_p_mapa2.

Please remember to set a seed with -s or --seed as the code is using a default seed, and you will get
the same results multiple times.
'''

import sys
sys.path.append('codes2/')
import itertools as itr
from itertools import product
import os,time
from multiprocessing import Process, Queue
import subprocess as sp
from math import floor
import math as mth
import pickle
import numpy as np
from numpy import random as rng
import modA as mda
import argparse

def jumps(rngseed,par,proc):
    #par[0] number of jumps
    #par[1] target poool size K
    #par[2] max host length
    #par[3] max numb of effector per path at time0
    #par[4] max numb of target per effector gene
    #par[5] mu1
    #par[6] mu2
    #par[7] rates
    #par[8] DT
    #par[9] NH
    #par[10] pmin
    save_pth=args.p
    pmin=par[10]
    Hn={} #host dictionary
    rng.seed(rngseed)
    for jn in xrange(par[0]):
        l=rng.randint(1,par[2]) #length of host genome
        u=mda.newhost.NEWHOST(l,par[1])
        Hn[jn]=u
    pickle.dump(Hn,open(save_pth+str(proc)+"Hosts.p","wb"),protocol=2)
    r=0.0
    j=0
    while r<=.1:
        j++1
        pathogen_dic=mda.newhost.NEWPATHOGEN(par[1],par[3],par[4])#,itr)
        r=sum(mda.gpmap.g_p_mapa(Hn[0],pathogen_dic).values())/float(len(Hn[0]))
    print r
    print Hn[0]
    printuseful(pathogen_dic,Hn[0])
    path_pop={}
    path_pop[0]=[0,[10]]
    path_r={}
    path_r[0]=r
    path_genomes={}
    path_probs={}
    events={}
    path_genomes[0]=pathogen_dic
    evitems = [0, 1, 2, 3]
    jn=0
    rnj=int(max(path_pop.keys()))+1
    for t in xrange(par[0]*par[8]):
        rmax=max(path_r.values())
        npflag=0
        npops=[]
        for el in path_pop:
            if path_pop[el][1][-1]>=0:
                path_probs[el]={}
                path_probs[el]=mda.transformations.probabilities(path_genomes[el],Hn[jn],par[7],path_pop[el][1][-1]) #pathogen,host,rates,pop
                events[el]={}
                events[el]=mda.transformations.events(path_probs[el]);
                if any(ev in events[el].values() for ev in evitems):
                    npthaux1={}
                    npthaux1=mda.transformations.transform(path_genomes[el],events[el],par[1],par[5],par[6],par[4])
                    raux=sum(mda.gpmap.g_p_mapa(Hn[jn],npthaux1).values())/float(len(Hn[jn]))
                    if raux>rmax:
                        path_r[rnj]=raux
                        path_genomes[rnj]=npthaux1
                        npops.append(rnj)
                        rnj+=1
                        npflag=1
        if npflag!=0:
            for jk in npops:
                path_pop[jk]=[t,[10]]

        assert path_pop.keys()==path_genomes.keys()
        flagest=0
        for el in path_pop:
            if path_pop[el][1][-1]>=0:
                flagest=1
                path_pop[el][1].append(mda.population.N_calc(path_pop,path_r,el,path_pop[el][1][-1],par[9]))
        if flagest==0:
            print("ALL-DEATH")
            break

        if ((t%par[8])==(par[8]-1)):
            print "jump in progress"
            pickle.dump( path_pop, open(save_pth+str(proc)+"jump"+str(jn)+"testpops.p", "wb"),protocol=2)
            pickle.dump( path_genomes, open(save_pth+str(proc)+"jump"+str(jn)+"genomes.p", "wb"),protocol=2)
            pickle.dump( path_r, open(save_pth+str(proc)+"jump"+str(jn)+"r.p", "wb"),protocol=2)
            if jn<(par[0]-1):
                print "jump:",jn
                popx={}
                rux={}
                genomesx={}
                jn+=1
                for k in path_pop:
                    if (path_pop[k][1][-1]>10.0):
                        if (path_pop[k][1][-1]>par[10]):
                            popx[k]=[t,[pmin]]
                        else:
                            popx[k]=[t,[path_pop[k][1][-1]]]

                        genomesx[k]=mda.transformations.deepcopy(path_genomes[k])
                        rux[k]=sum(mda.gpmap.g_p_mapa(Hn[jn],genomesx[k]).values())/float(len(Hn[jn]))
                print popx
                path_pop={}
                path_genomes={}
                path_r={}
                print popx
                for k in popx.keys():
                    print popx[k]
                    path_pop[k]=popx[k]
                    path_genomes[k]=genomesx[k].copy()
                    path_r[k]=rux[k]
                del popx
                del genomesx
                del rux
                print "jump completed"
            print jn

    print proc
    print("test completed")

def main():
    parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
    """))
    parser.add_argument("p",help="path to the main directory")
    parser.add_argument("N", type=int, help="number of processes")
    parser.add_argument("j", type=int, help="number of jumps")
    parser.add_argument("DT", type=int, help="time interval between jumps")
    parser.add_argument("-s","--seed", type=int, default=594476731, help="seed for random number generation")
    parser.add_argument("-t","--target", type=int, default=100, help="target pool size / default 100")
    parser.add_argument("-hl","--hostlenght",type=int, default=50, help="max number of target genes in host / default 50")
    parser.add_argument("-e","--effectorinit",type=int, default=3, help="max number of effector at time 0 / default 3")
    parser.add_argument("-p","--promiscuity", type=int, default=10, help="max number of genes targeted by an effector / default 10")
    parser.add_argument("-m","--mutation", type=float, default=0.01, help="mutation rate / default 0.01")
    parser.add_argument("-d", "--duplication", type=float, default=0.01, help="duplication rate / dafult 0.01")
    parser.add_argument("-d2","--deletion", type=float, default=0.01, help="deletion rate / default 0.01")
    parser.add_argument("-h","--hgt", type=float, default=0.01, help="hgt rate / default 0.01")
    parser.add_argument("-NH","--hostpopulation", type=int, default=10**5, help="size of host population")
    args=parser.parse_args()
    seeds=[]
    NUM_PROCESSES=args.N
    SEED=args.seed
    children=[]
    ##########
    #Parameters
    eta=0.5
    beta=1.5-eta
    DT=args.DT
    NJ=args.j #number of jumps
    K=args.target #target pool size
    LHmax=args.hostlength #max host genome length
    NEO=args.effectorinit #max numer of effector per pathogen at time 0
    NTO=args.promiscuity #max number of target for each effector gene
    MU1=eta*(1.0/3)
    MU2=beta*(2.0/3)
    m1=args.mutation #mutation
    m2=args.duplication #duplication
    m3=args.deletion #deletion
    m4=args.hgt #hgt
    NH=args.hostpopulation
    pmin=NH/100.0
    PV=[NJ,K,LHmax,NEO,NTO,MU1,MU2,[m1,m2,m3,m4],DT,NH,pmin] #parameters values
    for process in xrange(NUM_PROCESSES):
        pid = os.fork()
        seeds.append(SEED-(3+process))
        if pid:
            children.append(pid)
        else:
            jumps(seeds[process],PV,process)
            os._exit(0)

    for i, child in enumerate(children):
        os.waitpid(child, 0)

if __name__ == "__main__":
    main()
