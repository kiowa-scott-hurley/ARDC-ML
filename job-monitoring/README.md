# Job Monitoring on M3.
Note: This documentation is under active development, meaning that it can change over time as we refine it. Please email help@massive.org.au if you require assistance, or have suggestions to improve this documentation.

This folder includes templates required to monitor a Python job on MASSIVE, and a Jupyter notebook to analyse the outputs. 

We have included an example with concrete steps in CNN_example/README.md which we recommend you try first.

It is important to note the job monitoring template provided here is set up specifically for Python jobs - if you require assisstance editing it to be appropriate for other jobs please email us at help@massive.org.au.

## Instructions to monitor your own job
Having visibility over how your job runs can help you understand if your job is spending a lot of energy moving files around, or if it’s using the GPUs to their fullest capacity. This job monitoring script will allow you to gather metrics about your job, and then examine the outputs in a Jupyter notebook. 

There are three steps to this process.

1. Editing the job monitoring file.
2. Running the job monitoring file, and filtering the output.
3. Editing the Jupyter notebook to visualise the results. 

These instructions differ slightly depending on if you're running an interactive job using [smux](https://docs.massive.org.au/M3/slurm/interactive-jobs.html?highlight=smux) or the [CvL desktop](https://docs.massive.org.au/M3/connecting/connecting-via-strudel.html?highlight=desktop), or if you're submitting a job to the queue using [sbatch](https://docs.massive.org.au/M3/slurm/simple-batch-jobs.html). 

### Step One: Monitoring the Job
In order to monitor your job, you'll need to make two edits to `job_monitoring_template.bash` using your favourite text editor. 

The first section to edit is where you are setting up the environment to run your job. For example, this might include performing module loads, or activating virtual environments. Anything that needs to happen before your job runs should be put here.

```
# Set up your environment
# ###############################################################

# Insert your environment set up commands here
# module load software
# cd to/your/directory

# ################################################################
```

The second section to edit is where you actually insert the command you would usually use to run your job. You must ensure you add an "&" to the end of your command.

```
# Insert the command you want to monitor here, and add an “&” to the end of it
# ###############################################################

python your/python/job &

# ###############################################################
```

Once you have made these edits, save the job monitoring file. 

### Step Two: Running the job monitoring script, and filtering the output (smux or desktop)

Once you have your edited job monitoring script, you'll want to run it.
```
./job_monitoring_template.bash
```
It will output a logfile called `nvidia-$LOGDATE.log`.

In order to make this logfile readable to pandas in the Jupyter notebook, you'll need to filter the data with the following command:

```
export DATE=$LOGDATE; cat nividia-$DATE.log | grep -v 'gpu\|Idx' > nvidia-$DATE-filtered.log
```
This creates a file called nvidia-$DATE-filtered.log which you will use in the Jupyter notebook.

### Step Two: Running the job monitoring script, and filtering the output (sbatch)

Once you have edited your job monitoring script, you'll want to run it in an sbatch script. For example;
```
#!/bin/bash
#SBATCH --job-name=MyJob
#SBATCH --account=ab12
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=4096
#SBATCH --gres=gpu:V100:1
#SBATCH --partition=m3g

./job_monitoring_template.bash
```
Once this has ran you will have a file called `nvidia-$LOGDATE.log`.

In order to make this logfile readable to pandas in the Jupyter notebook, you'll need to filter the data with the following command:

```
export DATE=$LOGDATE; cat nividia-$DATE.log | grep -v 'gpu\|Idx' > nvidia-$DATE-filtered.log
```
You could add this command to your sbatch job submission script. This creates a file called nvidia-$DATE-filtered.log which you will use in the Jupyter notebook to visualise your resource utilisation. 

### Step Three: Visualising results in the Jupyter Notebook

We have provided a Jupyter notebook called `gpu-usage.ipynb`. You can open this in the [Strudel desktop](https://docs.massive.org.au/M3/connecting/connecting-via-strudel.html?highlight=desktop) using the terminal and the browser, or with [Strudel2 Beta's JupyterLab](https://docs.massive.org.au/M3/connecting/strudel2/connecting-to-jupyter-lab.html?highlight=jupyterlab) feature. 

Once you open `gpu-usage.ipynb`, there are a few things you will need to edit before running the cells.

Firstly, you need to edit 
```
logfile = 'your/logfile/nvidia-$DATE-filtered.log'
```
so the notebook accesses the filtered logfile. 

Secondly, in all of the plots there is a line which will save them. Edit this to reflect the directory you would like your plots saved to.

```
# Edit with your filepath
matplotlib.pyplot.savefig('your/place/to/save/plots' + filename, dpi = (300), facecolour=fig.get_facecolor())
```

Once you've made these edits, you should be able to run the cells and see some plots. 

More information about what these plots represent is to be added to this documentation shortly.
