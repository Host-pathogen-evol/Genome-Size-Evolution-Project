import os
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

def datadisplay(lth,ltn,ngt,efflens,telens,dbina,dbinb,P,SEED,pth,wfitn,Qi):

  #plt.use('Agg')
##########################################
  rxclrmin=min(telens)
  rxclrmax=max(telens)
  #if not rxclrmin:
  #print rxclrmax


  i=rxclrmin
  sna=[]
  while(i<rxclrmax+10):
      sna.append(i)
      i+=dbina

  hsza=np.histogram(telens,sna)
  ysna=hsza[0]
  xsna=np.delete(hsza[1],[len(hsza[1])-1])

  nsuma=(sum(ysna)*dbina)
  psa=[]
  for i in ysna:
      psa.append(float(i)/nsuma)
  #print ps
############################################
  rxclrmin=min(efflens)
  rxclrmax=max(efflens)
  #print rxclrmin
  #print rxclrmax
  #print(efflens)

  i=rxclrmin
  sn=[]
  while(i<rxclrmax+10):
    sn.append(i)
    i+=dbinb

    hsz=np.histogram(efflens,sn)
    ysn=hsz[0]
    xsn=np.delete(hsz[1],[len(hsz[1])-1])

  normsum=(sum(ysn)*dbinb)
  ps=[]
  for i in ysn:
    ps.append(float(i)/normsum)

############################################
  fig, axes2 = plt.subplots(2,2,figsize=(100, 8))

  axes2[0][0].plot(lth)
  axes2[0][0].plot(ltn,"r-")

  ax_inset=fig.add_axes([0.59,0.75,0.1,0.1])
  ax_inset.plot(wfitn,"r-+")

  axes2[0][1].plot(ngt,"b*-")


  #fig, axes3 = plt.subplots(1,1,figsize=(10, 8))
  #axes3.plot(ngt,"r-")
  #axes2[1][0] = plt.subplots(1, 1, figsize=(20, 8))


  axes2[1][0].plot(xsna, psa,"r--o")
  axes2[1][0].set_title('TEs pdf '+str(len(telens)), fontsize=10)
  axes2[1][0].set_ylabel("$P(l_i=n)$",fontsize=10)
  axes2[1][0].set_xlabel("$Gene$ $Size$ $n$ $(bp)$",fontsize=10)
  axes2[1][0].xaxis.set_tick_params(labelsize=10)
  axes2[1][0].yaxis.set_tick_params(labelsize=10)
  axes2[1][0].yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))


#fig, axes=plt.subplots(1, 1, figsize=(20, 8))
#axes.hist(rxclr, histtype="stepfilled",bins=250, alpha=0.8, normed=True)
#################################################################
  axes2[1][1].plot(xsn, ps,"r--o")

  axes2[1][1].set_title('EFFs pdf '+str(len(efflens)), fontsize=10)
  axes2[1][1].set_ylabel("$P(l_i=n)$",fontsize=10)
  axes2[1][1].set_xlabel("$Gene$ $Size$ $n$ $(bp)$",fontsize=10)
  axes2[1][1].xaxis.set_tick_params(labelsize=10)
  axes2[1][1].yaxis.set_tick_params(labelsize=10)
  axes2[1][1].yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
####################################################################
  ttl=''
  #for i in P:
  ttl+='c='+str(Qi)
  #print ttl

  fig.suptitle(ttl, fontsize=30)


  nj=1
  import os
  namefig=pth+'/pts'+str(nj)+'plot.svg'
  while os.path.exists(namefig):
    nj+=1
    namefig=pth+'/pts'+str(nj)+'plot.svg'
  print namefig

  #namepth=pth+'plots.svg'


  fig.set_size_inches(13.5,10.5)
  fig.patch.set_alpha(0.5)
  fig.savefig(namefig,dpi=100, bbox_inches='tight')
  plt.close(fig)
##########################################################################
'''*********modify next line to save DT, number of jumps as well as the other parameters
just adding them at the end of the things the fun needs and at the and of the Data list
'''
def savedata(lth,ltn,ngt,efflens,telens, P,SEED,pth,wfitn,trns,nefft,ntest,lneff,lntest, DT, JUMPS): ###*

  Data=[lth,ltn,ngt,nefft,ntest,efflens,telens, P,SEED,trns,lneff,lntest,DT,JUMPS] ###*
  Data2=[wfitn]

  nj=1
  namefig=pth+'/pts'+str(nj)+'plotdata.p'

  while os.path.exists(namefig):
    nj+=1
    namefig=pth+'/pts'+str(nj)+'plotdata.p'
    namefig2=pth+'/pts'+str(nj)+'plotdata_2.p'
  print namefig

  #**********add these lines
  aladd=pth.strip('./').split('/')
  aladd.append(str(nj))
  Data.append(aladd)

  pickle.dump(Data,open(namefig,"wb"))
  pickle.dump(Data2,open(namefig2,wb),protocol=2)
