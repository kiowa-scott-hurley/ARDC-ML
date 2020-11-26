#!/bin/bash
# A script to monitor gpu and cpu usage for arbitrary commands (Python flavour?) 

# Define BASH functions for monitoring 

outputcputime () {
   while true
   do
 getcputime | ts %.s >> cputime-$LOGDATE.log
      sleep 1
   done
}

getcputime () {
    local proc="python"
    local clk_tck=$(getconf CLK_TCK)
    local usercputime=0
    local syscputime=0
    local pids=$(pgrep $proc)
    for pid in $pids;
    do
        local stats=$(cat "/proc/$pid/stat")
        local statarr=($stats)
        local utime=${statarr[13]}
        local stime=${statarr[14]}
        usercputime=$(bc <<< "scale=3; $usercputime + $utime / $clk_tck")
        syscputime=$(bc <<< "scale=3; $syscputime + $stime / $clk_tck")
    done
    echo $usercputime $syscputime
}

# Setup variables 
LOGDATE=`date +%s`

# Set up your environment here
# ###############################################################

cd path/to/job-monitoring/CNN_example
source path/to/conda/bin/activate
conda activate CNN

# ################################################################

# Export environment to file for determining running parameters
env > environment-$LOGDATE.log

# Insert the command you want to monitor here, and add an “&” to the end of it
# ###############################################################

python path/to/job-monitoring/CNN_example/Intro_to_CNNs.py

# ###############################################################

# Monitoring the job

PID1=$!
echo $PID1
echo Running program PID: $PID1;

PYTHONPID=`pgrep python |sed 's/ /,/g'`
printf "PythonPIDs=",$PYTHONPID\\n
# Record gpu usage for node
nvidia-smi dmon -s umtp -i 0 -d 1 | ts %.s > nvidia-$LOGDATE.log &
# Loop to record user and sys cpu times from proc
outputcputime &

echo Job Monitoring Complete
