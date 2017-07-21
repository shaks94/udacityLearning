import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.misc as misc

image = misc.imread("test.jpg")
print("image\n",image)
print("image.size",image.size)
print("imageType",type(image))
ysize = image.shape[0]
xsize = image.shape[1]

region_select = np.copy(image)

left_bottom = [0, 539]
right_bottom = [900, 300]
apex = [400, 0]

fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)

print("fit_left")
print(fit_left)
print("fit_right")
print(fit_right)
print("fit_bottom")
print(fit_bottom)

XX, YY = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
print("XX")
print(XX)
print("YY")
print(YY.shape)
print(YY)
region_thresholds = (YY > (XX*fit_left[0] + fit_left[1])) & \
                    (YY > (XX*fit_right[0] + fit_right[1])) & \
                    (YY < (XX*fit_bottom[0] + fit_bottom[1]))
print("(XX*fit_left[0] + fit_left[1])")
print((XX*fit_left[0] + fit_left[1]))
print("region_thresholds")
print(region_thresholds)