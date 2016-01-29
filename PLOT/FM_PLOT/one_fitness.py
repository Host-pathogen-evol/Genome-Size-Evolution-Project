#!usr/bin/python

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
import matplotlib.ticker as mtick
import argparse

parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
"""))
parser.add_argument("p",help="path to the right directory")
parser.add_argument("r", type=int, help="number of runs")
parser.add_argument("j", type=int, help="number of jumps")
parser.add_argument("-n","--nojumps", type=bool, default=False, help="set to True if run with only c=0.1 / default False")
parser.add_argument("-s","--singlerun",type=int, default=0, help="single run to plot / default 0")
args=parser.parse_args()

pth=args.p
print pth
xi=args.j+1 #jumps
if args.nojumps==False:
    nX=['n0/','n1/','n2/','n3/','n4/','n5/','n6/','n7/','n8/'] #Parameters C
else:
    nX=['n0/']

rj='RUN'+str(args.singlerun)+'/'
for c_value in nX: #n0, n1, etc
    plot_this=[]
    print "processing c value", c_value
    for ji in xrange(1,xi): #number of jumps
        fitness_values=[]
        print "jump",ji
        try:
            fin=pth+rj+c_value+'pts'+str(ji)+'plotdata.p_2'
            f=open(fin,"rb")
            A=pickle.load(f)
            f.close()
            fitness_values+=A[0]
        except IOError:
            continue
        plot_this+=[(1-x) for x in fitness_values]
        print len(plot_this)
    print "plotting"
    fig1, axesa = plt.subplots(1,figsize=(10, 8))
    axesa.set_ylabel("$U_g(t)$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    plt.plot(range(len(plot_this)),plot_this,color='black')
    #plt.title('$Fitness$',fontsize=50)
    #print plot_this
    #print len(plot_this)
    #plt.xlim([0,len(average)])
    #plt.ylim([min(average)-100,max(average)+100])

    namepth=pth+"one_fitness_"+str(c_value)[:-1]+"run_"+str(args.singlerun)
    fig1.patch.set_alpha(0.5)
    fig1.savefig(namepth+'.png', dpi=100, bbox_inches='tight')
