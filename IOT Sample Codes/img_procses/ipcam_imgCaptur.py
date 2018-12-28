import urllib
import cv2
import numpy as np

url="http://192.168.43.1:8080/shot.jpg"
num = 10
while True:
    
    imgPath=urllib.urlopen(url)
    imgNp=np.array(bytearray(imgPath.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    cv2.imshow("frame",img)
    if (cv2.waitKey(1) == ord('q')):
        num = num - 1
        cv2.imwrite("database/first."+str(num)+".jpg",img)

cv2.destroyAllWindows()
