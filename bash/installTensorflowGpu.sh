#!/usr/bin/env bash
# this is experiential, on my mac that this does not work
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/gpu/tensorflow_gpu-0.12.1-py3-none-any.whl
pip install --upgrade $TF_BINARY_URL
export CUDA_HOME=/usr/local/cuda
export DYLD_LIBRARY_PATH="$CUDA_HOME/lib:$CUDA_HOME:$CUDA_HOME/extras/CUPTI/lib"
export LD_LIBRARY_PATH=$DYLD_LIBRARY_PATH
sudo ln -s /usr/local/cuda/lib/libcuda.dylib ln -s /usr/local/cuda ./usr/local/cuda/lib/libcuda.1.dylib
# for further information see
# https://github.com/tensorflow/tensorflow/issues/6729#issuecomment-279483546 and
# https://github.com/tensorflow/tensorflow/issues/6729#issuecomment-279523633
