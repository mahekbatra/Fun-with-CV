#Import cv2
import cv2

#Load the images 
pic1 = cv2.imread("Night.png")
pic2 = cv2.imread("Evening.jpg")

#Show the images
cv2.imshow("Image1",pic1)
cv2.imshow("Image1",pic2)
cv2.waitKey()
cv2.destroyAllWindows()

#Concat two images
pic = cv2.hconcat([pic1,pic2])

#Display the combined image
cv2.imshow("Image1",pic)
cv2.waitKey()
cv2.destroyAllWindows()
