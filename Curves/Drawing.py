import matplotlib.pyplot as plt
from Conversions import complex_to_xy, points_to_xy





def make_blank_canvas(xrange=None,yrange=None,size=[12,12]):
    fig = plt.figure()
    fig.set_size_inches(size[0],size[1])
    # If no coordinate range is given fit everything into a square
    if not xrange and not yrange:
        ax = plt.axes()
        ax.set_aspect("equal","datalim")
    # If only xrange is given fit a square
    elif not yrange:
        ax = plt.axes(xlim=xrange,ylim=xrange)
    # If both are given fix the rectangle
    else:
        ax = plt.axes(xlim=xrange,ylim=yrange)
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])
    
    return fig,ax

    
def mbline(M,B,xlim=[-5,5],ylim=[-5,5],**kwargs):
    
    def calc_y(m,x,b):
        return m*x+b

    def calc_x(m,y,b):
        return (y-b)/m
    
    x_lo = xlim[0]
    y_lo = ylim[0]
    
    x_hi = xlim[1]
    y_hi = ylim[1]
    
    for m,b in zip(M,B):
        
        x0 = x_lo
        y0 = calc_y(m,x_lo,b)
        
        if y0 < y_lo:
            x0 = calc_x(m,y_lo,b)
            y0 = y_lo
        elif y0 > y_hi:
            x0 = calc_x(m,y_hi,b)
            y0 = y_hi
                
        x1 = x_hi
        y1 = calc_y(m,x_hi,b)
        if y1 > y_hi:
            x1 = calc_x(m,y_hi,b)
            y1 = y_hi
        elif y1 < y_lo:
            x1 = calc_x(m,y_lo,b)
            y1 = y_lo

        plt.plot([x0,x1],[y0,y1],**kwargs)
    
    return [[x0,y0],[x1,y1]]


# Draw a curve from:
#   seperate lists of x and y coordinates
#   a list of (x,y) points
#   a list of complex numbers
def draw_curve_xy(x,y,**kwargs):
    plt.plot(x,y,**kwargs)

def draw_curve_points(P,**kwargs):
    x,y = points_to_xy(P)
    plt.plot(x,y,**kwargs)

def draw_curve_complex(C,**kwargs):
    x,y = complex_to_xy(C)
    plt.plot(x,y,**kwargs)
    

# Draw a curve that attaches the start to the end from:
#   seperate lists of x and y coordinates
#   a list of (x,y) points
#   a list of complex numbers
def draw_closed_curve_xy(x,y,**kwargs):
    # Convert to list because an np.array doesn't play nice
    X = list(x) + [x[0]]
    Y = list(y) + [y[0]]
    plt.plot(X,Y,**kwargs)
    
def draw_closed_curve_points(P,**kwargs):
    x,y = points_to_xy(P)
    draw_closed_curve_xy(x,y,**kwargs)
    
def draw_closed_curve_complex(P,**kwargs):
    x,y = complex_to_xy(P)
    draw_closed_curve_xy(x,y,**kwargs)
    

# Draw scatterplot from:
#   seperate lists of x and y coordinates
#   a list of (x,y) points
#   a list of complex numbers
def draw_dots_xy(x,y,**kwargs):
    plt.scatter(x,y,**kwargs)

def draw_dots_points(P,**kwargs):
    x,y = points_to_xy(P)
    plt.scatter(x,y,**kwargs)

def draw_dots_complex(C,**kwargs):
    x,y = complex_to_xy(C)
    plt.scatter(x,y,**kwargs)





if __name__ == '__main__':
    
    make_blank_canvas([-5,5],[-5,5])
    draw_curve_xy([1,2,3],[0,1,0])
    
    make_blank_canvas([-5,5],[-5,5])
    draw_closed_curve_xy([1,2,3],[0,1,0])