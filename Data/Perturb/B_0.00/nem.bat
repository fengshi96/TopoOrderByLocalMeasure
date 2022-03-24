#!/bin/sh
#SBATCH --job-name=nem-0.00|24
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
python ../../nem.py input.inp correlation 1 2 &> nem.out
time
