#!/bin/sh
#SBATCH --job-name=wp4.00-0.02|24
#SBATCH -N 1
#SBATCH --ntasks=8
#SBATCH -t 2:00:00 			
#SBATCH --mem=20G
#SBATCH --mail-type=FAIL			
#SBATCH --mail-user=feng.934@osu.edu				
hostname
#SBATCH --no-requeue
cd $SLURM_SUBMIT_DIR
module load python/3.7-conda4.5
time
python ../../wp.py /fs/byo/trivedi/feng.934/3.Project_2022/3.NAbelian/2.Lanczos/6.L24_4x3/Kzz_4.00/B_0.02/input.inp &> Wp.dat
time
