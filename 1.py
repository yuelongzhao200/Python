import numpy as np
import matplotlib.pyplot as plt
n=np.arange(0,15)
a=3.0/4
f=a**n
plt.subplot(221)
plt.title(u'a=3/4')
plt.stem(n,f)
a=5.0/4
f=a**n
plt.subplot(222)
plt.title(u'a=5/4')
plt.stem(n,f)
a=-3.0/4
f=a**n
plt.subplot(223)
plt.title(u'a=-3/4')
plt.stem(n,f)
a=-5.0/4
f=a**n
plt.subplot(224)
plt.title(u'a=-5/4')
plt.stem(n,f)
plt.show()

n=np.arange(0,32)
plt.ylim(-1,1)
plt.subplot(211)
plt.title(u'sin(npi/6)')
plt.stem(n,np.sin(n*np.pi/6))
plt.subplot(212)
plt.title(u'sin(5n)')
plt.stem(n,np.sin(5*n))
plt.show()

def dwxl(t):
    r=np.where(t==0.0,1.0,0.0)
    return r
n=np.arange(-4,8)
plt.ylim(0,2)
plt.stem(n,dwxl(n))
plt.show()

def dwjy(t):
    r=np.where(t>=0.0,1.0,0.0)
    return r
n=np.arange(-4,8)
plt.ylim(0,2)
plt.stem(n,dwjy(n))
plt.show()