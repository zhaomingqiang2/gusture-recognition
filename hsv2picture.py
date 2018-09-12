import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
import time
################################################################################


#列出目录下文件列表
def modlist(path):
    # 列出path里面所有文件信息
    listing = os.listdir(path)
    retlist = []
    for name in listing:
        #print("name......=",name)
        if name.startswith('.'):
            continue
        retlist.append(name)
    return retlist


#保存img文件
def saveROI(path,imgname,img):
    
    print(path+imgname+'.png')
    cv2.imwrite(path+imgname, img) # 写入文件
    print("Saving img: ", imgname)
    time.sleep(0.05)
    

def hsvpicture(ImagePath):
    imgFile = ImagePath

    # load an original image
    img = cv2.imread(imgFile)
    ################################################################################


    #img = cv2.GaussianBlur(img, (5, 5), 2) # 高斯模糊，给出高斯模糊矩阵和标准差
    rows,cols,channels = img.shape

    # convert color space from bgr to rgb                        
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # prepare an empty image space
    imgSkin = np.zeros(img.shape, np.uint8)
    # copy original image
    imgSkin = img.copy()                       

    # convert color space from rgb to hsv
    imgHsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

    for r in range(rows):
        for c in range(cols):
     
            # get values of hue, saturation and value
            # standard -- h range: [0,360]; s range: [0,1]; v range: [0,255]
            # opencv -- h range: [0,180]; s range: [0,255]; v range: [0,255]       
            H = imgHsv.item(r,c,0)
            S = imgHsv.item(r,c,1)
            V = imgHsv.item(r,c,2)
            
            # non-skin area if skin equals 0, skin area otherwise        
            skin = 0
                    
            if ((H >= 0) and (H <= 25 / 2)) or ((H >= 335 / 2) and (H <= 360 / 2)):
                if ((S >= 0.2 * 255) and (S <= 0.6 * 255)) and (V >= 0.4 * 255):
                    skin = 1
                    # print 'Skin detected!'
            
            if 0 == skin:
                imgSkin.itemset((r,c,0),0)
                imgSkin.itemset((r,c,1),0)                
                imgSkin.itemset((r,c,2),0)

    # display original image and skin image
    #plt.subplot(1,2,1), plt.imshow(img), plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    #plt.subplot(1,2,2), plt.imshow(imgSkin), plt.title('HSV Skin Image'), plt.xticks([]), plt.yticks([])
    #plt.show()
    return imgSkin
    ################################################################################


PATH = './five'
imglist = modlist(PATH)
for imgpath in imglist:
    saveROI('./hsvfive/',imgpath,hsvpicture(PATH+'/'+imgpath))
    



