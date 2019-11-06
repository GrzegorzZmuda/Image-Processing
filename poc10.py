from PIL import Image
import cv2
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from scipy import stats
import scipy.io

toconv=Image.open('lenaRGB.bmp')
a = np.array(toconv)
p=a
fig, axs = plt.subplots(2,4)
axs[0,0].imshow(p)

tmpr=[]
tmpg=[]
tmpb=[]
res=[]

for i in range(len(a)):
    tmpr.append([])
    tmpg.append([])
    tmpb.append([])
    for j in range(len(a[i])):
        tmpr[i].append(a[i][j][0])
        tmpg[i].append(a[i][j][1])
        tmpb[i].append(a[i][j][2])


axs[0,1].hist(tmpr)
axs[0,2].hist(tmpg)
axs[0,3].hist(tmpb)
r= cv2.equalizeHist(np.array(tmpr))
g= cv2.equalizeHist(np.array(tmpg))
b= cv2.equalizeHist(np.array(tmpb))

for i in range(len(a)):
    res.append([])
    for j in range(len(a[i])):
        res[i].append([])
        res[i][j].append(r[i][j])
        res[i][j].append(g[i][j])
        res[i][j].append(b[i][j])



axs[1,1].hist(r)
axs[1,2].hist(g)
axs[1,3].hist(b)
axs[1,0].imshow(np.array(res))
plt.show()
