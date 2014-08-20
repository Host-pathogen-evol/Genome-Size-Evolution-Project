#!/usr/bin/env python
from pygsl import rng as rn
import math as mth
import numpy as np
import TwoSpeedMods as hpm
import cubel as cbl

LH=8
Omega=mth.pow(2,LH)
print Omega
raw_input()
xn=cbl.getgenesl(LH)
#print xn
cbl.prteffset(xn)


S1=xn[1]
S2=xn[2]
print S1, S2

dh=cbl.effgendist(S1,S2)
print dh

S1=xn[2]
S2=xn[2]
print S1, S2

dh=cbl.effgendist(S1,S2)
print  dh
