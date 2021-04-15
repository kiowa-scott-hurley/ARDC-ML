# Job Monitoring on M3.
Note: This documentation is under active development, meaning that it can change over time as we refine it. Please email help@massive.org.au if you require assistance, or have suggestions to improve this documentation.

This folder includes templates required to monitor a Python job on MASSIVE, and a Jupyter notebook to analyse the outputs. 

It is important to note the job monitoring template provided here is set up specifically for Python jobs - if you require assisstance editing it to be appropriate for other jobs please email us at help@massive.org.au.

This also assumes you are using a desktop or smux session while monitoring.

## Instructions to monitor your own job
Having visibility over how your job runs can help you understand if your job is spending a lot of energy moving files around, or if it’s using the GPUs to their fullest capacity. This job monitoring script will allow you to gather metrics about your job, and then examine the outputs in a Jupyter notebook. 

There are three steps to this process.

1. Editing the job monitoring file.
2. Running the job monitoring file, and filtering the output.
3. Editing the Jupyter notebook to visualise the results. 

## Step One: Monitoring the Job
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

## Step Two: Running the job monitoring script, and filtering the output

Once you have your job monitoring script, you'll want to run it.
```
./job_monitoring_template.bash
```
It will output a logfile called `nvidia-$LOGDATE.log`.

In order to make this logfile readable to pandas in the Jupyter notebook, you'll need to filter the data with the following command:

```
export DATE=$LOGDATE; cat nvidia-$DATE.log | grep -v 'gpu\|Idx' > nvidia-$DATE-filtered.log
```
This creates a file called nvidia-$DATE-filtered.log which you will use in the Jupyter notebook.

## Step Three: Visualising results in the Jupyter Notebook

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
