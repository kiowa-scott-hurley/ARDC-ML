# Instructions to run this example job
This contains an example Python file to test the job monitoring script with. The Python file is taken from the Data Fluency Introduction to Deep Learning and Tensorflow course located here: https://github.com/MonashDataFluency/intro-to-tensorflow. It is a simple Tensorflow script which trains a convolutional neural network (CNN) to classify the MNIST dataset. 

This example assumes you have a conda environment with tensorflow-gpu installed, and that the normal commands to run the job would be:

```
cd path/to/your/Intro_to_CNNs.py
source path/to/conda/bin/activate
conda activate CNN_venv

python Intro_to_CNNs.py
```

Edit the job monitoring script per the instructions on the other page to reflect this, or to reflect the method you would usually use to run a Python script. 

Included in this repo is an example filtered log file `nvidia-filtered.log` from monitoring this job so you can see how it looks in the Jupyter notebook. 

You'll still need to edit the notebook filepath to this logfile, and update where the plots are saved.
