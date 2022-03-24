using HDF5
using LinearAlgebra
using Glob

function basisPartition(wf, sysIndx, nSites)
    """
    	wf: wavefunction mounted from hdf5
    	sysIndx: Array{Int, 1}, Index of sites for RDM
    	nSites: Int, number of sites of the whole system
    """
    nSys = size(sysIndx)[1]
    envIndx = [i for i = 1:nSites]
    for i = 1:nSys
        filter!(e->e≠sysIndx[i], envIndx)
    end
    nEnv = size(envIndx)[1]
    
    @assert nSys + nEnv == nSites
    
    dimDof = 2
    dimHilSys = dimDof^nSys
    dimHilEnv = dimDof^nEnv

    sysBitConfig = zeros(Bool, (dimHilSys, nSites))
    envBitConfig = zeros(Bool, (dimHilEnv, nSites))

    axisScalar = ones(UInt32, nSites)  # UInt32: upto 2^32 (32 sites ED)
    for i = 1 : nSites
        axisScalar[nSites + 1 - i] *= dimDof^(i - 1)
    end

    for i = 1 : dimDof^nSys
        upperpad::Int = size(digits(dimDof^(nSys - 1), base = 2))[1]
        exBits = digits(i-1, base = 2, pad = upperpad)  # expose bits' position for sys dofs

        for j = 1 : size(sysIndx)[1]
            sysBitConfig[i, sysIndx[j]] = exBits[j]
        end

    end

    for i = 1 : dimDof^nEnv
        upperpad::Int = size(digits(dimDof^(nEnv - 1), base = 2))[1]
        exBits = digits(i-1, base = 2, pad = upperpad)  # expose bits' position for evn dofs

        for j = 1 : size(envIndx)[1]
            envBitConfig[i, envIndx[j]] = exBits[j]
        end

    end


    @assert dimHilSys == size(sysBitConfig)[1]
    @assert dimHilEnv == size(envBitConfig)[1]


    # Index matrix
    matIndx = zeros(UInt32, (dimHilSys, dimHilEnv))    # UInt32: upto 2^32 (32 sites ED)

    for i = 1 : dimHilSys
        for j = 1 : dimHilEnv
            matIndx[i,j] = sum((sysBitConfig[i,:] + envBitConfig[j,:]).* axisScalar) + 1 # +1 is because 1-based
        end
    end
    
    # wavefunction as matrix
    wf_as_mat = zeros(Complex{Float64}, (dimHilSys, dimHilEnv))
    
    for i = 1 : dimHilSys
        for j = 1 : dimHilEnv
            wf_as_mat[i,j] = wf[matIndx[i,j]]
        end
    end
    
    return wf_as_mat
end

# Parameters
sysIndxA = Int8[8,9] .+ 1 # cut a z-bond + 2 y-bond
sysIndxB = Int8[8,9,10] .+ 1 # cut a x-bond + 2 y-bond

Nsite = 24
dirList = ["B_0.03"] # glob("B_*")

Svn = zeros(Float32, (size(dirList)[1], 3))

counter = 1
for bdir in dirList
	R = r"B_(\d+\.\d+)"
	Breg = match(R, bdir)
	B = parse(Float32, Breg.captures[1])
	
	# read data
	hd5 = h5open(bdir * "/dataSpec.hdf5","r")
	dset=hd5["3.Eigen/Wavefunctions"]
	evec=read(dset)
	close(hd5)

	# bipartition of wavefunction
	# A
	@time wf_as_mat_A = basisPartition(evec[1,:], sysIndxA, Nsite)
	@time wf_as_mat_B = basisPartition(evec[1,:], sysIndxB, Nsite)

	#@show size(wf_as_mat);

	# then trace out enironment
	rdmA = wf_as_mat_A * adjoint(wf_as_mat_A)
	entS_A = eigvals(rdmA)
	topop_A = count(i->(i<0), entS_A)
	@show PentS_A = entS_A[topop_A+1:end]  # popped out negative values
	
	# then trace out enironment
	rdmB = wf_as_mat_B * adjoint(wf_as_mat_B)
	entS_B = eigvals(rdmB)
	topop_B = count(i->(i<0), entS_B)
	@show PentS_B = entS_B[topop_B+1:end]  # popped out negative values


	# println("\nEigen Spectrum:"); show(stdout, "text/plain", PentS); println()

	@show eeA = - transpose(PentS_A) * log.(PentS_A)
	@show eeB = - transpose(PentS_B) * log.(PentS_B)
	Svn[counter, 1] = B
	Svn[counter, 2] = eeA
	Svn[counter, 3] = eeB
	global counter = counter + 1
end


io = open("SvN.dat", "w")
for i in 1 : size(dirList)[1]	
	write(io, string(Svn[i,1]) * " " * string(Svn[i,2]) * " " * string(Svn[i,3]) * "\n")
end
close(io)






