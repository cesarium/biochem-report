#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

fA = "prot-nelf-MD2-distA.list"
fB = "prot-nelf-MD2-distB.list"
fC = "prot-nelf-MD2-distC.list"
fD = "prot-nelf-MD2-distD.list"

dA = np.loadtxt(fA).transpose()
dB = np.loadtxt(fB).transpose()
dC = np.loadtxt(fC).transpose()
dD = np.loadtxt(fD).transpose()

with plt.style.context("rcParams.txt"):
    mA , mB , mC , mD = np.mean(dA[1]), np.mean(dB[1]), np.mean(dC[1]), np.mean(dD[1])
    sA , sB , sC , sD = np.std(dA[1]), np.std(dB[1]), np.std(dC[1]), np.std(dD[1])
    
    plt.plot(dA[0],dA[1], label = "chain A : OD1 - A | $\mu$ = {:.2f} $\AA$ | $\sigma$ = {:.2f} $\AA$".format(mA,sA), marker = '.')
    plt.plot(dB[0],dB[1], label = "chain A : OD2 - B | $\mu$ = {:.2f} $\AA$ | $\sigma$ = {:.2f} $\AA$".format(mB,sB), marker = '.')
    plt.plot(dC[0],dC[1], label = "chain B : OD1 - C | $\mu$ = {:.2f} $\AA$ | $\sigma$ = {:.2f} $\AA$".format(mC,sC), marker = '.')
    plt.plot(dD[0],dD[1], label = "chain B : OD2 - D | $\mu$ = {:.2f} $\AA$ | $\sigma$ = {:.2f} $\AA$".format(mD,sD), marker = '.')
    
    plt.axhline(y=mA , linestyle='-', lw = 4, color = 'tab:blue')
    print("mA = ", mA)
    plt.axhline(y=mB , linestyle='-', lw = 4, color = 'tab:orange')
    print("mB = ", mB)
    plt.axhline(y=mC , linestyle='-', lw = 4, color = 'tab:green')
    print("mC = ", mD)
    plt.axhline(y=mD , linestyle='-', lw = 4, color = 'tab:red')
    print("mD = ", mD)
    
    plt.xlabel("Tempo de Produção / ps",fontsize=35), plt.ylabel('Distância / $\AA$',fontsize=35)
    plt.legend(loc='upper center', ncol=2, fancybox=True,mode='expand')
    plt.tight_layout()
    plt.savefig('plots-ASP-1UN.pdf')
