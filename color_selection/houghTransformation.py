import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

image = mpimg.imread('exit-ramp.jpg')

gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
print("gray")
plt.imshow(gray)
plt.show()
kernel_size=5
blur_gray=cv2.GaussianBlur(gray,(kernel_size,kernel_size),0)
print("b_gray",blur_gray.size)
low_threshold = 50
hight_threshold = 150

edges = cv2.Canny(blur_gray,low_threshold,hight_threshold)
print("edges")
plt.imshow(edges)
plt.show()
mask = np.zeros_like(edges)
ignore_mask_color=255
print("mask1")
plt.imshow(mask,cmap='Greys_r')
plt.show()
imshape = image.shape
vertices = np.array([[(80,imshape[0]),(450, 290), (490, 290), (imshape[1],imshape[0])]], dtype=np.int32)
print("vertices",vertices)
cv2.fillPoly(mask,vertices,ignore_mask_color)
print("mask2")
plt.imshow(mask,cmap='Greys_r')
plt.show()
masked_edges = cv2.bitwise_and(edges,mask)
print("masked_edges",masked_edges.shape)
plt.imshow(masked_edges)
plt.show()
rho =2
theta = np.pi/180
threshold = 15
min_line_length =40
max_line_gap=20
line_image = np.copy(image)*0
print("line_image")
plt.imshow(line_image)
plt.show()
lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                            min_line_length, max_line_gap)
print("lines",lines.size)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

color_edges = np.dstack((edges, edges, edges))

lines_edges = cv2.addWeighted(color_edges, .0, line_image, 10, 10)
print("line_edges1")
plt.imshow(lines_edges)
plt.show()
print("line_edges2")
lines_edges = cv2.addWeighted(color_edges, .8, line_image, 10, 10)
plt.imshow(lines_edges)
plt.show()