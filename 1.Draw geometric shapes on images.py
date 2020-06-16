import cv2
import numpy as np
img=cv2.imread('Doraemon4.jpg',1)

img=cv2.line(img,(0,0),(200,200),(147,96,34),6)
img=cv2.arrowedLine(img,(230,40),(200,280),(188,90,156),4)
img=cv2.rectangle(img,(384,0),(510,78),(150,150,150),-1)
img=cv2.circle(img,(447,63),50,(240,200,230),-1)
font=cv2.FONT_HERSHEY_DUPLEX
img=cv2.putText(img,'OpenCv',(150,600),font,4,(255,0,0),2)

cv2.imshow('Image',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('Final.jpg',img)

