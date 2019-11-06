
from PIL import Image
import cv2
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
print(a)
a=bin(a,80)
axs[0].imshow(a, cmap='gray')
axs[1].hist(a)
print(a)
plt.show()