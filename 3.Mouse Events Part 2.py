import cv2
import numpy as np

def click_event(event,x,y,index,params):
    if event==cv2.EVENT_FLAG_LBUTTON:
        cv2.circle(img,(x,y),5,(0,255,255),-1)
        point.append((x,y))
        if len(point) >=2:
            cv2.line(img,point[-1],point[-2],(255,255,255),2)
        cv2.imshow('Image',img)

img = cv2.imread('black1.jpg')
cv2.imshow('Image', img)

cv2.setMouseCallback('Image', click_event)
point=[]

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Mouse.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
