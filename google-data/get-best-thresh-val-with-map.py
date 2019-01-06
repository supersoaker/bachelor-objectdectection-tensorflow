import subprocess
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start', default='0.17', help='start threshold value')
parser.add_argument('--end', default='0.18', help='end threshold value')
parser.add_argument('--step', default='0.001', help='step for iterating best threshold value')

i = float(parser.start)
while (i < float(parser.end)):
    print('loading with thresval: ' + str(i))
    subprocess.run([
        './flow --imgdir ./bachelor-objectdectection-tensorflow/data/probe2/test/ --model cfg/tiny-yolo-ipm.cfg --load 255 --gpu 1.0 --threshold ' + str(
            i) + ' --txt'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, shell=True)
    result = subprocess.run(['python mAP/main.py'], stdout=subprocess.PIPE, shell=True)
    output = result.stdout.decode('utf-8')
    p = re.findall(r'mAP = (.*)%', output, re.MULTILINE)
    print(p)
    i = i + float(parser.step)
