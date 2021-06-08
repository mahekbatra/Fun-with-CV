#Import numpy and cv2 library
import cv2
import numpy as np

#Create an image
photo = np.zeros((800,1200,3))
photo[:,:]=[255,255,255]

#Sky
cv2.rectangle(photo,(0,0),(1200,550),(255,191,0),-1)

#cloud
cv2.circle(photo,(80,100),50,(255,255,255),-1)
cv2.circle(photo,(110,80),50,(255,255,255),-1)
cv2.circle(photo,(140,80),50,(255,255,255),-1)
cv2.circle(photo,(170,100),50,(255,255,255),-1)
cv2.circle(photo,(120,120),50,(255,255,255),-1)

#building
cv2.rectangle(photo,(730,150),(950,550),(255,0,255),-1)
cv2.circle(photo,(840,550),90,(255,255,255),-1)

cv2.rectangle(photo,(770,200),(820,250),(0,0,0),-1)
cv2.rectangle(photo,(770,270),(820,320),(0,0,0),-1)
cv2.rectangle(photo,(770,340),(820,390),(0,0,0),-1)

cv2.rectangle(photo,(850,200),(900,250),(0,0,0),-1)
cv2.rectangle(photo,(850,270),(900,320),(0,0,0),-1)
cv2.rectangle(photo,(850,340),(900,390),(0,0,0),-1)

#Road
cv2.rectangle(photo,(0,550),(1200,800),(0,0,0),-1)
cv2.rectangle(photo,(150,660),(300,700),(255,255,255),-1)
cv2.rectangle(photo,(400,660),(550,700),(255,255,255),-1)
cv2.rectangle(photo,(650,660),(800,700),(255,255,255),-1)
cv2.rectangle(photo,(900,660),(1050,700),(255,255,255),-1)


#House
cv2.rectangle(photo,(120,350),(370,550),(255,0,0),-1)
cv2.rectangle(photo,(210,425),(290,550),(0,0,255),-1)
cv2.rectangle(photo,(230,475),(270,550),(0,0,0),-1)
cv2.rectangle(photo,(145,350),(170,550),(0,255,255),-1)
cv2.rectangle(photo,(325,350),(350,550),(0,255,255),-1)
pts=np.array([[90,350],[120,250],[370,250],[400,350]])
pts = pts.reshape((-1,1,2))
cv2.fillPoly(photo,[pts],(255,0,0))

#Tree1
cv2.rectangle(photo,(520,300),(580,550),(0,0,255),-1)
cv2.circle(photo,(550,210),100,(0,255,0),-1)

#Tree2
cv2.rectangle(photo,(1060,250),(1120,550),(0,0,255),-1)
pts=np.array([[1020,300],[1090,100],[1170,300]])
pts = pts.reshape((-1,1,2))
cv2.fillPoly(photo,[pts],(0,255,0))


#Display an image
cv2.imshow('Image',photo)
cv2.waitKey()
cv2.destroyAllWindows()
