import numpy as np
import matplotlib.pyplot as plt
from SimpleCurves import polar_to_cart

def archimedian_spiral(a=0,b=1,turns=1,draw=True,n=1001):
    th = np.linspace(0,2*turns*np.pi,n)
    
    r = a+(b*th)
    
    x,y = polar_to_cart(r,th)
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        
        plt.plot(x,y,color="CornflowerBlue",linewidth=2)

    
    return x,y

# Needs work on image
def hyperbolic_spiral(a=0,b=1,turns=1,draw=True,n=1001):
    th = np.linspace(0,2*turns*np.pi,n)
    
    r = a+(b/th)
    
    x,y = polar_to_cart(r,th)
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        
        plt.plot(x,y,color="CornflowerBlue",linewidth=2)

    
    return x,y

def fermat_spiral(a=0,b=1,turns=1,draw=True,n=1001):
    th = np.linspace(0,2*turns*np.pi,n)
    
    r = a+(b*th**.5)
    
    x,y = polar_to_cart(r,th)
    
    if draw == True:
        fig = plt.figure()
        fig.set_size_inches(10,10)
        plt.axes().set_aspect("equal","datalim")
        plt.axis("off")
        
        plt.plot(x,y,color="CornflowerBlue",linewidth=2)
        plt.plot(-x,-y,color="CornflowerBlue",linewidth=2)

    
    return x,y


if __name__ == '__main__':
    
    x,y = archimedian_spiral(turns=5)
#    x,y = hyperbolic_spiral(turns=2,n=101)
    x,y = fermat_spiral(turns=3)