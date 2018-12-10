# bachelor-objectdectection-tensorflow



#### Installation
```bash

conda create -n mruescher-bachelor pip python=3.5
conda activate mruescher-bachelor
pip install -r env/requirements.txt
pip install --ignore-installed --upgrade tensorflow
```

export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/gpu/tensorflow_gpu-0.12.1-py3-none-any.whl
pip install --upgrade $TF_BINARY_URL

export CUDA_HOME=/usr/local/cuda
export DYLD_LIBRARY_PATH="$CUDA_HOME/lib:$CUDA_HOME:$CUDA_HOME/extras/CUPTI/lib"
export LD_LIBRARY_PATH=$DYLD_LIBRARY_PATH
sudo ln -s /usr/local/cuda/lib/libcuda.dylib ln -s /usr/local/cuda ./usr/local/cuda/lib/libcuda.1.dylib


#### 


#### Notices
Using python 3.5 because of "tensorflow-gpu"