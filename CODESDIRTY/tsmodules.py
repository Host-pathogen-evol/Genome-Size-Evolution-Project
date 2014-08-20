#!/usr/bin/env python

#def hpminit(SEED):
	#from pygsl import rng as rng
	#import math as mth
	#import numpy as np
	#rk=rng.rng()
	#print rk.name()
	#mu=rk.set(SEED)
	#return rk

def effnnet(Kxs,cx,rx):
	effnt={}
	for i in range(1,Kxs+1):
		lj=[]
		for j in range (1,Kxs+1):
			qx=rk.uniform()
			if rk<=qx:
				lj.append(j)
		effnt[i]=lj
	return effnt		

def prtmat(Mat):
	for row in Mat:
		print row

def HPMATRIX(Kn,Kx,kix,rk):
	#print rk.name()
	HPMT=[[0.0 for col in range(Kx)] for row in range(Kn)]

	for i in range(0,Kn):
		for j in range(0,Kx):
			l1=rk.uniform()
			if l1<kix:
				HPMT[i][j]=1.0
	#			l1x=rk.uniform()
	#			if l1x<0.5:
	#				HPMT[i][j]=1.0
	#			else:
	#				HPMT[i][j]=1.0
	#		HPMT[j][i]=HPMT[i][j]
	#	print i
	return HPMT

def NEWHOST(Lhx,Khx,rk):
	
	hx=[]
	for q in range(Lhx):
		zx=1+rk.uniform_int(Khx)
		hx.append(zx)
	return hx

def PMINLENS(K,lr,rk):
	import numpy as np
	lo={}
	muln=lr[0]
	sigmaln=lr[1]
	print muln
	print sigmaln
	raw_input()
	for i in range(K):
		#lo[i+1]=rk.lognormal(muln,sigma)
		#lo[i+1]=1.0+lrmax*rk.uniform()
		lok=np.random.lognormal(mean=muln,sigma=sigmaln,size=1)
		lo[i+1]=lok[0]
	return lo

def NEWPATHOGENUNIT(np,Kp,rk,lr):
	PTHU=[]
	import numpy as np
	lnmu=lr[0]
	lnsigma=lr[1]
	if np==0:
		PTHU.append('C')
		PTHU.append('gk')
		#lc=rk.uniform_int(lrmax)
		#lc=1.0+lrmax*(rk.uniform())
		lc=np.random.lognormal(mean=lnmu,sigma=lnsigma,size=1)
		PTHU.append(lc[0])
	else:
		nt=rk.uniform_int(2)
		lc=np.random.lognormal(mean=lnmu,sigma=lnsigma,size=1)
		if nt==0:
				PTHU.append('C')
				PTHU.append('gk')
				#lc=rk.uniform_int(lrmax)
				#lc=1.0+lrmax*(rk.uniform()) 
				PTHU.append(lc[0])	

		if nt==3:
				PTHU.append('NC')
				
				PTHU.append('gk')
				#lc=rk.uniform_int(lrmax)
				#lc=1.0+lrmax*(rk.uniform()) 
				PTHU.append(lc[0])	

		if nt==1:
				PTHU.append('EFF')				
				qx=1+rk.uniform_int(Kp)
				gn='p'+str(qx)
				PTHU.append(gn)
				PTHU.append(lc[0])	

	return PTHU

def INIPATHGEN(hn,Kp,rk,lr):
	zo={}
	for j in range(hn):
		zo[j]=NEWPATHOGENUNIT(j,Kp,rk,lr)
	return zo	

def GETGENOMELENGTH(gn):
	GL=0
	GLNC=0
	GLC=0
	for i in gn.keys():
		print('locus %d'%int(i))
		if gn[i][0]=='EFF':
			print("EFFECTOR")
			print("TAG:%s"%gn[i][1])
			print("length:%f"%gn[i][2])
			lx=gn[i][2]
			GL+=lx
			GLNC+=lx		

		if gn[i][0]=='C':
			print("CODING")
			lx=gn[i][2]
			print("length:%f"%lx)
			GL+=lx
			GLC+=lx

		if gn[i][0]=='NC':
			print("NON-CODING")
			print("length:%d"%lx)
			lx=gn[i][2]
			print lx
			GL+=lx
			GLNC+=lx
	#print GL
	#print GLC
	#print GLNC			
	return GL

