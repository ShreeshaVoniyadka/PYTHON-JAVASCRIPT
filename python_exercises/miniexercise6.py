import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    width=int(cap.get(3))# property of video
    height=int(cap.get(4))
    img=cv2.line(frame,(0,0),(width,height),(255,0,0),5)#:to draw a line in webcam
    #img =cv2.rectangle(img,(100,100),(200,200),(128,128,128),5)
    #img = np.zeros(frame.shape,np.uint8)#shaping a iamge with a blackscreen
    #img=cv2.circle(img,(200,200),(100),(134,0,75),-5)
    FONT=cv2.FONT_HERSHEY_COMPLEX
    img=cv2.putText(img,"myself shreesha",(0,185),FONT,1,(0,0,225),2,cv2.LINE_AA, False)
    #smaller_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    #image[:height//2,:width//2]=cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)#rotate a video
    #image[height//2:,:width//2]=cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)
    #image[:height//2,width//2:]=cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)
    #image[height//2:,width//2:]=cv2.rotate(smaller_frame,cv2.cv2.ROTATE_180)
    cv2.imshow('frame',frame)#frame fromline 5 is possible
    if  cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()