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
    yscl = -height /rangey
    
def draw():
    global xscl,yscl
    background(255) # 白色
