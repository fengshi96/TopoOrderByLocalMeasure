#!/bin/sh
#SBATCH --job-name=4.00-0.01|24ED
#SBATCH -N 1
#SBATCH --ntasks=8
#SBATCH -t 48:00:00 			
#SBATCH --mem=180G
#SBATCH --mail-type=FAIL			
#SBATCH --mail-user=feng.934@osu.edu				
hostname
#SBATCH --no-requeue
cd $SLURM_SUBMIT_DIR
module load python/3.7-conda4.5
time
python $EDPY/main.py /fs/byo/trivedi/feng.934/3.Project_2022/3.NAbelian/2.Lanczos/6.L24_4x3/Kzz_4.00/B_0.01/input.inp &> runForInput.cout
time
