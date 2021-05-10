#!/bin/bash
#SBATCH --job-name=v10032bench
#SBATCH --array=1-7
#SBATCH --mem=64G
#SBATCH --gres=gpu:V100:1
#SBATCH --time=00:30:00
#SBATCH --output=./v100_32GB_benchmark_results/slurm%j.out
#SBATCH --error=slurm%j.err
#SBATCH --partition=m3g
#SBATCH --constraint="V100-32G"

############################ EDIT YOUR FILE PATH HERE ###################################
# go to benchmarking folder
# cd path/to/ARDC-ML/ai-benchmark

# module load CUDA and CUDNN
module load cuda/11.0 
module load cudnn/8.0.5-cuda11

# activate your virtual environment
source benchmark_venv/bin/activate

# make folder to store results
mkdir -p v100_32GB_benchmark_results

echo "now processing task id:: " ${SLURM_ARRAY_TASK_ID}
python benchmark.py &> v100_32GB_benchmark_results/v100_32GB_benchmark_${SLURM_ARRAY_TASK_ID}.txt

