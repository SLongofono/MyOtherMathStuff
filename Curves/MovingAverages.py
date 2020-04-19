import numpy as np
from Drawing import make_blank_canvas
from KernelFunctions import triangular_kernel

# Simple moving average of equally spaced data
def simple_moving_average(X,Y,width=1):
    
    # Number of values considered at each step
    N = 2*width+1
    
    # Padded version of Y
    y = Y[:]
    y = [y[0]]*width + y + [y[-1]]*width

    m_av = []
    for i in range(len(Y)):
        m_av.append(sum(y[i:N+i])/N)
    
    return m_av


def weighted_mean(X,W):

    s = sum([x*w for x,w in zip(X,W)])
    n = sum(W)
    
    return s/n
        
    
def weighted_moving_average(X,Y,width=1,weights=[]):
    
    # Number of values considered at each step
    N = 2*width+1
    
    # Padded version of Y
    y = Y[:]
    y = [y[0]]*width + y + [y[-1]]*width
    
    if not weights:
        weights = [triangular_kernel(u) for u in np.linspace(-1,1,N)]
    elif len(weights) == N:
        raise Exception("Invalid weights")
        
    
    m_av = []
    for i in range(len(Y)):
        m_av.append(weighted_mean(y[i:N+i],weights))
    
    return m_av


def simple_moving_median(X,Y,width=1):
    
    # Number of values considered at each step
    N = 2*width+1
    
    # Padded version of Y
    y = Y[:]
    y = [y[0]]*width + y + [y[-1]]*width

    m_av = []
    for i in range(len(Y)):
        m_av.append(np.median(y[i:N+i]))
    
    return m_av
    
    
    
    
if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    
    x1 = np.linspace(0,7,200)
    y1 = list(np.cos(x1)+np.random.normal(0,.3,200))
    
    av1 = simple_moving_average(x1,y1,10)
    av2 = weighted_moving_average(x1,y1,10)
    av3 = simple_moving_median(x1,y1,10)
    
    make_blank_canvas(size=(14,14))
    
    ax = plt.subplot(2,2,1)
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.scatter(x1,y1,color="lightgray")
    plt.plot(x1,av1)
    plt.title("Simple Moving Average",size=16)
    
    ax = plt.subplot(2,2,2)
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.scatter(x1,y1,color="lightgray")
    plt.plot(x1,av2)
    plt.title("Triangular Weighted Moving Average",size=16)

    ax = plt.subplot(2,2,3)
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.scatter(x1,y1,color="lightgray")
    plt.plot(x1,av3)
    plt.title("Moving Median",size=16)