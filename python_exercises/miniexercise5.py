import cv2
#import  random
img =cv2.imread('EXERCISES/istockphoto-944837866-612x612.jpg',1)
#can be 0,1,-1:depends on the type like gre,coloured!!
#img =cv2.resize(img,(500,400))

#print(img),print(img.shape):opt=channels(3),width(2),height(1),bgr repesentation,

#changing border by assignng randomcolor
#for i in range(100):
#for  j in range(img.shape[1]):
#img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]

#copying a part of image towards the other parts
#tag=img[0:200,100:200]
#img[100:300,300:400]=tag
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
