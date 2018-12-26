import numpy as np
import cv2 as cv
import glob
import imutils
import re
import os

savingType = 'voc-xml'  # 'voc-xml' or 'csv-with-array-keys' or 'csv-with-object-name' or 'Cartucho/mAP'
xmlFilePathPrefix = '/../data/'

# Read image data
dir_path = os.path.dirname(os.path.realpath(__file__))
images = sorted(glob.glob(dir_path + '/../data/*/*/*.jpg'))
dataDirectories = sorted(glob.glob(dir_path + '/*/'))
dataFiles = {}

# Creating new csv for each data directory
for dirName in dataDirectories:
    dirName = dirName[:-1]  # slice out last trailing slash
    file = open(dirName + '.csv', 'w')
    file.write("")
    if (savingType == 'csv-with-object-name'):
        file.write("%s;%s;%s;%s;%s;%s;%s;%s\n" %
                   ('filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax'))
    file.close()
    file = open(dirName + '.csv', 'a')
    dataFiles[dirName.replace(dir_path + '/', '', 1)] = file

i = 1
for imgNamePath in images:
    # print(imgNamePath)
    img = cv.imread(imgNamePath)

    imgNamePath = imgNamePath.replace(dir_path + '/', '', 1)

    regex = r"^(.*?)\/(.*?)\/_main/.*?/(.*)\.jpg$"

    dataDir = re.findall(regex, imgNamePath)[0][0]
    objectType = re.findall(regex, imgNamePath)[0][1]
    imgName = re.findall(regex, imgNamePath)[0][2]

    # Adding white border, because some images are to big
    # img = cv.copyMakeBorder(img, 50, 50, 50, 50, cv.BORDER_CONSTANT, value=[255, 255, 255])

    # Define colors and threshold for contours
    # gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # white_bg = 255 * np.ones_like(img)
    # ret, thresh = cv.threshold(gray, 60, 255, cv.THRESH_BINARY_INV)
    # blur = cv.medianBlur(thresh, 1)
    # kernel = np.ones((10, 20), np.uint8)

    imgOrg = img.copy()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.bilateralFilter(gray, 11, 17, 17)
    img = cv.Canny(gray, 30, 200)
    # ret, img = cv.threshold(img, 60, 255, cv.THRESH_BINARY_INV)
    ret, img = cv.threshold(img, 0, 255, 0)

    # imgOrg2 = img.copy()
    # src = cv.imread(imgOrg2)
    # tmp = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # _, alpha = cv.threshold(tmp, 0, 255, cv.THRESH_BINARY)
    # b, g, r = cv.split(src)
    # rgba = [b, g, r, alpha]
    # dst = cv.merge(rgba, 4)
    # cv.imshow(imgOrg2, img)

    # Use OpenCv for finding contours
    # img_dilation = cv.dilate(blur, kernel, iterations=1)
    # im2, ctrs, hier = cv.findContours(img.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # ret, thresh = cv.threshold(img, 60, 255, cv.THRESH_BINARY_INV)
    #
    ## sort the containers
    img = cv.convertScaleAbs(img)
    ctrs = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    ctrs = imutils.grab_contours(ctrs)
    ctrs = sorted(ctrs, key=cv.contourArea, reverse=True)[:10]

    # thresh, img = cv.threshold(img, 128, 255, 0)
    #
    # ctrs = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # ctrs = imutils.grab_contours(ctrs)
    # ctrs = sorted(ctrs, key=cv.contourArea, reverse=True)[:10]

    # cv.drawContours(image, contours, -1, (0, 255, 0), 3)

    imgHeight, imgWidth = img.shape

    # cv.imshow('Object detector', edged)

    # Foreach container found
    for cnt in ctrs:
        x, y, w, h = cv.boundingRect(cnt)
        w = x + w
        h = h + y

        if (imgName == '26'):
            x, y, w, h = (69, 1, 432, 399)
        elif (imgName == '02'):
            x, y, w, h = (173, 143, 880, 990)
        elif (imgName == '03'):
            x, y, w, h = (137, 79, 360, 329)
        elif (imgName == '24'):
            x, y, w, h = (118, 38, 796, 567)
        elif (imgName == '41'):
            x, y, w, h = (3, 2, 634, 422)
        elif (imgName == '44'):
            x, y, w, h = (59, 53, 390, 368)
        elif (imgName == '27'):
            x, y, w, h = (47, 15, 207, 171)
        elif (imgName == '31'):
            x, y, w, h = (49, 16, 206, 180)
        elif (imgName == '32'):
            x, y, w, h = (181, 169, 530, 527)
        elif (imgName == '35'):
            x, y, w, h = (15, 14, 299, 303)
        elif (imgName == '37'):
            x, y, w, h = (67, 110, 931, 889)
        elif (imgName == '38'):
            x, y, w, h = (21, 30, 976, 966)
        elif (imgName == '50'):
            x, y, w, h = (31, 28, 308, 304)
        elif (imgName == '51'):
            x, y, w, h = (1, 1, 399, 499)
        elif (imgName == '53'):
            x, y, w, h = (15, 11, 281, 284)
        elif (imgName == '54'):
            x, y, w, h = (10, 8, 471, 460)
        elif (imgName == '57'):
            x, y, w, h = (49, 98, 457, 416)
        elif (imgName == '58'):
            x, y, w, h = (37, 46, 358, 356)

        w = w - x
        h = h - y

        cv.rectangle(imgOrg, (x, y), (x + w, y + h), (66, 244, 104), 2)
        # cv.rectangle(img, (x, y), (x + w, y + h), Scalar(0, 255, 128), 2)
        if (savingType == 'csv-with-array-keys' or savingType == 'csv-with-object-name'):
            csvStr = "%s;%s;%s;%s;%s;%s;%s;%s\n" % (imgNamePath, w, h, objectType, x, y, x + w, y + h)
            if (savingType == 'csv-with-array-keys'):
                if (objectType == 'gauge'):
                    objectType = 0
                if (objectType == 'handwheel'):
                    objectType = 1
                if (objectType == 'valve'):
                    objectType = 2
                csvStr = "%s %s,%s,%s,%s,%s\n" % (imgNamePath, x, y, x + w, y + h, objectType)
            dataFiles[dataDir].write(csvStr)

        if (savingType == 'voc-xml'):
            if (int(imgName) <= 20):
                objectType = 'gauge'
            if (int(imgName) > 20 <= 40):
                objectType = 'valve'
            if (int(imgName) > 40):
                objectType = 'handwheel'
            xmlString = """ 
            <annotation>
                <folder>{objectType}</folder>
                <filename>{imgNamePath}</filename>
                <path>{imgNamePath}</path>
                <source>
                    <database>Unknown</database>
                </source>
                <size>
                    <width>{imgHeight}</width>
                    <height>{imgHeight}</height>
                    <depth>3</depth>
                </size>
                <segmented>0</segmented>
                <object>
                    <name>{objectType}</name>
                    <pose>Unspecified</pose>
                    <truncated>0</truncated>
                    <difficult>0</difficult>
                    <bndbox>
                        <xmin>{xmin}</xmin>
                        <ymin>{ymin}</ymin>
                        <xmax>{xmax}</xmax>
                        <ymax>{ymax}</ymax>
                    </bndbox>
                </object>
            </annotation>
            """.format(
                imgNamePath=imgName + '.jpg',
                xmin=x,
                ymin=y,
                xmax=x + w,
                ymax=y + h,
                objectType=objectType,
                imgHeight=imgHeight,
                imgWidth=imgWidth
            )
            path = dir_path + xmlFilePathPrefix + dataDir + '/' + objectType
            os.makedirs(path, exist_ok=True)
            file = open(path + '/' + imgName + '.xml', 'w')
            file.write(xmlString)
            file.close()

        if (savingType == 'Cartucho/mAP'):
            txtStr = "%s %s %s %s %s\n" % (objectType, x, y, x + w, y + h)
            file = open(dir_path + '/../github-repos/mAP/ground-truth/' + imgName + '.txt', 'w')
            file.write(txtStr)
            file.close()

        # break after first bounding box was found
        break

    # Show the image with a python window
    cv.imshow(imgName, imgOrg)

    # # Press any key to close the image
    cv.waitKey(0)
    #
    # # Clean up
    cv.destroyAllWindows()
    print('Verarbeitet: ' + ("%.2f" % (i / len(images) * 100) + '%'))
    i = i + 1

# filename,width,height,class,xmin,ymin,xmax,ymax
# tong-line-tong-torque.png,400,400,gauge,28,146,180,289

# https://github.com/qqwweee/keras-yolo3
# x_min,y_min,x_max,y_max,class_id

# [x,y,z,w]
# [0,1,2,3] Dimensionen


# ValueError: Dimension 0 in both shapes must be equal, but are 1 and 75. Shapes are
# [1,1,1024,39] and [75,1024,1,1]. for 'Assign_360' (op: 'Assign') with input shapes: [1,1,1024,39], [75,1024,1,1].
# (tensorflow1) Marlons-MacBook-Pro-2:keras-yolo3-mr mruescher$
