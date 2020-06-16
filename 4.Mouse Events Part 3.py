import cv2
import numpy as np

def click_event(event,x,y,index,params):
    if event==cv2.EVENT_FLAG_LBUTTON:
        blue=img[x,y,0]
        green=img[x,y,1]
        red=img[x,y,2]
        ##cv2.circle(img,(x,y),5,(0,0,255),-1)
        myColorImage=np.zeros((512,512,3),np.uint8)

        myColorImage[:]=[blue,green,red]
        cv2.imshow('Color',myColorImage)

img=cv2.imread('Doraemon4.jpg')
cv2.imshow('Image',img)

cv2.setMouseCallback('Image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
