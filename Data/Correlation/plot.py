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
    data = readfArray("out.dat")
    DXX = derivative(data[:, 1], data[:, 0])

    kzsD = data[:, 0][1:] - 0.03
    





    fig, ax = plt.subplots(1, 1,  figsize=(8,6))  # 1 row 1 col
    
    ax.plot(data[:, 0], data[:, 1], color='blue')
    ax.axvline(x=2, color = 'black', linestyle='--', lw=1)

    ax2=ax.twinx()
    ax2.plot(kzsD, DXX, color='red')
    
    ax.legend(loc='best', fontsize=18, frameon = False)
    ax.tick_params(axis = 'both', which = 'both', direction='in', labelsize=28)
    ax.tick_params(axis = 'y', colors='blue')
    ax2.tick_params(axis = 'both', which = 'both', direction='in', labelsize=28)
    ax2.tick_params(axis = 'y', colors='red')
    ax2.set_yticks([-0.2, -0.1])
    # plt.minorticks_on()
    
    ax.set_xlabel(r"$K_z/K$", fontsize=28)
    ax.set_ylabel(r"$\langle \sigma_i^x \sigma_{i+x}^x \rangle$", color='blue', fontsize=28)
    ax2.set_ylabel(r"$d\langle \sigma_i^x \sigma_{i+x}^x \rangle/dK_z$", color='red', fontsize=28)
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

def derivative(Ys, Xs):
    derivatives = []
    for i in range(len(Xs) - 1):
        deltaY = Ys[i+1] - Ys[i]
        deltaX = Xs[i+1] - Xs[i]
        derivatives.append(deltaY / deltaX)
    return np.array(derivatives)

if __name__ == '__main__':
    sys.argv ## get the input argument
    total = len(sys.argv)
    cmdargs = sys.argv
    main(total, cmdargs)
