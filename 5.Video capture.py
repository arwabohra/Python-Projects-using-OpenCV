import cv2

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('Output.avi',fourcc,20.0,(640,480))
print(cap.isOpened())
while (cap.isOpened()):
    ret,frame=cap.read()

    ##print(cap.get(3))---640
    ##print(cap.get(4))---480

    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        out.write(frame)
        cv2.imshow('Frame',gray)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()