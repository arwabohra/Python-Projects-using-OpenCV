import cv2
import datetime
cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('DateTime.avi',fourcc,20.0,(640,480))

while (cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        datet=str(datetime.datetime.now())
        text='WIDTH :' + str(cap.get(3)) + ' HEIGHT :' + str(cap.get(4))
        font=cv2.FONT_HERSHEY_SIMPLEX
        frame=cv2.putText(frame,text,(10,30),font,1,(0,255,0),1,cv2.LINE_AA)
        frame=cv2.putText(frame,datet,(10,650),font,1,(0,255,0),1,cv2.LINE_AA)

        cv2.imshow('Frame',frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else :
        break
cap.release()
out.release()
cv2.destroyAllWindows()

