import cv2
import numpy as np
import os
import imutils
from imutils import paths

pathToimages = r'C:\Users\DELL\Desktop\programming\computerVision\dataset\blur_images'
imagePaths = list(paths.list_images(pathToimages))
for imagePath in imagePaths:
    imageName = imagePath.split(os.path.sep)[-1].split('.')[0]
    img = cv2.imread(imagePath)
    origImg = imutils.resize(img, 600)
    blurImg = cv2.GaussianBlur(origImg, (7,7), 2)
    shapened2 = cv2.addWeighted(origImg, 4.0, blurImg, -3.0, 0)

    cv2.imshow("shapened2", shapened2)
    cv2.imshow("original", origImg)
    cv2.waitKey(0)

    storePath = os.path.join(pathToimages,'new')
    if not os.path.exists(storePath):
        os.mkdir(storePath)
    os.chdir(storePath)
    fileName = f'{storePath}/{imageName}nonoise'
    cv2.imwrite(fileName+".jpg", shapened2)