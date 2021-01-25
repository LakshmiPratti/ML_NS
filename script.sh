#!/bin/bash
#SBATCH -A student
#SBATCH --qos=medium
#SBATCH -c 10
#SBATCH -n 1
#SBATCH --gres=gpu:4
#SBATCH --mem-per-cpu=2048
#SBATCH --time=4-00:00:00
#SBATCH --mail-type=END
#SBATCH -o output.txt 
#SBATCH --job-name=DLasgn

echo "Job Started"
cd  /Data/sci477/
echo "Running Script"
python3 code.py
echo "Job Finished"
