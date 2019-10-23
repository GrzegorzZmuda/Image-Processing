import matplotlib.image
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import scipy.io
from pillow_lut import load_hald_image


a = matplotlib.image.imread("lena.bmp")

c = 255 - a

plt.imshow(a,cmap='gray')
plt.show()
plt.imshow(c,cmap='gray')
plt.show()