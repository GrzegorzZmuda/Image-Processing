from PIL import Image
import cv2
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy import stats


a=Image.open('hist1.bmp')
a = np.array(a)
a= cv2.equalizeHist(a)
c=[plt.hist(a)[0]]
for i in range(len(plt.hist(a))-1):
    c.append(plt.hist(a)[i+1])


fig,axs = plt.subplots(3)
axs[0].imshow(a, cmap='gray')
axs[1].hist(a)
axs[2].plot(c)
plt.show()