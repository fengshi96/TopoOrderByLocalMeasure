import re, math
import sys
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('text', usetex=True)

def main(total, cmdargs):
    if total != 1:
        print (" ".join(str(x) for x in cmdargs))
        raise ValueError('redundent args')

    # main codes
    gammas = readfArray("gammas.dat")
    topo = readfArray("topoEE.dat")

    kzs = gammas[:, 0]

    fig, ax = plt.subplots(1, 1,  figsize=(8,6))  # 1 row 1 col
    
    ax.plot(kzs, gammas[:, 1], marker='s', label=r"$1+2$ (Fig.2c)")
    ax.plot(kzs, gammas[:, 2], marker='s', label=r"$2+3$ (Fig.2b)")
    ax.plot(kzs, gammas[:, 3], marker='s', label=r"$2+4$")
    ax.plot(kzs, gammas[:, 4], marker='s', label=r"$2+5$")
    ax.plot(kzs, -topo[:, 0], marker='s', label="Kitaev-Preskill")
    ax.axhline(y=math.log(2), color = 'black', linestyle='--', lw=1)

    ax.legend(loc='best', fontsize=18, frameon=False)
    ax.tick_params(axis = 'both', which = 'both', direction='in', labelsize=28)
    plt.ylim(ymin=0.2, ymax=1)
    plt.xlim(xmin=1.8, xmax=8.2)
    
    
    
#     ax.set_yticks([0.2, 0.4, 0.6, 0.69, 0.8, 1.0])
#     ax.set_yticklabels(['0.2', '0.4', '0.6', 'log2' '0.8', '1.0'])
    ax.set_xlabel(r"$K_z/K$", fontsize=28)
    ax.set_ylabel(r"$\gamma$", fontsize=28)
    # plt.show()
    plt.savefig("figure.pdf", dpi=600, bbox_inches='tight')
#

#     gammas = readfArray("gammas2.dat")
#     topo = readfArray("topoEE2.dat")
# 
#     kzs = gammas[:, 0]
# 
#     fig, ax = plt.subplots(1, 1,  figsize=(7,6))  # 1 row 1 col
#     
#     ax.plot(kzs, gammas[:, 1], marker='^', label=r"$1+2$")
#     ax.axhline(y=math.log(2), color = 'black', linestyle='--', lw=1)
# 
#     ax.legend(loc='best', fontsize=28, frameon=False)
#     ax.tick_params(axis = 'both', which = 'both', direction='in', labelsize=32)
#     plt.ylim(ymin=0.6, ymax=0.9)
# #     plt.xlim(xmin=1.8, xmax=8.2)
#     
#     
#     
# #     ax.set_yticks([0.2, 0.4, 0.6, 0.69, 0.8, 1.0])
# #     ax.set_yticklabels(['0.2', '0.4', '0.6', 'log2' '0.8', '1.0'])
# #     ax.set_xlabel(r"$K_z/K$", fontsize=28)
# #     ax.set_ylabel(r"$\gamma$", fontsize=28)
#     # plt.show()
#     plt.savefig("figure.pdf", dpi=600, bbox_inches='tight')
    























def readfArray(str, Complex = False):
    file = open(str,'r')
    lines = file.readlines()
    file.close()

    # Determine shape:
    row = len(lines)
    testcol = lines[0].strip("\n").rstrip().split()
    col = len(testcol)  # rstip to rm whitespace at the end 

    m = np.zeros((row, col))
    for i in range(row):
        if lines[i] != "\n":
            line = lines[i].strip("\n").rstrip().split()
            # print(line)
            for j in range(col):
                val = float(line[j])
                m[i, j] = val
    return m



if __name__ == '__main__':
    sys.argv ## get the input argument
    total = len(sys.argv)
    cmdargs = sys.argv
    main(total, cmdargs)
