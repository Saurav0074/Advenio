import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('Image1.jpg')

# apply color-space change from BGR to l-a-e for detecting the atrophy class pixels
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# specifying lower and upper range of the colors to be considered
lower_limit = np.array([10, 10, 0])
upper_limit = np.array([185, 146, 255])

# threshold the lab image to consider only the atrophy class pixels
mask = cv2.inRange(lab, lower_limit, upper_limit)

# mask the above obtained region with the original image to treat rest regions as bg
res = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow('img', res)
k  = cv2.waitKey(0)

# apply color-space change from bgr to hls to detect the optic disc class
# repeat the above procedure
hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

lower_limit = np.array([0,115,0])
upper_limit = np.array([255,255,255])

# threshold the hls image
mask2 = cv2.inRange(hls, lower_limit, upper_limit)

# bitwise AND mask and original image
res1 = cv2.bitwise_and(img, img, mask = mask2)

cv2.imshow('img', res1)
k  = cv2.waitKey(0)

# extracting the reddish mark
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_limit = np.array([0,0,0])
upper_limit = np.array([12,240,255])

# threshold the hsv image
mask3 = cv2.inRange(hsv, lower_limit, upper_limit)

# bitwise XOR mask with original image
res2 = cv2.bitwise_xor(img, img, mask = mask3)

cv2.imshow('img', res2)
k  = cv2.waitKey(0)

# masking the original image with result of above masks to see the overall effect of both
mod1 = 255 - res1
final1 = mod1 * img

mod2 = 255 - res
final2 = mod2 * final1

mod3 = 255 - res2
final3 = mod3 * final2

mod4 = 254
final4 = mod4 * final3

cv2.imshow('image1', final4)
k = cv2.waitKey(0) 

################### Watershed algorithm ############################

gray = cv2.cvtColor(final3, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((4,4), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations = 1)

# sure background area
sure_bg = cv2.dilate(opening, kernel, iterations = 20)

# finding sure foreground area 
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret , sure_fg = cv2.threshold(dist_transform, 0.1* dist_transform.max(), 255, 0)

# finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Marker labelling
im2, contours, hierarcy = cv2.findContours(sure_fg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
ret, markers = cv2.connectedComponents(sure_fg)

# Adding one to all labels so that sure background is not 0, but 1
markers = markers+1

# Marking the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

# Using the jet color-map to show different colors
plt.imshow(markers, cmap = "hsv")
plt.show()
