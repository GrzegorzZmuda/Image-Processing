from PIL import Image
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


a=Image.open('lena1.bmp')
b=Image.open('lena2.bmp')
c=Image.open('lena3.bmp')
d=Image.open('lena4.bmp')


fig,axs = plt.subplots(4,2)
axs[0,0].imshow(a, cmap='gray')
axs[0,1].hist(a)
axs[1,0].imshow(b, cmap='gray')
axs[1,1].hist(b)
axs[2,0].imshow(c, cmap='gray')
axs[2,1].hist(c)
axs[3,0].imshow(d, cmap='gray')
axs[3,1].hist(d)
plt.show()