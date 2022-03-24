import re
import math 
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
    hs = np.arange(0, 0.00205, 0.00005)
    data = readfArray("ESpectrum_2.dat")

    
    fig, ax = plt.subplots(1, 1,  figsize=(8,2))  # 1 row 1 col
    
    for i in range(len(data)):
        for j in range(4):
            ax.scatter(hs[i], data[i, j], color='blue', marker='_')
    
    ax.legend(loc='best', fontsize=18, frameon = False)
    ax.tick_params(axis = 'both', which = 'both', direction='in', labelsize=18)
    # plt.minorticks_on()
    
#     ax.set_yscale('log')
    ax.set_xticks([0.0000, 0.0005, 0.0010, 0.0015, 0.0020])
    ax.set_xticklabels([0, 0.5, 1, 1.5, 2])
    ax.set_yticks([0.2, 0.3])
    ax.set_xlim(xmin=-0.00005, xmax=0.002)
    ax.set_xlabel(r"$h/J_{TC}$", fontsize=18)
    ax.set_ylabel(r"$\lambda(\rho_x)$", fontsize=18)
    # plt.show()
    plt.savefig("figure.pdf", dpi=600, bbox_inches='tight')

























def readfArray(str, Complex = False):
    def toCplx(s):
        if "j" in s:
            return complex(s)
        else:
            repart = float(s.split(",")[0].split("(")[1])
            impart = float(s.split(",")[1].strip("j").split(")")[0])
            return complex(repart,impart)
    
    file = open(str,'r')
    lines = file.readlines()
    file.close()

    # Determine shape:
    row = len(lines)
    testcol = lines[0].strip("\n").rstrip().split()
    col = len(testcol)  # rstip to rm whitespace at the end 

    if Complex:
        m = np.zeros((row, col), dtype=complex)
        for i in range(row):
            if lines[i] != "\n":
                line = lines[i].strip("\n").rstrip().split()
                # print(line)
                for j in range(col):
                    val = toCplx(line[j])
                    m[i, j] = val
        
    else:
        m = np.zeros((row, col), dtype=float)
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
