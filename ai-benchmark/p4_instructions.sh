# navigate to the directory with your benchmarking stuff in it
[ksco0005@m3-login2 ksco0005] cd ~/nq46/ksco0005/aibench

#load cuda and cudnn
[ksco0005@m3-login2 ksco0005] module load cuda/10.1
[ksco0005@m3-login2 ksco0005] module load cudnn/7.6.5-cuda10.1

#activate virtual env and install TF and ai-bench
[ksco0005@m3-login2 ksco0005] source benching/bin/activate
[ksco0005@m3-login2 ksco0005] pip install tensorflow-gpu
[ksco0005@m3-login2 ksco0005] pip install ai-benchmark

#run the benchmarks
[ksco0005@m3-login2 ksco0005] python benchmark.py &> p4_benchmark_1.txt
[ksco0005@m3-login2 ksco0005] python benchmark.py &> p4_benchmark_2.txt
[ksco0005@m3-login2 ksco0005] python benchmark.py &> p4_benchmark_3.txt
[ksco0005@m3-login2 ksco0005] python benchmark.py &> p4_benchmark_4.txt
[ksco0005@m3-login2 ksco0005] python benchmark.py &> p4_benchmark_5.txt
[ksco0005@m3-login2 ksco0005] python benchmark.py &> p4_benchmark_6.txt
[ksco0005@m3-login2 ksco0005] python benchmark.py &> p4_benchmark_7.txt

