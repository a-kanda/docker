docker run --gpus all -u $(id -u):$(id -g) -d -p 8888:8888 -v /work:/tf/work  tensorflow/tensorflow:latest-gpu-py3-jupyter
