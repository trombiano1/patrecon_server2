#!/bin/sh
#SBATCH -p v
#SBATCH -t 1:0:00
#SBATCH --gres=gpu:2
export PATH=/home/app/cuda/bin:$PATH
export LD_LIBRARY_PATH=/home/app/cuda/lib64:$LD_LIBRARY_PATH
echo CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES
srun python test2.py