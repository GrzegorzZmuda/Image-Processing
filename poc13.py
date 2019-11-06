
from PIL import Image
import cv2 as cv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from scipy import stats
import scipy.io
fig, axs = plt.subplots(2)
toconv=Image.open('coins.png')

def bin(a,b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]<b:
                a[i][j]=0

    return a

a = np.array(toconv)

ret2,th2 = cv.threshold(a,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
axs[0].imshow(th2, cmap='gray')
axs[1].hist(th2.ravel(),255,[0,255])

plt.show()