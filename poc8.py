

from PIL import Image
import cv2
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy import stats
import scipy.io

def conv(a,b):
    fig, axs = plt.subplots(3)
    axs[0].plot(a)
    axs[1].imshow(b, cmap='gray')
    axs[2].imshow(b.point(a),cmap='gray')

    plt.show()
    c=b.point(a)
    return c



toconv=Image.open('hist1.bmp')
a = np.array(toconv)
b= cv2.equalizeHist(a)

res=stats.cumfreq(a,256)
x = res.lowerlimit + np.linspace(0, res.binsize*res.cumcount.size,res.cumcount.size)

lut=[]
for i in range(256):
    tmp=(i*max(x)/x[i])

    lut.append(tmp)


lm=min(lut)



my=conv(lut,toconv)
print(lut)
res1=stats.cumfreq(b,256)
y = res1.lowerlimit + np.linspace(0, res1.binsize*res1.cumcount.size,res1.cumcount.size)

res2=stats.cumfreq(my,256)
z = res2.lowerlimit + np.linspace(0, res2.binsize*res1.cumcount.size,res2.cumcount.size)

fig,axs = plt.subplots(3,3)
axs[0,0].imshow(a, cmap='gray')
axs[1,0].hist(a)
axs[2,0].bar(x, res.cumcount, width=res.binsize)
axs[0,1].imshow(b, cmap='gray')
axs[1,1].hist(b)
axs[2,1].bar(y, res1.cumcount, width=res1.binsize)
axs[0,2].imshow(my, cmap='gray')
axs[1,2].hist(my)
axs[2,2].bar(z, res2.cumcount, width=res2.binsize)
plt.show()