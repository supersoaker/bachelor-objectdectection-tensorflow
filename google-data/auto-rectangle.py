import numpy as np
import cv2
import glob
import imutils
import re
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--savingType', default='voc-xml',
                    choices=['voc-xml', 'csv-with-array-keys', 'csv-with-object-name', 'Cartucho/mAP'],
                    help='saving type of the bounding boxes (default: %(default)s)')
parser.add_argument('--xmlPath', default='/../data/', help='path where the xmls will be saved (default: %(default)s)')
parser.add_argument('--imageModifyLevel', default='0',
                    help='how much the images will be modified (default: %(default)s)')
parser.add_argument('--imagePath', default='/../data/_main/*/*.jpg',
                    help='relative glob path to the image directory (default: %(default)s)')
parser.add_argument('--showImage', default='false',
                    help='should the image be shown after each iteration (default: %(default)s)')

args = parser.parse_args()
savingType = args.savingType
xmlFilePathPrefix = args.xmlPath
imageModifyLevel = args.imageModifyLevel
imagePath = args.imagePath

# Read image data
dir_path = os.path.dirname(os.path.realpath(__file__))
images = sorted(glob.glob(dir_path + imagePath))
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
    img = cv2.imread(imgNamePath)

    imgNamePath = imgNamePath.replace(dir_path + '/', '', 1)

    regex = r"^../data/_main/(.*?)(/)(.*)\.jpg$"

    dataDir = re.findall(regex, imgNamePath)[0][0]
    objectType = re.findall(regex, imgNamePath)[0][1]
    imgName = re.findall(regex, imgNamePath)[0][2]

    # Adding white border, because some images are to big
    # img = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[255, 255, 255])

    imgOrg = img.copy()
    imgOrg2 = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    img = cv2.Canny(gray, 30, 200)
    # ret, img = cv2.threshold(img, 60, 255, cv2.THRESH_BINARY_INV)
    ret, img = cv2.threshold(img, 0, 255, 0)

    ## sort the containers
    img = cv2.convertScaleAbs(img)
    ctrs = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    ctrs = imutils.grab_contours(ctrs)
    ctrs = sorted(ctrs, key=cv2.contourArea, reverse=True)[:10]

    imgHeight, imgWidth = img.shape

    if (imageModifyLevel == '2'):
        img = cv2.cvtColor(imgOrg, cv2.COLOR_BGR2RGB)
        lower_white = np.array([245, 245, 245], dtype=np.uint8)
        upper_white = np.array([255, 255, 255], dtype=np.uint8)
        mask = cv2.inRange(img, lower_white, upper_white)  # could also use threshold
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (
            3, 3)))  # "erase" the small white points in the resulting mask
        mask = cv2.bitwise_not(mask)  # invert mask

        # load background (could be an image too)
        bk = np.full(img.shape, (66, 128, 200), dtype=np.uint8)  # white bk
        # bk = cv2.imread('/Users/mruescher/Desktop/MarlonR.jpg')
        # bk = cv2.resize(bk, (imgWidth, imgHeight))

        # get masked foreground
        fg_masked = cv2.bitwise_and(img, img, mask=mask)


        # fg_masked = np.zeros((400, 400, 3), dtype="uint8")
        # fg_masked[np.where((fg_masked == [0,0,0]).all(axis=2))] = [66, 244, 104]

        # cv2.imshow(imgName, fg_masked)
        # get masked background, mask must be inverted
        mask = cv2.bitwise_not(mask)
        bk_masked = cv2.bitwise_and(bk, bk, mask=mask)
        # cv2.imshow(imgName, bk_masked)

        # combine masked foreground and masked background
        imgOrg = cv2.bitwise_or(fg_masked, bk_masked)
        mask = cv2.bitwise_not(mask)  # revert mask to original
        # cv2.imshow(imgName, final)

    # Foreach container found
    for cnt in ctrs:
        x, y, w, h = cv2.boundingRect(cnt)
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

        cv2.rectangle(imgOrg, (x, y), (x + w, y + h), (66, 244, 104), 2)
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
            xmlString = """<annotation>
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
            path = dir_path + xmlFilePathPrefix + dataDir + '/'
            print(path)
            cv2.imwrite(path + '/' + imgName + '.jpg', imgOrg)
            os.makedirs(path, exist_ok=True)
            file = open(path + '/' + imgName + '.xml', 'w')
            file.write(xmlString)
            file.close()

        if (savingType == 'Cartucho/mAP'):
            if (int(imgName) <= 20):
                objectType = 'gauge'
            if (int(imgName) > 20 <= 40):
                objectType = 'valve'
            if (int(imgName) > 40):
                objectType = 'handwheel'
            txtStr = "%s %s %s %s %s\n" % (objectType, x, y, x + w, y + h)
            path = dir_path + xmlFilePathPrefix + dataDir + '/'
            file = open(path + '/' + imgName + '.txt', 'w')
            # file = open(dir_path + '/../github-repos/mAP/ground-truth/' + imgName + '.txt', 'w')
            file.write(txtStr)
            file.close()

        # break after first bounding box was found
        break

    # Show the image with a python window
    if(args.showImage == 'true'):
        cv2.imshow(imgName, imgOrg)
        # Press any key to close the image
        cv2.waitKey(0)
        # Clean up
        cv2.destroyAllWindows()

    #
    print('Verarbeitet: ' + ("%.2f" % (i / len(images) * 100) + '%'))
    i = i + 1
