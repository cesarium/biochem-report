#!/bin/python3
import os
import numpy as np
import matplotlib.pyplot as plt

# Search current directory for .xmgr files
Names = os.listdir('.')
names = []
for name in Names:
    if name.endswith('standard.xmgr'):
        names.append(name)

for name in names:

    resid = name[13:15]
    chain = name[15]

    if resid == '25' and chain == 'A':
        res25A = name
    if resid == '25' and chain == 'B':
        res25B = name
    if resid == '21' and chain == 'A':
        res21A = name
    if resid == '21' and chain == 'B':
        res21B = name
    if resid == '29' and chain == 'A':
        res29A = name
    if resid == '29' and chain == 'B':
        res29B = name

# Aspartic acid
dataA = np.loadtxt(res25A).transpose()
dataB = np.loadtxt(res25B).transpose()
with plt.style.context("rcParams.txt"):

    fig,ax = plt.subplots(figsize=(16, 9))
    ax.plot(dataA[0], dataA[1], label = "RDF - A", marker = '.', color = 'navy', ms=25)
    ax.plot(dataB[0], dataB[1], label = "RDF - B", marker = '*', color = 'orange', ms=25)
    ax.set_xlabel('$r$ / $\AA$',fontsize=35), ax.set_ylabel('$g(r)$',fontsize=35)
    plt.yticks(fontsize=22),plt.xticks(fontsize=22)


    
ax2 = ax.twinx()
ax2.plot(dataA[0], dataA[2], label = "$C_{H_2O}$ - A", color = 'navy' , lw = 5)
ax2.plot(dataB[0], dataB[2], label = "$C_{H_2O}$ - B", color = 'orange' , lw = 5)
ax2.set_ylabel('Number of $H_2O$ molecules',fontsize=35)

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0 ,prop={'size': 24})
plt.yticks(fontsize=22)
plt.xlim(5,)
plt.title('RDF : ASP 25',fontsize=35)
plt.tight_layout()
plt.savefig('plots-rdf-ASP25.pdf')
plt.show()


# XXX 21
dataA = np.loadtxt(res21A).transpose()
dataB = np.loadtxt(res21B).transpose()

with plt.style.context("rcParams.txt"):

    fig,ax = plt.subplots(figsize=(16, 9))
    ax.plot(dataA[0], (dataA[1]+dataB[1])/2, label = "RDF", marker = '.', color = 'navy', ms=25)
    ax.set_xlabel('$r$ / $\AA$',fontsize=35), ax.set_ylabel('[ $g_A(r)$ + $g_B(r)$ ] / 2',fontsize=35)
    plt.yticks(fontsize=22),plt.xticks(fontsize=22)

ax2 = ax.twinx()
ax2.plot(dataA[0], (dataA[2] + dataB[2])/2, label = "$C_{H_2O}$", color = 'orange' , lw = 5)
ax2.set_ylabel('Number of $H_2O$ molecules',fontsize=35)

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax2.legend(lines + lines2, labels + labels2, loc=0 ,prop={'size': 24})
plt.yticks(fontsize=22)
plt.title('RDF : GLU 21',fontsize=35)
plt.tight_layout()
plt.savefig('plots-rdf-GLU21.pdf')
plt.show()

# YYY 29
dataA = np.loadtxt(res29A).transpose()
dataB = np.loadtxt(res29B).transpose()

with plt.style.context("rcParams.txt"):

    fig,ax = plt.subplots(figsize=(16, 9))
    ax.plot(dataA[0], (dataA[1]+dataB[1])/2, label = "RDF", marker = '.', color = 'navy', ms=25)
    ax.set_xlabel('$r$ / $\AA$',fontsize=35), ax.set_ylabel('[ $g_A(r)$ + $g_B(r)$ ] / 2',fontsize=35)
    plt.yticks(fontsize=22),plt.xticks(fontsize=22)

ax2 = ax.twinx()
ax2.plot(dataA[0], (dataA[2] + dataB[2])/2, label = "$C_{H_2O}$", color = 'orange' , lw = 5)
ax2.set_ylabel('Number of $H_2O$ molecules',fontsize=35)

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax2.legend(lines + lines2, labels + labels2, loc=0 ,prop={'size': 24})
plt.yticks(fontsize=22)
plt.title('RDF : ASP 29',fontsize=35)
plt.tight_layout()
plt.savefig('plots-rdf-ASP29.pdf')
plt.show()

x = dataA[0]
y1 = (dataA[1] + dataB[1])/2
y2 = (dataA[2] + dataB[2])/2
zy = y1[np.where(y2>1.)[0][0]]
zx = x[np.where(y2>1.)[0][0]]
print(zx,zy)
