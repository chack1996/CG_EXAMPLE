# it works on python 3
import scipy.ndimage
import numpy.linalg
import matplotlib.pyplot as plt

def imageCompress(k):
    image=scipy.ndimage.imread('dog.jpg',flatten=True)
    plt.imshow(image,cmap=plt.cm.gray)
    plt.ion()
    plt.show()
    U, s, V =numpy.linalg.svd(image)
    s10=numpy.diag(s[:k],0)
    u1=numpy.zeros((image.shape[0],k),float)
    u1[:,:]=U[:,:k]
    vt1=numpy.zeros((k,image.shape[1]),float)
    vt1[:,:]=V[:k,:]
    result=u1.dot(s10).dot(vt1)
    plt.imshow(result,cmap=plt.cm.gray)
    plt.ion()
    plt.show()



for k in range(11,0,-1):
    print(k,".......")
    imageCompress(k)
    temp=input()

