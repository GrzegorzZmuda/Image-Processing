
from PIL import Image
import cv2
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from scipy import stats
import scipy.io
fig, axs = plt.subplots(2,4)
toconv=Image.open('figura.png')



a = np.array(toconv)

toconv=Image.open('figura2.png')

b = np.array(toconv)

toconv=Image.open('figura3.png')
c=np.array(toconv)

toconv=Image.open('figura4.png')
d=np.array(toconv)

axs[0,0].imshow(a, cmap='gray')
axs[1,0].hist(a.ravel(),256,[0,255])
axs[0,1].imshow(b, cmap='gray')
axs[1,1].hist(b.ravel(),255,[0,255])
axs[0,2].imshow(c, cmap='gray')
axs[1,2].hist(c.ravel(),255,[0,255])
axs[0,3].imshow(d, cmap='gray')
axs[1,3].hist(d.ravel(),255,[0,255])


plt.show()

