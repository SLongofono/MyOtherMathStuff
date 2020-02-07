from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Image, Spacer
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.shapes import Drawing
from math import sqrt, sin, cos, exp
from matplotlib import pyplot as plt

def ballistic_motion(V0,th,y0,g,m,A,Cd,rho,dt):

    if y0 < 0:
        raise Exception("y0 must be non-negative")
    
    Vt = sqrt((2*m*g)/(rho*A*Cd))
    t = 0
    
    x, y = [0], [y0]
    tof = 0
    while True:
        t += dt
        d = (1-exp(-g*t/Vt))
        x.append(((V0*Vt*cos(th))/g)*d)
        y.append(y0+(Vt/g)*(V0*sin(th)+Vt)*d-(Vt*t))
        tof += dt
        if y[-1] < 0:
            y[-1] = 0
            break
        
    
    
    return {"V0" : V0,
            "th" : th,
            "y0" : y0,
            "g" : g,
            "m" : m,
            "A" : A,
            "Cd" : Cd,
            "rho" : rho,
            "Vt" : Vt,
            "dt" : dt,
            "tof" : tof}, x, y


def ballistic_tables(D,x,y):
    
    #Initial Conditions
    A = [[f"Initial Speed:     {round(D['V0'],3)}m/s"],
         [f"Angle of Release:  {round(D['th'],3)}"],
         [f"Initial Height:    {round(D['y0'],3)}m"]]
    
    conditions = Table(A,
            style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                   ("FONTNAME",(0,0),(-1,-1),"Courier")])

    B = [[f"Projectile Mass:   {round(D['m'],3)}kg"],
         [f"Cross Section:     {round(D['A'],3)}m^2"],
         [f"Drag Coefficient:  {round(D['Cd'],3)}"],
         [f"Terminal Velocity: {round(D['Vt'],3)}m/s"]]
    
    # Object properties
    props = Table(B,
            style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                   ("FONTNAME",(0,0),(-1,-1),"Courier")])

    
    #Environmental conditions
    C = [[f"Gravitation:       {-round(D['g'],3)}m/s^2"],
         [f"Air Density:       {round(D['rho'],3)}"]]
    
    environs = Table(C,
            style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                   ("FONTNAME",(0,0),(-1,-1),"Courier")])
    
    # Outcomes
    d = sqrt(abs(x[-1]-x[-2])**2 + abs(y[-1]-y[-2])**2)
    outcomes = [[f"Final Distance:    {round(x[-1],3)}"],
                [f"Final Speed:       {round(d/D['dt'],3)}"],
                [f"Time of Flight:    {round(D['tof'],3)}"]]
    
    outcomes = Table(outcomes,
            style=[("BOX",(0,0),(-1,-1),2,colors.gray),
                   ("FONTNAME",(0,0),(-1,-1),"Courier")])
    
    return conditions, props, environs, outcomes


def list_to_intervals(L,n):
    out = []
    row = []
    for pos,val in enumerate(L,1):
        row.append(val)
        if pos % n == 0:
            out.append(row)
            row = []
    if len(row) > 0:
        out.append(row)
    return out


def line_plot(x,y):
    drawing = Drawing(400, 200)
    
    data = [(a,b) for a,b in zip(x,y)]
    
    lp = LinePlot()
    lp.y = 40
    lp.x = 30 
    lp.width = 400
    lp.height = 200
 
 
    lp.lineLabels.fontSize = 6
    lp.lineLabels.boxStrokeWidth = 0.5
    lp.lineLabels.visible = 1
    lp.lineLabels.boxAnchor = 'c'
    lp.lineLabels.angle = 0
    lp.lineLabelNudge = 10
    lp.joinedLines = 1
    lp.lines.strokeWidth = 1.5
 
    lp.data = [data]
    drawing.add(lp)
     
     
    return drawing


def ballistic_pdf(V0,th,y0,g,m,A,Cd,rho,dt=1/30):
    data, x, y = ballistic_motion(V0,th,y0,g,m,A,Cd,rho,dt)
    datatabs = ballistic_tables(data,x,y)
    doc = SimpleDocTemplate("BallisticMotion.pdf", pagesize=letter)


    elements = []
    
    draw = line_plot(x,y)
    elements.append(draw)

    for t in datatabs:
        elements.append(t)
        elements.append(Spacer(1, 30))
    
    doc.build(elements)
    
    return data, x, y




if __name__ == '__main__':
    
    ballistic_pdf(90,1,10,10,20,.7,.2,10.2)
    