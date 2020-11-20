#!/bin/bash
#SBATCH --job-name=k80benchmark
#SBATCH --array=1-7
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
#SBATCH --time=00:30:00
#SBATCH --output=slurm%j.out
#SBATCH --error=slurm%j.err
#SBATCH --partition=m3c

############################ EDIT YOUR FILE PATH HERE ###################################
# go to benchmarking folder
# cd path/to/ARDC-ML/ai-benchmark

# module load CUDA and CUDNN
module load cuda/10.1
module load cudnn/7.6.5-cuda10.1

# activate your virtual environment
source benchmark_venv/bin/activate

# install TensorFlow and ai-benchmark
pip install tensorflow-gpu
pip install ai-benchmark

# make folder to store results
mkdir -p k80_benchmark_results

# run the benchmark seven times and save the outputs
echo "now processing task id:: " ${SLURM_ARRAY_TASK_ID}
python benchmark.py &> k80_benchmark_results/k80_benchmark_${SLURM_ARRAY_TASK_ID}.txt
