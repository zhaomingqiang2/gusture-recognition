import cv2
import os
import time



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


PATH = './ok'
imglist = modlist(PATH)
#print(imglist)
for imgpath in imglist:
    print(imgpath)
    



    img = cv2.imread(PATH+'/'+imgpath)

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
    ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) 
  
    _,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img,contours,-1,(0,0,255),3)
  
    #cv2.imshow(imgpath, _)
    saveROI('./glary/',imgpath,_)
    saveROI('./line/',imgpath,img)
    #cv2.waitKey(0)
