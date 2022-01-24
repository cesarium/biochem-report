#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

# Search current directory for .xmgr files
f = "ptraj-rmsd.out"
# f = "ptraj-rmsd-12ns.out"
d = np.loadtxt(f).transpose()

with plt.style.context("rcParams.txt"):
    plt.plot(d[0],d[1], marker = '.')
    plt.xlabel("Tempo de Produção / ps",fontsize=35), plt.ylabel('RMSD / $\AA$',fontsize=35)
    plt.title("Evolução da RMSD ao longo da produção",fontsize=35), plt.tight_layout()
    plt.savefig('plots-rmsd.pdf')
