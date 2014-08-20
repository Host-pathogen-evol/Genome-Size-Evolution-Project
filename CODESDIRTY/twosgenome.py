#!/usr/bin/env python
from pygsl import rng as rn
import math as mth
import numpy as np
import tsgfuncs as hpm
import pickle
###########################################
#Parameters and Constants Definition
Lh=10  #NUMBER OF HOST  UNITS
Lp=50  #INITIAL NUMBER OF PATHOGEN UNITS
C=0.5  #COST PARAMETER

###########################################
#GENE-POOL SETUP-HYPERCUBES
HP=[]
HP=hpm.getgenesl(2)
#print HP
###########################################
#GENE LIST-C.
