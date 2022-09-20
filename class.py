import cv2
 
# load image and start video
watermark = cv2.imread("sammy.png")
yourVideo = cv2.VideoCapture("aquarium.mp4")

class FileName:
    name = ''

    def __init__(self,name):
        self.name = name

fileName = FileName('aquarium.mp4')

print(fileName.name)
