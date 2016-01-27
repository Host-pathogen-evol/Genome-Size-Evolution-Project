##################################################################
def splitgen(gen):
  effls=[]
  tels=[]
  for i in gen.keys():
    if gen[i][0]=='eff':
        effls.append(gen[i][1])
    else:
        tels.append(gen[i][1])
  return [effls, tels]
##################################################################
def loaddata(name):

    fin=open(name,"r")
    line=fin.readline()
    data=[]
    while line:
        data.append(float(line))
        line=fin.readline()
    return data
###################################################################
def inigenome(ne,nte,rk,tepar,effpar):
    import math
    #print ne, nte
    #print tepar
    #print effpar
    gen={}

    for i in range(ne):
        l=math.floor((effpar[1]-effpar[0])*rk.uniform()+effpar[0])
        sn=rk.uniform_pos()
        gen[i]=['eff',l,sn]
    for i in range(nte):
        l=math.floor( (tepar[1]-tepar[0])*rk.uniform()+tepar[0] )
        gen[ne+i]=['te',l]

    return gen
####################################################################
def trates(Gen,MU): #MU=[Np,m1,m2,m3,m4,m5,m6,m7,m8?,Lth,beta1,beta2]
    import math
    #print("HOLA")


    TPR={}
    Np=MU[0]
    m1=MU[1] #hgt effs
    m2=MU[2] #hgt te
    m3=MU[3] #eff recomb
    m4=MU[4] #te dup
    m5=MU[5] #eff dup+te
    m6=MU[6] #eff->null
    m7=MU[7] #te->0
    m8=MU[8] #eff->0
    Lth=MU[9]
    b1=MU[10]
    b2=MU[11]
    Wo=MU[12]
    #print len(MU)
    #print MU
    #print("#################")

    L=0.0
    neff=0.0
    ntes=0.0
    Wn=0.0

    for j in Gen.keys():
        L+=Gen[j][1]
        #print Gen[j]
        if Gen[j][0]=='eff':
          neff+=1.0
          Wn+=Gen[j][2]
        if Gen[j][0]=='te':
          ntes+=1.0
        #raw_input()
    if neff>0.0:
   	 Ws=1.0-((Wn/neff)/((Wn/neff)+(Wo)))
    else:
    	print("EFF=0-KILL")


    Nk=(1500.0-(neff+ntes))
    if Nk<0:
        Nk=0.0

    FL=1.0/( 1.0+ (2.0*L/Lth)**2 )
    #print Ws
    #raw_input()

    for j in Gen.keys():
        #print j
        if Gen[j][0]=='eff':
            zn=[]
            #if L<Lth: #HGT
            #  if(neff>0.0):
            t1=(m1/neff)*(FL +0.0*Ws)*Nk

            #  else:
            #    t1=m1*((Lth-L)+0.0*Ws)*Nk
            #else:
            #    t1=0.0

            t2=m3*Np*(Gen[j][1]) #Eff recomb

            #Duplication
            #if L<Lth:
            t3=m5*Np*FL*math.exp(-b2*Gen[j][1])*Ws*Nk#*Gen[j][2]
            #it3=m5*Np*FL*math.exp(-b2*Gen[j][1])*Nk#*Gen[j][2]
            #else:
            #    t3=0.0

            #Function loss
            #t4=m6*((Gen[j][1]**5)/( (Gen[j][1]**5)+ ((5e3)**5) ))
            #t4=m6*(1.0-Gen[j][2])#((Gen[j][1]**5)/( (Gen[j][1]**5)+ ((5e3)**5) ))
            t4=m6*Np*math.exp(-Gen[j][2])#((Gen[j][1]**5)/( (Gen[j][1]**5)+ ((5e3)**5) ))

            #Removal
            #if (neff>0.0):
            t5=m8*Np*math.exp(-Gen[j][2])
            #else:
            #t5=0.0 #m8*(1-Ws)
            #*((Gen[j][1]**5)/( (Gen[j][1]**5)+ ((100.0)**5) ))
            #t5=m7*((L)/((L)+((0.001*Lth))))  #removal

            zn.append(t1)
            zn.append(t2)
            zn.append(t3)
            zn.append(t4)
            zn.append(t5)

            TPR[j]=zn

        if Gen[j][0]=='te':
            zn=[]

            #if L<Lth:
              #if (ntes>0.0):
                #t1=(m2/ntes)*(Lth-L) #htg
            t1=(m2/ntes)*FL*Nk #htg
            #  else:
            #    t1=m2*(Lth-L)
            #else:
            #    t1=0.0

            #if L<Lth:
            t2=m4*Np*FL*Nk*math.exp(-b1*Gen[j][1]) #rep
            #else:
            #    t2=0.0

            #if ntes>0.0:
              #t3=(m7)*(Lth-L)*Nk#*((Gen[j][1]**5)/((Gen[j][1]**5)+((9e3)**5)))
            t3=m7*Np#*math.exp(-Gen[j][2]) #*((Gen[j][1]**5)/((Gen[j][1]**5)+((9e3)**5)))
            #else:
            #  t3=0.0#m7*(Lth-L) #m7*((Gen[j][1]**5)/((Gen[j][1]**5)+((9e3)**5)))
              #t3=m7*(Lth-L) #m7*((Gen[j][1]**5)/((Gen[j][1]**5)+((9e3)**5)))
            #t3=m7*((L)/((L)+((0.001*Lth))))  #removal
            zn.append(t1)
            zn.append(t2)
            zn.append(t3)
            TPR[j]=zn

    #print("adios")
    return TPR
