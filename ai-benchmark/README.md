# ai-benchmark for GPUs on M3
As part of the ongoing [ARDC Environments to Accelerate Machine Learning-Based Discovery project](https://ardc.edu.au/project/environments-to-accelerate-machine-learning-based-discovery/), we are working to better understand the hardware available to researchers who use M3. In future this will allow us to create documentation which will inform researchers how to select the right hardware for their needs. We have used [ai-benchmark](https://pypi.org/project/ai-benchmark/) to gather data about how the [GPUs available on M3](https://docs.massive.org.au/M3/m3users.html) perform across machine learning related activities.

This folder contains the scripts used to run ai-benchmark across our GPUs, including:
- Tesla V100-PCIE-16GB
- Tesla V100-PCIE-32GB
- Tesla P100-PCIE-16GB
- Tesla T4
- Tesla K80
- Tesla P4

ai-benchmark is an open source Python library which evaluates hardware across a range of AI activities, and provides a score for each individual activity, as well as a final;
- Device Inference Score;
- Device Training Score, and;
- Device AI score.

You can compare these results to the ai-benchmark ranking here: http://ai-benchmark.com/ranking_deeplearning.html.

## Information about the scripts 

Each script provided here runs the benchmark 7 times per GPU so any variance can be observed. These scripts are written as [batch jobs](https://docs.massive.org.au/M3/slurm/simple-batch-jobs.html#running-simple-batch-jobs) that once submitted, will be queued and execute when there are sufficient resources available.

The only exception to this are the P4 GPUs, which are used for desktops. The best way to benchmark these is interactively through the [CvL desktop](https://www.cvl.org.au/cvl-desktop/getting-started-with-the-cvl). There is an instruction file on how to run these benchmarks too, called ```p4_instructions.txt```

Each benchmark should take approximately 20 minutes to complete.

## Instructions to run the benchmarks

1. Clone the git repository and then navigate to ai-benchmark

```
$ git clone repository 
$ git pull
$ cd path/to/ARDC-ML/ai-benchmark
```

2. Set up a Python virtual environment so you will be able to install ai-benchmark

```
$ /usr/local/python/3.7.4-static/bin/python3 -m venv benchmark_venv
```

3. Edit the relevant GPU file with your preferred text editor and ensure the path is set to your benchmark directory. The section to edit is clearly marked in the files. For example:

```nano gpu_benchmark.sh```

``` 
############################ EDIT YOUR FILE PATH HERE ###################################
# go to benchmarking folder
# cd path/to/ARDC-ML/ai-benchmark
```

4. Submit the benchmark using sbatch

```
sbatch gpu_benchmark.sh
```

This will then run the benchmarks and save the outputs in ```path/to/ARDC-ML/ai-benchmark/gpu_benchmark_results. ```
