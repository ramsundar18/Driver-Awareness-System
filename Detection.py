import cv2
import numpy as np

img1 = cv2.imread('Imagequery/20 speed limit.jpg')
img2 = cv2.imread('Imagetrain/speed limit is 20 please maintain your speed.jpg')
img3 = cv2.imread('Imagequery/50 speed limit.jpg')
img4 = cv2.imread('Imagetrain/speed limit is 50 please maintain your speed.jpg')
img5 = cv2.imread('Imagequery/90 speed limit.jpg')
img6 = cv2.imread('Imagetrain/speed limit is 90 maintain your speed.jpg')
img7 = cv2.imread('Imagequery/stop.jpg')
img8 = cv2.imread('Imagetrain/stop sign ahead.jpg')

orb = cv2.ORB_create()

kp1 , des1 = orb.detectAndCompute(img1,None)
kp2 , des2 = orb.detectAndCompute(img2,None)
kp3 , des3 = orb.detectAndCompute(img3,None)
kp4 , des4 = orb.detectAndCompute(img4,None)
kp5 , des5 = orb.detectAndCompute(img5,None)
kp6 , des6 = orb.detectAndCompute(img6,None)
kp7 , des7 = orb.detectAndCompute(img7,None)
kp8 , des8 = orb.detectAndCompute(img8,None)



bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)
matches = bf.knnMatch(des3,des4,k=2)
matches = bf.knnMatch(des5,des6,k=2)
matches = bf.knnMatch(des7,des8,k=2)

good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

img9 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
img10 = cv2.drawMatchesKnn(img3,kp3,img4,kp4,good,None,flags=2)
img11 = cv2.drawMatchesKnn(img5,kp5,img6,kp6,good,None,flags=2)
img12 = cv2.drawMatchesKnn(img7,kp7,img8,kp8,good,None,flags=2)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('img3',img3)
cv2.imshow('img4',img4)
cv2.imshow('img5',img5)
cv2.imshow('img6',img6)
cv2.imshow('img7',img7)
cv2.imshow('img8',img8)
cv2.waitKey(0)
