#!/bin/python3
import os
import numpy as np
import matplotlib.pyplot as plt

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

# Search current directory for .xmgr files
Names = os.listdir('.')
names = []
for name in Names:
    if name.startswith('summary'):
        names.append(name)

sm = 'summary.'
dens = 'DENSITY'
epot = 'EPTOT'
temp = 'TEMP'
volu = 'VOLUME'
pres = 'PRES'

d_dens = np.loadtxt( sm + dens , skiprows = 201).transpose()
d_pres = np.loadtxt( sm + pres ).transpose()
d_volu = np.loadtxt( sm + volu , skiprows = 201).transpose()
d_temp = np.loadtxt( sm + temp ).transpose()
d_epot = np.loadtxt( sm + epot ).transpose()

d_pres3 = np.loadtxt('summary3.PRES').transpose()

with plt.style.context("rcParams.txt"):
    #11.69,8.27
    fig, axs = plt.subplots(5)

    # Density
    axs[0].plot(d_dens[0],d_dens[1], marker = '.', color = 'navy' , linestyle="None")
    axs[0].set_ylabel('Densidade / g cm$^{-3}$')
    axs[0].set_xlim(0,)

    # Pressure
    axs[1].plot(d_pres[0],d_pres[1], marker = '.', color = 'navy' , linestyle="None")
    x = d_pres[0][201:]
    z = d_pres[1][201:]
    y = moving_average(z,15)
    #y = y.cumsum()/np.arange(1,len(y)+1,1)# Pressure mean
    axs[1].plot( x[7:-7], y , linewidth=5. , color='tab:red')
    axs[1].set_ylabel('Pressão / bar')
    axs[1].set_xlim(0,)
    axs[1].axhline(y=1,color = "orange", linewidth = 3.5)

    # Volume
    axs[2].plot(d_volu[0],d_volu[1], marker = '.', color = 'navy' , linestyle="None")
    axs[2].set_ylabel('Volume / cm$^{3}$')
    axs[2].ticklabel_format(axis='y',style='sci',scilimits=(5,0))

    # Temperature
    axs[3].plot(d_temp[0],d_temp[1], marker = '.', color = 'navy' , linestyle="None")
    axs[3].set_ylabel('Temperatura / K')

    # Pot energy
    axs[4].plot(d_epot[0],d_epot[1], marker = '.', color = 'navy' , linestyle="None")
    axs[4].set_ylabel('$E_{pot}$ / kcal$\cdot$ mol$^{-1}$')
    axs[4].ticklabel_format(axis='y',style='sci',scilimits=(5,0))

    for ax in axs:
        ax.axvline(x=20, color = "orange", linewidth = 3.5)
        ax.set_xlim(-5,)

    plt.xlabel("Tempo / ps")
    fig.suptitle('Variáveis termodinâmicas durante Dinâmica Molecular\n',fontsize=35)
    fig.tight_layout()
    fig.savefig('plots-summary.pdf')
