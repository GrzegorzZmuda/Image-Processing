from PIL import Image
import matplotlib.pyplot as plt
import scipy.io
def conv(a,b):
    fig, axs = plt.subplots(3)
    axs[0].plot(a)
    axs[1].imshow(b, cmap='gray')
    axs[2].imshow(b.point(a),cmap='gray')

    plt.show()
    c=b.point(a)
    return c


mat = scipy.io.loadmat('funkcjeLUT.mat')
print(mat.keys())
a=Image.open('lena.bmp')
conv(mat['odwlog'][0],a)
conv(mat['wykladnicza'][0],a)
conv(mat['kwadratowa'][0],a)
conv(mat['log'][0],a)
conv(mat['pila'][0],a)
conv(mat['odwrotna'][0],a)
conv(mat['pierwiastkowa'][0],a)
