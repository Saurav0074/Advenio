import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('Image1.jpg')
#filtered = cv2.pyrMeanShiftFiltering(img, 21, 51)
# gray without filter is better
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.imshow(gray)
plt.show()


#edges = cv2.Canny(lap, 100, 200)
#plt.imshow(edges, cmap = "jet")
#plt.show()

#blur = cv2.GaussianBlur(gray, (5, 5), 0)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#edges = cv2.Canny(thresh, 100, 200)
plt.imshow(thresh)
plt.show()


#plt.imshow(thresh, 'gray')
#plt.show()

# noise removal
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations = 2)

# sure background area
sure_bg = cv2.dilate(opening, kernel, iterations = 3)

# finding sure foreground area 
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret , sure_fg = cv2.threshold(dist_transform, 0.6* dist_transform.max(), 255, 0)

# finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)


#plt.imshow(sure_fg, 'gray')
#plt.show()

# Marker labelling
im2, contours, hierarcy = cv2.findContours(sure_fg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
ret, markers = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

plt.imshow(markers, cmap = "jet")
plt.show()