def HPINTERACTION(H,P,HP):
	mi=0
	#print len(HP)
	Sk=[]
	for i in P.keys():
		if P[i][0]=='EFF':
			for j in P[i]:
				mu=(type(j) is str)
				if (mu== True) and (j!='EFF'):
					print j
					jsp=int(j.replace('p',''))
					#print jsp
 					si=0.0
 					#print jsp-1
					for l in H:	
						si+=HP[jsp-1][l-1]					
					Sk.append(si)

	N1=len(Sk)
 	N2=len(H)
 	N3=sum(Sk)			
	return N3


def reactions(Gn, RT, rk, Wn, HP,H,VIR):
	import math as mth 
	Sn={}	
	ngi=0
	for i in Gn.keys():
		#print Gn[i][0]
		if Gn[i][0]=='EFF':

			#print "EFFECTOR IS GONNA BE COPIED!"
			r1=RT[0]*RT[1]/Gn[i][2]      #Synonymous r1
			r2=RT[0]*(1.0-RT[1])/Gn[i][2]  #Silencing E->* r2
			un=int(Gn[i][1].replace('p',''))
			mi=0.0
			for hl in H:
				mi+=HP[un-1][hl-1]
			wo=len(H)*VIR

			print wo
			print mi
			r3=RT[5]*((mth.pow(wo,11) )/( mth.pow(mi,11) + mth.pow(wo,11) ))
			print r3

			re=[r1, r2, r3]
			rte=sum(re)
			print rte 
			ri=rk.uniform()
			print ri
			ti=(1.0/rte)*mth.log(1.0/ri)
			Sn[i]=ti
			raw_input("EFF done")

		if Gn[i][0]=='C':

			r4=(RT[2]*RT[3])/(Gn[i][2]) #Synonymous r4
			r5=(RT[2]*(1.0-RT[3]))/(Gn[i][2]) #C->NC Silencing r5
			rcod=[r4,r5]
			rtc=sum(rcod)
			rmb=rk.uniform()
			ric=(1.0/rtc)*mth.log(1.0/rmb)
			Sn[i]=ric
			raw_input('rates coding done')

		if Gn[i][0]=='NC':
			r=rk.uniform()
			r6=mth.exp(-RT[4])  #NC->* removal r3
			rremov=(1.0/r6)*mth.log(1.0/r)
			Sn[i]=rremov
			raw_input('non-coding done')
				
	return Sn

def reactionsjmp(Gn,H,HP):
	GN=Gn
	for i in Gn.keys():
		if Gn[i][0]=='NC':
			j=Gn[i][1]
			print j
			jn=int(j.replace('p',''))
			qi=0.0
			for k in H:
				if (HP[jsp-1][k-1]!=0.0):
					qi=1.0
					break				
			if(qi==1.0):
				GN[i][0]=='EFF'
	
		if Gn[i][0]=='EFF':
			j=Gn[i][1]
			print j
			jn=int(j.replace('p',''))
			qi=0.0
			for k in H:
				if(HP[jsp-1][k-1])!=0.0:
					qi=1.0
					break
			if(qi==0.0):
				GN[i][1]=='NC'

			
	return GN

def HPSCORES(H,PTH,HP,VIR):
	Nj=[]
	nc=0.0
	nnc=0.0
	ne=0.0
	for i in PTH.keys():
		if PTH[i][0]=='NC':
			nnc+=1.0
		if PTH[i][0]=='EFF':
			ne+=1.0
		if PTH[i][0]=='C':
			nc+=1.0

	Nj=[nc,nnc,ne,len(H),(ne*float(len(H)))*VIR]
	return Nj
