import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import misc

image =misc.imread('test.jpg')
print ('this is image typw' , type(image),"\n this is image size",image.shape)

print(image.shape)
ysize=image.shape[0]
xsize=image.shape[1]
print("ysize",ysize)
print("XSIZE ",xsize)
color_size = np.copy(image)

red_threshold=200
green_threshold=200
blue_threshold=200
rgb_threshold = [red_threshold, green_threshold, blue_threshold]
print("rgb_threshold",rgb_threshold[0:3])

thresholds = (image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])
print("image[:,:,0]")
print(image[:,:,0])
print("image[:,:,0].shape",image[:,:,0].shape)
print("image[:,:,1]")
print(image[:,:,1])
print("image[:,:,1].shape",image[:,:,1].shape)
print("image[:,:,2]")
print(image[:,:,2])
print("image[:,:,2].shape",image[:,:,2].shape)


print("thresholds")
print(thresholds)

image[thresholds] = [0,0,0]

plt.imshow(image)
plt.show()
