
# 设置x的最小值和最大值
xmin = -10
xmax = 10

# y的最小值和最大值
ymin = -10
ymax = 10

# 计算x值和y值的范围
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl,yscl
    size(600,600)
    xscl = width / rangex
    yscl = -height / rangey
    
def draw():
    global xscl,yscl
    background(255) # 白色
    translate(width/2,height/2)
    # 青色的线
    strokeWeight(1)
    stroke(0,255,255)
    for i in range(xmin,xmax+1):
        line(i,ymin,i,ymax)
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
        
