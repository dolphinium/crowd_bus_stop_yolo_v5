import cv2
import platform

if platform.system() == "Windows":
    pathway = ".\\"  # Windows
else:
    pathway = "./"  # Linux

img = cv2.imread(pathway + 'img.jpg')

print(img.shape)
height = img.shape[0]
width = img.shape[1]

# cut the image into 3 equal parts vertically
img1 = img[0:height, 0:int(width / 3)]
img2 = img[0:height, int(width / 3):int(2 * width / 3)]
img3 = img[0:height, int(2 * width / 3):width]

cv2.imshow('a', img1)
cv2.imwrite((pathway+'img1.jpg'), img1)
cv2.imshow('b', img2)
cv2.imwrite((pathway+'img2.jpg'), img2)
cv2.imshow('c', img3)
cv2.imwrite((pathway+'img3.jpg'), img3)

cv2.waitKey(0)

