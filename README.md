# bachelor-objectdectection-tensorflow



#### Installation
```bash

conda create -n mruescher-bachelor pip python=3.5
conda activate mruescher-bachelor
pip install -r env/requirements.txt
pip install --ignore-installed --upgrade tensorflow
```

#### Usage
generate new images
```bash
pythonw google-data/auto-rectangle.py --xmlPath /../data/probe2/ --imageModifyLevel 3 --savingType voc-xml
```


#### Notices
Using python 3.5 because of "tensorflow-gpu"
built on https://github.com/llSourcell/YOLO_Object_Detection