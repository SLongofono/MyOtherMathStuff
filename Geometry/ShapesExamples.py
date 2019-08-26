from Shapes import Circle, Ellipse
from SuperEllipse import SuperEllipse
from Utils.Drawing import make_canvas, plot_points, scatter_points
from AffineTransforms import rotate, reflect_y
import numpy as np


c = Circle(2)
make_canvas([-3,3],size=5)
plot_points(c.points())
scatter_points([c.pos])


e = Ellipse(2.5,2)
E = e.points()
E += e.foci()
E = np.asarray(E)


P = reflect_y(rotate(E,1))
make_canvas([-3,3],size=4)
plot_points(P[:-2])
scatter_points(P[100:101],color='orange')
scatter_points(P[101:102],color='green')

A = SuperEllipse(a=2,b=2)
for i in [.4,.8,1.2,1.6,2,2.4]:
    make_canvas([-3,3],size=4)
    A.n = i
    A.draw()