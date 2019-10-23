import matplotlib.image
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import scipy.io
from pillow_lut import load_hald_image


a = matplotlib.image.imread("lena.bmp")
b = matplotlib.image.imread("jet.bmp")
c = ((a + b)/2)

plt.imshow(a,cmap='gray')
plt.show()
plt.imshow(b,cmap='gray')
plt.show()
plt.imshow(c,cmap='gray')
plt.show()