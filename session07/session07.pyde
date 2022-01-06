xmin = -10
xmax = 10
ymin = -10
ymax = 10
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl,yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey
    
def draw():
    line(-10,10,-10,10)
