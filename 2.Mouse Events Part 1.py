import cv2
import numpy as np

##events= [i for i in dir(cv2) if 'EVENT' in i]
##print(events)
##print(len(events))

def click_event(event,x,y,index,params):
    if event==cv2.EVENT_FLAG_LBUTTON:
        print(x,y)
        font=cv2.FONT_HERSHEY_DUPLEX
        strXY=str(x) + ' ' + str(y)
        cv2.putText(img,strXY,(x,y),font,0.5,(255,255,0),1)
        cv2.imshow('Image',img)
    if event==cv2.EVENT_FLAG_RBUTTON:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        strBGR = str(blue) + ' ' + str(green) + ' ' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 0), 1)
        cv2.imshow('Image', img)

img=cv2.imread('Doraemon1.jpg')
cv2.imshow('Image',img)

cv2.setMouseCallback('Image',click_event)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Mouse.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()