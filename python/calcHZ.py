import numpy as np

def calcHZ(Lstar, riCi=0, roCi=2):
    riCriticalFlux =  [1.1,1.4,1.76]
    roCriticalFlux =  [.32,.36,.53]
    
    ri = np.round(np.sqrt(Lstar/riCriticalFlux[riCi]), 1)
    ro = np.round(np.sqrt(Lstar/roCriticalFlux[roCi]), 3)
    
    return ri, ro