##############################
def montec(rates, rk):
    sn=0.0
    for i in rates.keys():
        #print rates[i]
        a=sum(rates[i])
        #print a
        sn=sn+a

    #print sn
    nxtr=[]
    END=''
    if sn>0.0:
      a=rk.uniform()
      mu=a*sn
      sx=0.0
      fl=0
      #nxtr=[]

      for i in rates.keys():
        rn=0
        for k in rates[i]:
            sx+=k
            #print mu, sx,  rn
            if sx>=mu:
                fl=1
                nxtr.append(i)
                nxtr.append(rn)
                #nxtr.append()
                #print("done!")
                break
            rn+=1
        if fl==1:
            break
    else:
      END='TRUE'

    #print nxtr
    return [nxtr,END]
##########################################
def transform(nxtr,gen,rk,tepar,effpar):
    import math
    gi=nxtr[0]
    ri=nxtr[1]

    zn=gen[gi][0]
    #print gi, gen[gi], ri, zn
    gx={}
    #for u in gen.keys():
    #    gx[u]=gen[u]

    if zn=='eff':
        #print("EFF!")
        #print ri
        #raw_input()
        if ri==0:
            ki=0
            for u in gen.keys():
              rn=[]
              for zk in gen[u]:
                rn.append(zk)
              gx[ki]=rn # [gen[u][0],gen[u][1]]
              ki+=1
            #print("create effector")
            nu=[]
            nu.append('eff')
            l=math.floor((effpar[1]-effpar[0])*rk.uniform()+effpar[0])
            nu.append(l)
            nu.append(rk.uniform_pos())
            ng=len(gx.keys())
            gx[ng]=nu
            #break


        if ri==1:
            #print("Length Recomb")
            ki=0
            for u in gen.keys():
              if u != gi:
                rn=[]
                for zk in gen[u]:
                  rn.append(zk)
                gx[ki]=rn#[gen[u][0],gen[u][1]]
                ki+=1
            ng=len(gx.keys())
            l=gen[gi][1]+math.floor( (1-2.0*rk.uniform())*100 )
            if l<=math.floor(0.5*effpar[0]):
              if l>=0.0:
                gx[ng]=['te',l]
            else:
              #coin=rk.uniform()
              gx[ng]=[gen[gi][0],l,(0.01+gen[gi][2])]
            #l=gen[gi][1]+math.floor(((effpar[1]-effpar[0])*rk.uniform()/3.0)+effpar[0])
            #a=gen[gi][1]+math.floor((effpar[1]-effpar[0])*rk.uniform()+effpar[0])
            #ng=len(gx.keys())
            #  gx[ng]=[gen[gi][0],l]
            #break

        if ri==2:
            #print("Repeat")
            ki=0
            for u in gen.keys():
                rn=[]
                for zi in gen[u]:
                  rn.append(zi)
                gx[ki]=rn #[gen[u][0],gen[u][1]]
                ki+=1
            ng=len(gx.keys())
            gx[ng]=[gen[gi][0],gen[gi][1],gen[gi][2]]
            #break

        if ri==3:
            #print("Bye")
            ki=0
            for i in gen.keys():
                if i != gi:
                    rn=[]
                    for zk in gen[i]:
                      rn.append(zk)
                    gx[ki]=rn #[gen[i][0],gen[i][1],gen[i][2]]
                if i == gi:
                    gx[ki]=['te',gen[gi][1]]
                ki+=1

            #break
        if ri==4:
          ki=0
          for i in gen.keys():
            if i!=gi:
                rn=[]
                for zk in gen[i]:
                  rn.append(zk)
                gx[ki]=rn
                ki+=1



    if zn=='te':
        if ri==0:
            #print ("create te")
          ki=0
          for i in gen.keys():
            rn=[]
            for zk in gen[i]:
              rn.append(zk)

            gx[ki]=rn#[gen[i][0],gen[i][1]]
            ki+=1
          nu=[]
          nu.append('te')
          l=math.floor( (tepar[1]-tepar[0])*rk.uniform()+tepar[0] )
          nu.append(l)
          ng=len(gx.keys())
          gx[ng]=nu
            #break

        if ri==1:
          ki=0
          for u in gen.keys():
            rn=[]
            for zk in gen[u]:
              rn.append(zk)
            gx[ki]=rn #[gen[u][0],gen[u][1]]
            ki+=1
          #print("Repeat")
          ng=len(gx.keys())
          gx[ng]=[gen[gi][0],gen[gi][1]]

        if ri==2:
          ki=0
          for i in gen.keys():
            if i!=gi:
                gx[ki]=gen[i]
                ki+=1
            #break
            #print("bye")

    return gx
    #if gen[gi][0]

