from scipy import ndimage
# from scipy.misc import imread
from scipy.misc.pilutil import imread
from scipy.ndimage import (label,find_objects)
import scipy.ndimage.measurements as meas



# edge_horizont = ndimage.sobel(greyscale, 0)
# edge_vertical = ndimage.sobel(greyscale, 1)

# magnitude = np.hypot(edge_horizont, edge_vertical)

# from scipy import ndimage


img = imread('f.png')
x,y = label(img)

image_threshold = .5
label_array, n_features =  ndimage.label(x>image_threshold)
slices = meas.find_objects(label_array)
print(slices)

print(n_features)

# Plot the resulting shapes
import pylab as plt
plt.subplot(121)
plt.imshow(x)
plt.subplot(122)
plt.imshow(label_array)
plt.show()
