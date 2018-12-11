import numpy as np
import cv2 as cv
import glob
import imutils
import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# Read image data
images = sorted(glob.glob(dir_path + '/*/*/*.jpg'))
dataDirectories = sorted(glob.glob(dir_path + '/*/'))
dataFiles = {}

# Creating new csv for each data directory
for dirName in dataDirectories:
    dirName = dirName[:-1] # slice out last trailing slash
    file = open(dirName + '.csv', 'w')
    # file.write("%s;%s;%s;%s;%s;%s;%s;%s\n" % ('filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax'))
    file.write("")
    file.close()
    file = open(dirName + '.csv', 'a')
    dataFiles[dirName.replace(dir_path + '/', '', 1)] = file


i = 1
for imgNamePath in images:
    # print(imgNamePath)
    img = cv.imread(imgNamePath)

    imgNamePath = imgNamePath.replace(dir_path + '/', '', 1)

    regex = r"^(.*?)\/(.*?)\/.*$"

    dataDir = re.findall(regex, imgNamePath)[0][0]
    objectType = re.findall(regex, imgNamePath)[0][1]

    # Adding white border, because some images are to big
    img = cv.copyMakeBorder(img, 50, 50, 50, 50, cv.BORDER_CONSTANT, value=[255, 255, 255])

    # Define colors and threshold for contours
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    white_bg = 255 * np.ones_like(img)
    ret, thresh = cv.threshold(gray, 60, 255, cv.THRESH_BINARY_INV)
    blur = cv.medianBlur(thresh, 1)
    kernel = np.ones((10, 20), np.uint8)

    imgOrg = img.copy()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 11, 17, 17)
    img = cv.Canny(gray, 30, 200)

    # Use OpenCv for finding contours
    img_dilation = cv.dilate(blur, kernel, iterations=1)
    im2, ctrs, hier = cv.findContours(img.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    ## sort the containers
    ctrs = cv.findContours(img.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    ctrs = imutils.grab_contours(ctrs)
    ctrs = sorted(ctrs, key=cv.contourArea, reverse=True)[:10]

    imgHeight, imgWidth = img.shape

    # cv.imshow('Object detector', edged)

    # Foreach container found
    for cnt in ctrs:
        x, y, w, h = cv.boundingRect(cnt)
        # if w / imgWidth < 0.3 or h / imgHeight < 0.3:
        #     continue
        # if (h < 50 and w < 50) or h > 200:
        #     continue
        cv.rectangle(imgOrg, (x, y), (x + w, y + h), (255, 255, 0), 2)
        # csvStr = "%s;%s;%s;%s;%s;%s;%s;%s\n" % (imgNamePath, w, h, objectType, x, y, x + w, y + h)
        if(objectType == 'gauge'):
            objectType = 0
        if(objectType == 'handwheel'):
            objectType = 1
        if(objectType == 'valve'):
            objectType = 2
        csvStr = "%s %s,%s,%s,%s,%s\n" % (imgNamePath, x, y, x + w, y + h, objectType)
        dataFiles[dataDir].write(csvStr)
        break

    # Show the image with a python window
    # cv.imshow('Object detector', imgOrg)

    # # Press any key to close the image
    # cv.waitKey(0)
    #
    # # Clean up
    # cv.destroyAllWindows()
    print('Verarbeitet: ' + ("%.2f" % (i / len(images) * 100) + '%'))
    i = i + 1

# filename,width,height,class,xmin,ymin,xmax,ymax
# tong-line-tong-torque.png,400,400,gauge,28,146,180,289

# https://github.com/qqwweee/keras-yolo3
# x_min,y_min,x_max,y_max,class_id