# def f(x):
#     return 6*x**3 + 31*x**2 + 3*x - 10

# print(f(0.5),f(-0.5),f(-0.75),f(-0.625))

'''猜测方法'''
def f(x):
    return 6*x**3 + 31*x**2 + 3*x - 10

def average(a,b):
    return (a + b)/2.0

def guess():
    lower = -1
    upper = 0
    for i in range(20):
        midpt = average(lower,upper)
        if f(midpt) == 0:
            return midpt
        elif f(midpt) < 0:
            upper = midpt
        else:
            lower = midpt
    return midpt
x = guess()
print(x,f(x))