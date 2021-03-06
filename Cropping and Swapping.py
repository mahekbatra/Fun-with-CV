#Import cv2 library
import cv2

#Load the images
image1=cv2.imread("Virat-Kohli-Anushka-Sharma.png")
image2=cv2.imread("Ranveer Deepika.png")

#Display the images
cv2.imshow("Image1",image1)
cv2.imshow("Image1",image2)
cv2.waitKey()
cv2.destroyAllWindows()

#Crop some part of the image
virat=image1[8:220,220:380]
ranveer=image2[8:220,200:360]
anushka=image1[6:220,430:610]
deepika=image2[6:220,360:540]

#Display all the cropped images
cv2.imshow("Virat",virat)
cv2.imshow("Ranveer",ranveer)
cv2.imshow("Anushka",anushka)
cv2.imshow("Deepika",deepika)
cv2.waitKey()
cv2.destroyAllWindows()

#Swap the cropped part of the images
image1[8:220,240:400]=ranveer
image1[6:220,430:610]=deepika

#display the final swapped image
cv2.imshow("Swap",image1)
cv2.imshow("Swap",image1)
cv2.waitKey()
cv2.destroyAllWindows()