##########################################
def lent(gen):
    Lt=0.0

    for i in gen.keys():
        Lt+=gen[i][1]

    return Lt
############################################
def ft(gen):
    ft=0.0
    ne=0.0
    for i in gen.keys():
        if gen[i][0]=='eff':
          ft+=gen[i][2]
          ne+=1.0
    if ne>0.0:
      ft=ft/ne

    return ft
############################################
############################################
############################################
############################################
############################################
############################################
############################################
############################################
############################################
############################################
############################################
############################################
############################################
############################################
def Fig1(rxclr,crinckler,pth):

  import numpy as np
  import matplotlib.pyplot as plt
  import matplotlib.ticker as mtick
  import pickle

  rxclrmin=min(rxclr)
  rxclrmax=2500 #max(rxclr)
  #print rxclrmin
  #print rxclrmax

  i=rxclrmin
  sn=[]
  while(i<rxclrmax+10):
    sn.append(i)
    i+=10

  hsz=np.histogram(rxclr,sn)
  ysn=hsz[0]
  xsn=np.delete(hsz[1],[len(hsz[1])-1])
  normsum=(sum(ysn)*10)
  ps=[]
  for i in ysn:
    ps.append(float(i)/normsum)

  fig, axes = plt.subplots(1, 1, figsize=(20, 8))
  axes.plot(xsn, ps,"r--o")
  fig.suptitle('RXLR effectors lengths distribution P. Infestans', fontsize=40)
  axes.set_ylabel("$P(l_i=n)$",fontsize=40)
  axes.set_xlabel("$Gene$ $Size$ $n$ $(bp)$",fontsize=40)
  axes.xaxis.set_tick_params(labelsize=30)
  axes.yaxis.set_tick_params(labelsize=30)
  axes.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
###########################################
  cklermin=min(crinckler)
  cklermax=3200 #max(crinckler)
  #print cklermin
  #print cklermax

  i=cklermin
  snx=[]
  while(i<cklermax+10):
    snx.append(i)
    i+=50

  hszx=np.histogram(crinckler,snx)
  ysnx=hszx[0]
  xsnx=np.delete(hszx[1],[len(hszx[1])-1])
  normsumx=(sum(ysnx)*50)
  psx=[]
  for i in ysnx:
    psx.append(float(i)/normsumx)

  ax_inset=fig.add_axes([0.5,0.55,0.3,0.3])
  ax_inset.plot(xsnx, psx,"r--o")

  plt.title('Crinkler lengths distribution P. Infestans', fontsize=18)
  ax_inset.set_ylabel("$P(l_i=n)$",fontsize=20)
  ax_inset.set_xlabel("$Gene$ $Size$ $n$ $(bp)$",fontsize=20)
  ax_inset.xaxis.set_tick_params(labelsize=15)
  ax_inset.yaxis.set_tick_params(labelsize=15)
  ax_inset.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
