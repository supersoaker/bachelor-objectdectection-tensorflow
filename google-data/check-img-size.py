import numpy as np
import cv2 as cv
import glob
import imutils
import re
import os
from PIL import Image

# Read image data
dir_path = os.path.dirname(os.path.realpath(__file__))
images = sorted(glob.glob(dir_path + '/../darkflow-data/train/images/*.jpg'))

i = 1
for imgNamePath in images:
    im = Image.open(imgNamePath)
    width, height = im.size
    print(imgNamePath)
    if(width <= 0):
        print(imgNamePath)

        https: // books.google.de / books?hl = de & lr = & id = J9b_CH - NrycC & oi = fnd & pg = PP2 & dq = Programming + Computer + Vision +
        with+Python & ots=B_76RZ7Jqx & sig=tUMpfU0ZeUj9Sw90PHryGyLCk60  # v=onepage&q=Programming%20Computer%20Vision%20with%20Python&f=false

        https: // books.google.de / books?id = J9b_CH - NrycC & lpg = PP2 & ots = B_76RZ7Jqx & dq = Programming % 20
        Computer % 20
        Vision % 20
        with% 20Python & lr & hl=de & pg=PP2  # v=onepage&q=Programming%20Computer%20Vision%20with%20Python&f=false 