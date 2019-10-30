from PIL import Image
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import cv2
import scipy.io







a=Image.open('phobos.bmp')
mat = scipy.io.loadmat('histogramZadany.mat')
tmp=mat['histogramZadany'][0]







fig,axs = plt.subplots(2)
axs[0].imshow(a, cmap='gray')
axs[1].imshow(b, cmap='gray')
plt.show()