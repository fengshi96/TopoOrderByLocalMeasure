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
    datax = readfArray("Gaps_28-xh_0.0.dat")
    datay = readfArray("Gaps_28-yh_0.0.dat")
    dataz = readfArray("Gaps_28-zh_0.0.dat")
    datam = readfArray("Gaps_28-h_0.0.dat")

    datam[0:25,1] = 0
    print(datam)

    kzs = datax[:, 0]

    fig, ax = plt.subplots(1, 1,  figsize=(8,6))  # 1 row 1 col
    
    ax.plot(kzs, datax[:, 1], marker='*', color='blue', label=r"$B_p \otimes B_p$")
    ax.plot(kzs, dataz[:, 1], marker='+', color='blue', label=r"$A_s \otimes B_p$")
    ax.axvline(x=2, color = 'black', linestyle='--', lw=1)
    ax.set_yscale('log')

    ax2=ax.twinx()
    ax2.plot(kzs, datam[:, 1], marker='s', color='red', label="Majorana")

    
    ax.legend(loc='lower left', fontsize=24, frameon = False)
    ax.tick_params(axis = 'both', which = 'both', direction='in', labelsize=28)
    ax.tick_params(axis = 'y', colors='blue')
    ax2.legend(loc='upper right', fontsize=20, frameon = False)
    ax2.tick_params(axis = 'both', which = 'both', direction='in', labelsize=28)
    ax2.tick_params(axis = 'y', colors='red')
    # plt.minorticks_on()
    
    ax.set_xlabel(r"$K_z/K$", fontsize=28)
    ax.set_ylabel(r"$\Delta_f$",  color='blue', fontsize=28)
    ax2.set_ylabel(r"$\Delta_m$",  color='red', fontsize=28)
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
