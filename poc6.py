
import matplotlib.image
import matplotlib.pyplot as plt

from PIL import Image, ImageMath
import numpy as np
import scipy.io
from pillow_lut import load_hald_image


c =Image.open('lena.bmp')
d = Image.open('kolo.bmp')

out = ImageMath.eval("convert(min(a, b), 'L')", a=c, b=d)
plt.imshow(c,cmap='gray')
plt.show()
plt.imshow(d,cmap='gray')
plt.show()
plt.imshow(out,cmap='gray')
plt.show()


out = ImageMath.eval("convert( max(a, b), 'L')", a=c, b=d)

plt.imshow(out,cmap='gray')
plt.show()