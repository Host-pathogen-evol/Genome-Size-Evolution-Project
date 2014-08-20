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

def IniScores(A,rk):

	Sc=[]
	#print ("IN")
	#print effj
	#print Hst
	#print len(A)
	#print type(A)
	#raw_input()
	for ic in A:
		if ic==1.0:
			mkx=rk.uniform_pos()
			Sc.append(mkx)
		if ic==0.0:
			Sc.append(0.0)
	#print("BYE!")
	return  Sc

def Hill(x,xo,n,xmax):
	yge=0.0
	#if x<xmax:
	yge=pow(x,n)/(pow(x,n)+pow(xo,n))
	return yge

def GeneExp(H,Pi,Sij,HP):
	gxp=0.0
	Qi=int(Pi)
	for jp in H:
		#print("(ei,ti)")
		#print Qi
		#print jp
		#print("Hij")
		#print HP[Qi-1][jp-1]
		#print ("sij")
		#print Sij[jp-1]
		if HP[Qi-1][jp-1]==1.0:
			ei=Hill(Sij[jp-1],0.5,5,3.0) #x^5/(0.5^5+x^5) xmax=3.0 THIS IS IMPORTANT
			gxp=gxp+ei
			#print gxp
			#print ei
			#raw_input()
	return gxp



def NEWHOST(Lhx,Khx,rk):

	hx=[]
	q=1
	zx=1+rk.uniform_int(Khx)
	hx.append(zx)
	while q<Lhx:
		mu=0
		zx=1+rk.uniform_int(Khx)
		for j in hx:
			if j==zx:
				mu=1
				break

		if mu==0:
			hx.append(zx)
			q=q+1

	hx.sort()

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

def NEWPATHOGENUNIT(ng,rk,lr):
	PTHU=[]
	import numpy as np
	lnmu=lr[0]
	lnsigma=lr[1]
	PTHU.append('E'+str(ng))
	PTHU.append(ng)
	lc=np.random.lognormal(mean=lnmu,sigma=lnsigma,size=1)
	PTHU.append(lc[0])

	return PTHU

def INIPATHGEN(hn,Kp,rk,lr):
	zo={}
	for j in range(hn):
		zo[j]=NEWPATHOGENUNIT(j,Kp,rk,lr)
	return zo

def INIASSEMBLE(gpo,Ho,HP,rk):
	for i in gpo.keys():
		#print i
		#print gp[i]
		#print gp[i][1]
		inx=gpo[i][1]-1
		smu={}
		emu={}
		for j in Ho:
			sq=0.0
			eq=0.0
			if(HP[inx][j-1]==1.0):
				sq=rk.uniform_pos()
			eq=Hill(sq,0.5,5,3.0)
			#smu[].append(sq)
			smu[j]=sq
			#emu.append(eq)
			emu[j]=eq
			#print inx, j-1, sq, eq
			#raw_input()
		#print smu
		#print emu
		#print sum(emu.values())/(Cn*Lh)
		gpo[i].append(smu)
		gpo[i].append(emu)
		#Wi.append(sum(emu))
	#raw_input()
	return gpo

def GETGENOMELENGTH(gn):
	GL=0
	GLNC=0
	GLC=0
	for i in gn.keys():
		GL+=gn[i][2]

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


def reactions(RK,Gn, Np,Lg,Prms,rk):
	import math as mth
	#Sn=[]
	#print('RATESFUNC')
	#print Np
	#print Gn
	#rnk=rk.uniform_pos()
	ngi=0
	Tr={}
	#RR=[]
	for i in Gn.keys():
			RR=[]
			#print Gn[i][0]
			#print Gn[i][1]
			#print Gn[i][2]
			#print Gn[i][3]
			#print("Wi:")
			#print Gn[i][4]
			#raw_input()
			LhCn=Prms[0]
			wi=sum(Gn[i][4].values())/LhCn
			fnei=0.8
			Lav=Prms[1]
			#print wi

		#r1=RK[0]*(Gn[i][2]/(Lg*Np))*(mth.fabs(1-wi))
			r1=Np*RK[0]*(Gn[i][2]/Lg)*(mth.exp((mth.fabs(1-wi)))-1.0)
			r2=Np*RK[1]*(fnei)*(0.5)*(1+mth.tanh(Lg-Lav))
			r3=Np*RK[2]*(fnei*Gn[i][2]/Lg)*(mth.exp(-10.0*wi))
			#print r1, r2, r3
			RR.append(r1)
			RR.append(r2)
			RR.append(r3)
			Tr[i]=RR
			#raw_input()
	return Tr


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

