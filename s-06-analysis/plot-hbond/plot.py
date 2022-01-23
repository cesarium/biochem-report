#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

f = "hbond-trim.dat"
# f = "ptraj-rmsd-12ns.out"
d = np.loadtxt(f).transpose()

with plt.style.context("rcParams.txt"):

    fig,ax = plt.subplots(figsize=(16, 9))
    ax.errorbar(d[0], d[1], yerr = d[2], label = "comp.", marker = '.',
                color = 'tab:red', ms=15, linestyle='none',
               lw = 0,elinewidth=1.5,ecolor='darkorange')

    ax.set_xlabel('% de occupação',fontsize=35), ax.set_ylabel('Comp. da Ligação / $\AA$',fontsize=35)
    plt.yticks(fontsize=22),plt.xticks(fontsize=22)



ax2 = ax.twinx()
ax2.errorbar(d[0], 180 - d[3], yerr = d[4] , label = r"$\theta$",
             color = 'navy' , marker = '.' , lw = 0, ms = 15,
            elinewidth=1.5, ecolor='dodgerblue')

ax2.set_ylabel(r'$\theta$ / graus',fontsize=35)

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0 ,prop={'size': 24})
plt.yticks(fontsize=22)
plt.xlim(5,)
plt.tight_layout()
plt.savefig('plots-hbonds-linear.pdf')
plt.show()
