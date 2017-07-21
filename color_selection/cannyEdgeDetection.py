import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from scipy import misc
image = mpimg.imread("exit-ramp.jpg")
plt.imshow(image)
plt.show()
import cv2
gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
plt.imshow(gray,cmap='gray')
plt.show()
kernel_size=3
blur_gray=cv2.GaussianBlur(gray,(kernel_size,kernel_size),0)
low_threshold=50
high_threshold=150
edges=cv2.Canny(blur_gray,low_threshold,high_threshold)
plt.imshow(edges,cmap='Greys_r')
plt.show()