def TRANSFORMATIONS(gn,rn,Gn,Hg,rk):
	#rn 0 ei->ei'
	#rn 1 ei->ei+ei
	#rn 2 ei->eo
	#print Gn
	Gnmod={}
	if rn==0:
		#print("CERO")
		for mu in Gn.keys():
			if (mu<gn) or (mu>gn):
				Gnmod[mu]=Gn[mu]
			if mu==gn:
				#print("TROUBLE HERE")
				#print Gn[gn][3]
				#raw_input()
				#sijn={}
				sigl=Gn[gn][2]/10000.0 ####Here 1000 is the Lo in li/Lo for the ds std in  s'=s+ds !!!!
				#print sn
				#print sigl
				skx=Gn[gn][3]
				sijn={}
				for sj in skx.keys():
					if skx[sj]==0.0:
						sijn[sj]=0.0
					if skx[sj]!=0.0:
						#print sj
						dsj=rk.gaussian(sigl)
						if (skx[sj]+dsj)>0:
						#print dsj
							sijn[sj]=skx[sj]+dsj
						if (skx[sj]+dsj)<=0:
							sijn[sj]=0.00001
					#print sijn
				nugen=[]
				nugen.append(Gn[gn][0])
				nugen.append(Gn[gn][1])
				ql=rk.uniform_pos()
				dlen=1.0
				if ql<=0.5:
					qq=rk.uniform_pos()
					nlen=Gn[gn][2]*(1+dlen*qq)
				if ql>0.5:
					qq=rk.uniform_pos()
					nlen=Gn[gn][2]*(1-dlen*qq)
				nugen.append(nlen)
				nugen.append(sijn)
				#Gnmod[gn][0]=Gn[gn][0]
				#Gnmod[gn][1]=Gn[gn][1]
				#Gnmod[gn][2]=Gn[gn][2]
				#Gnmod[gn][3]=sijn
				wijm={}
				for sk in sijn.keys():
					wqflg=0.0
					for kn in Hg:
						if sk==kn:
							wqflg=1.0
							break
					if wqflg==1.0:
						wk=Hill(sijn[sk],0.5,5,3.0)
					if wqflg==0.0:
						wk=0.0

					wijm[sk]=wk
				nugen.append(wijm)
				Gnmod[gn]=nugen
				#print dsj

		#print sn
		#raw_input()
		#break

	if rn==1:
		#print("UNO")
		for mu in Gn.keys():
			if mu<gn:
				Gnmod[mu]=Gn[mu]
			if mu==gn:
				Gnmod[mu]=Gn[mu]
				Gnmod[mu+1]=Gn[mu]
			if mu>gn:
				Gnmod[mu+1]=Gn[mu]
		#break
	if rn==2:
		#print("DOS")
		for mu in Gn.keys():
			if mu<gn or mu>gn:
				Gnmod[mu]=Gn[mu]
			if mu==gn:
				gx=[]
				#print type(Gn[gn][0])
				#raw_input()
				gx.append('SL'+Gn[gn][0])
				gx.append(Gn[gn][1])
				gx.append(rk.uniform()*Gn[gn][2])
				snu={}
				for ik in Gn[gn][3].keys():
					snu[ik]=0.0
				gx.append(snu)
				gx.append(snu)
				Gnmod[gn]=gx
	#print Gnmod
	return Gnmod

def GETWI(gn):
	Wi=[]
	for i in gn.keys():
		u=gn[i][4]
		wi=[]
		for j in u.keys():
			wi.append(u[j])
		#print wi
		Wi.append(sum(wi))
	return Wi

def JUMP(Gnj,Hnew,HP,rk):
	print("JUMPS FUNCTION")
	newsij=[]
	kys=Gnj.keys()[0]
	oldkys=Gnj[kys][3].keys()
	newsij=Gnj[kys][3].keys()
	newsij.extend(i for i in Hnew if i not in newsij)
	print newsij
	print oldkys
	compsij=list(set(newsij)-set(oldkys))
	#compsij2=list(set(newsij)-set(newsij))
	#print compsij
	#print compsij2
	#raw_input()
	GJMP={}
	for i in Gnj.keys():
		nugene=[]
		nugene.append(Gnj[i][0])
		nugene.append(Gnj[i][1])
		nugene.append(Gnj[i][2])

		ink=Gnj[i][1]-1
		print ink
		smu={}
		for jm in Gnj[i][3].keys():
			smu[jm]=Gnj[i][3][jm]
			#raw_input()
		#print smu
		for jm in compsij:
			if(HP[ink][jm-1]!=0.0):
				smu[jm]=rk.uniform_pos()
			if(HP[ink][jm-1]==0.0):
				smu[jm]=0.0
		#raw_input()
		#print("smu")
		#print smu
		emu={}
		for jm in smu.keys():
			qj=0.0
			pthflg=0
			for jl in Hnew:
				if jm==jl:
					pthflg=1.0
					break

			if((HP[ink][jm-1]!=0.0) and (pthflg==1.0)):
				qj=Hill(smu[jm],0.5,5,3.0)
			emu[jm]=qj

		#print("emu")
		#print emu
		nugene.append(smu)
		nugene.append(emu)
		GJMP[i]=nugene
		raw_input()
	return GJMP

def GETALPHARATE(Tr):
	alpha=0.0
	for x in Tr.keys():
		#print Tr[x]
		alpha=alpha+sum(Tr[x])
		#raw_input()
	return alpha

def WHICHREACTION(a,Tr,rk):
	lk=rk.uniform_pos()
	#print lk
	#print a
	#print lk*a
	#print Tr
	#raw_input()
	sumtr=0.0
	rpair=[]
	brkflg=0
	for ik in Tr.keys():
		cnt=0
		for jk in Tr[ik]:
			sumtr=sumtr+jk
			if sumtr>=(lk*a):
				rpair.append(ik)
				rpair.append(cnt)
				brkflg=1
				break
			cnt+=1
		if(brkflg==1):
			break
	return rpair

def prtgenomes(gk):
	for xn in gk.keys():
		print gk[xn][0]
		print gk[xn][1]
		print gk[xn][2]
		print gk[xn][3]
