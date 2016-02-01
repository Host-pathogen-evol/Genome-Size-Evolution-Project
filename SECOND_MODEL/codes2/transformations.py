import itertools as itr
from numpy import random as rk
import modA as mda
import math

#muation,deletion,dulication,hgt,add-lose target
def deepcopy(dictionary):
    new_dic={}
    for key in dictionary:
        new_dic[key]=dictionary[key].copy()
    return new_dic

def tgain(pathogen,eff,K):
    new_pathogen=deepcopy(pathogen)
    zk=rk.randint(1,K+1)
    while zk in new_pathogen[eff]:
        zk=rk.randint(1,K+1)
    new_pathogen[eff][zk]=rk.random()
    return new_pathogen

def tremove(pathogen,eff):

    if(len(pathogen[eff].keys())>1):
        new_pathogen=deepcopy(pathogen)
        removethis=rk.choice(new_pathogen[eff].keys())
        del new_pathogen[eff][removethis]
    else:
        new_pathogen={}
        for key in pathogen:
            if key!=eff:
                new_pathogen[key]=pathogen[key].copy()

    return new_pathogen

def mutation(pathogen,eff,K,mu1,mu2,nto):
    new_pathogen=deepcopy(pathogen)
    for target in new_pathogen[eff]:
        y=rk.randn()
        new_pathogen[eff][target]+=y
        if new_pathogen[eff][target]<0.0:
            new_pathogen[eff][target]=0.0
    ranx=rk.random()
    if ranx<mu1 and len(new_pathogen[eff].keys())<nto:
        new_pathogen=tgain(new_pathogen,eff,K)
    elif ranx>=mu2:
        new_pathogen=tremove(new_pathogen,eff)
    return new_pathogen

def deletion(pathogen,eff):
    new_pathogen={}
    for key in pathogen:
        if key!=eff:
            new_pathogen[key]=pathogen[key].copy()
    return new_pathogen

def duplication(pathogen,eff):
    new_pathogen=deepcopy(pathogen)
    l=max(new_pathogen.keys())+1
    new_pathogen[l]=pathogen[eff].copy()
    return new_pathogen

def hgt(pathogen,nto,k):
    new_pathogen=deepcopy(pathogen)
    l=max(new_pathogen.keys())+1
    new_pathogen[l]={}
    lj=rk.randint(1,nto+1) #number of targeted genes
    new_pathogen[l]=dict(itr.izip(mda.newhost.NEWHOST(lj,k),rk.random(lj)))
    return new_pathogen

def probabilities(pathogen,host,rates,pop):
    dic_prob={} #keys are eff, values are probabilities
    av_score_tar=sum(mda.gpmap.g_p_mapa(host,pathogen).values())/float(len(host))
    eff_scores=mda.gpmap.g_p_mapb(host,pathogen)
    for effector in pathogen:
        dic_prob[effector]=[rates[0]*pop,rates[1]*(1-av_score_tar)*pop,
                            (rates[2]*pop)*math.exp(-eff_scores[effector]),rates[3]*pop/len(pathogen),
                            pop*((1-rates[0])+(1-rates[1])*(1-av_score_tar)+1-(rates[2]*math.exp(-eff_scores[effector]))+1-(rates[3]/len(pathogen)))]
    return dic_prob

def events(dic_prob):
    appening={}
    for effector in dic_prob:
        k=rk.random()
        sum_prob=sum(dic_prob[effector])
        n=0
        alfa=k*sum_prob
        som=0.0
        for i in dic_prob[effector]:
            som+=i
            if som>=alfa:
                break
            n+=1
        appening[effector]=n
    return appening

def transform(pathogen,appening,K,mu1,mu2,nto):
    for effector in pathogen:
        event=appening[effector]
        if event==4:
            pass
        elif event==0:
            pathogen=mutation(pathogen,effector,K,mu1,mu2,nto)
        elif event==1:
            pathogen=duplication(pathogen,effector)
        elif event==2:
            pathogen=deletion(pathogen,effector)
        elif event==3:
            pathogen=hgt(pathogen,nto,K)
    return pathogen
