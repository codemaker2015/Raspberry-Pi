import urllib
import cv2
import numpy as np

url="http://192.168.1.29:8080/shot.jpg"
while True:
    
    imgPath=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow("frame",img)
    if ord('q') ==  cv2.waitKey(10):
        exit(0)
