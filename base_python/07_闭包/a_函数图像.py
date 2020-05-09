import math
import numpy as np

from matplotlib import pyplot as plt

a=np.arange(-100,100,0.0001)

b=[]


def sx(k):
    t1=math.sin(k)*k
    return t1



def plott(px):
    for k in a:
        if k!=0:
            temp1=px(k)
            b.append(temp1)
    
    
    
    plt.figure(figsize=(8,6))
    
    plt.plot(a,b)

plott(sx)