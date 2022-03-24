#!/bin/sh
#SBATCH --job-name=wp4.00-B_0.01|24
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
python /home/feng.934/Codes/0.Codes/ExactDiagPy/observe.py input.inp Cx 8 &> correlationX.out
echo "Cx for B=B_0.01 is Done!"
python /home/feng.934/Codes/0.Codes/ExactDiagPy/observe.py input.inp Cy 8 &> correlationY.out
echo "Cy for B=B_0.01 is Done!"
python /home/feng.934/Codes/0.Codes/ExactDiagPy/observe.py input.inp Cz 8 &> correlationZ.out
echo "Cz for B=B_0.01 is Done! \n"
time
