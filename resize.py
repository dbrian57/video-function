from email.mime import image
import cv2
import numpy as np
 
# load image and start video
foreground = cv2.imread("sammy.png", cv2.IMREAD_UNCHANGED)
cap = cv2.VideoCapture("aquarium.mp4")

imageWidth = foreground.shape[1]
imageHeight = foreground.shape[0]
vidWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH )
vidHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT )
fps =  cap.get(cv2.CAP_PROP_FPS)

scaleWidth = int(vidWidth * 0.2)
scaleHeight = int((scaleWidth / imageWidth) * imageHeight)

scaleDown = (scaleWidth, scaleHeight)
print(scaleDown)

resized = cv2.resize(foreground, scaleDown, interpolation=cv2.INTER_AREA)

cv2.imwrite("saved.png", resized)