import subprocess
import re

i = 0.15
while (i < 0.2):
    subprocess.run([
        './flow --imgdir ./bachelor-objectdectection-tensorflow/data/probe2/test/ --model cfg/tiny-yolo-ipm.cfg --load 255 --gpu 1.0 --threshold 0.173 --txt'],
        stdout=subprocess.PIPE, shell=True)
    result = subprocess.run(['python mAP/main.py'], stdout=subprocess.PIPE, shell=True)
    output = result.stdout.decode('utf-8')
    p = re.findall(r'mAP = (.*)%', output, re.MULTILINE)
    print(p)
    i = i + 0.05
