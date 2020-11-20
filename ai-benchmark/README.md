This folder contains scripts to run ai-benchmark (http://ai-benchmark.com/; https://pypi.org/project/ai-benchmark/) on the GPUs offered on M3 (https://docs.massive.org.au/M3/m3users.html). The open source Python library evaluates hardware across a variety of AI activities and provides scores for each test, as well as a final Device Inference Score, Device Training Score, and overall AI score, which you can compare to their own ranking here: http://ai-benchmark.com/ranking_deeplearning.html.

Each script provided here runs the benchmark 7 times per GPU so any variance can be observed. These scripts are written as batch jobs  that once submitted, will be queued and execute when there are sufficient resources. More information on batch jobs can be found here (https://docs.massive.org.au/M3/slurm/simple-batch-jobs.html#running-simple-batch-jobs)

The only exception to this are the P4 GPUs, which are used for desktops. The best way to benchmark these is interactively through the CvL desktop (https://www.cvl.org.au/cvl-desktop/getting-started-with-the-cvl). There is an instruction file on how to run these benchmarks too.

Each benchmark should take approximately 20 minutes to complete.

To run the benchmarks:

#clone the git repository and then navigate to ai-benchmark
$ git clone repository 
$ cd path/to/ARDC-ML/ai-benchmark

# set up a Python virtual environment so you will be able to install ai-benchmark later
$ /usr/local/python/3.7.4-static/bin/python3 -m venv benchmark_venv

# edit the relevant GPU file with your preferred text editor and ensure the path is set to your benchmark directory
# nano gpu_benchmark.sh for example

# submit the benchmark using sbatch
sbatch gpu_benchmark.sh

This will then run the benchmarks and save the outputs in path/to/ARDC-ML/ai-benchmark/gpu_benchmark/results. 

Note: Tests have been performed to confirm that ai-benchmark does not optimise performance for extra GPU resources (i.e. --gres:gpu:2) or more CPU cores (i.e. --ntasks=4).