#setp(a, xticks=[], yticks=[])
###########################################
  fig.set_size_inches(13.5,10.5)
  fig.patch.set_alpha(0.5)
  namepth=pth+'/Fig1.svg'
  fig.savefig(namepth,dpi=100, bbox_inches='tight')
  pickle.dump([xsnx,psx,xsn,ps],open(pth+"/F1data.p","wb"))
###########################################
###########################################
###########################################
###########################################
def Fig2(tes,pth):
  import numpy as np
  import matplotlib.pyplot as plt
  import matplotlib.ticker as mtick
  import pickle

  tesmin=min(tes)
  tesmax=max(tes)
#print rxclrmin
#print rxclrmax
  i=tesmin
  sn=[]
  while(i<tesmax+10):
    sn.append(i)
    i+=500
  hsz=np.histogram(tes,sn)
  ysn=hsz[0]
  xsn=np.delete(hsz[1],[len(hsz[1])-1])
  normsum=(sum(ysn)*500)
  ps=[]
  for i in ysn:
    ps.append(float(i)/normsum)
#print ps
#############################################
  clade=[65,95,220,230,240,280]
  pcoding=[14451,16988,19622,20545,18155,19634]
#plt.style.use('ggplot')
  fig, axes2 = plt.subplots(1,1,figsize=(10, 8))
#axes2 = axes.ravel()
  leg=['P. ramorum','P. sojae','P. phaseoli Race F18','P. ipomoeae PIC79916','P. infestans','P. mirabilis PIC99114']
  font = {'family' : 'serif',
        'color'  : 'darkred',
        'weight' : 'normal',
        'size'   : 18,
        }
  axes2.plot(clade,pcoding,"--o")
  plt.text(clade[0]+2, pcoding[0], leg[0], fontdict=font)
  plt.text(clade[1]+1, pcoding[1], leg[1], fontdict=font)
  plt.text(clade[2]-60, pcoding[2]+100, leg[2], fontdict=font)
  plt.text(clade[3]+1, pcoding[3], leg[3], fontdict=font)
  plt.text(clade[4]-20, pcoding[4]-250, leg[4], fontdict=font)
  plt.text(clade[5]-45, pcoding[5]+100, leg[5], fontdict=font)
  axes2.set_ylabel("Protein coding genes",fontsize=40)
  axes2.set_xlabel("Genome Size (Mb)",fontsize=40)
  formatter = plt.ScalarFormatter()
  formatter.set_powerlimits((-3, 4))
  plt.gca().yaxis.set_major_formatter(formatter)
  axes2.ticklabel_format(axis='y', style='sci')#, scilimits=(-20,2))
  axes2.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
  axes2.xaxis.set_tick_params(labelsize=30)
  axes2.yaxis.set_tick_params(labelsize=30)
###################################
  ax_inset=fig.add_axes([0.55,0.2,0.3,0.3])
  ax_inset.plot(xsn, ps,"r--o")
  ax_inset.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
  ax_inset.xaxis.set_tick_params(labelsize=15)
  ax_inset.yaxis.set_tick_params(labelsize=15)
  plt.title('TEs length distribution P. Infestans', fontsize=18)
  ax_inset.set_ylabel("$P(l_i=n)$",fontsize=20)
  ax_inset.set_xlabel("$Gene$ $Size$ $n$ $(bp)$",fontsize=20)
######################################
  fig.set_size_inches(13.5,10.5)
  fig.patch.set_alpha(0.5)
  namepth=pth+'/Fig2.svg'
  fig.savefig(namepth,dpi=100, bbox_inches='tight')
  pickle.dump([clade,pcoding,leg, xsn,ps],open(pth+"/F2data.p","wb"))
