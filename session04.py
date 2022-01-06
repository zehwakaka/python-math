'''part01'''
# def plug():
#     x = -100 # 从-100开始
#     while x < 100: # 一直到100
#         if 2*x + 5 == 13: # 如果使等式成立
#             print("x =",x)
#         x += 1
# plug() # 运行plug函数

# def equation(a,b,c,d):
#     '''解ax + b = cx + d形式的方程'''
#     return (d-b)/(a-c)

# print(equation(1/2,2/3,1/5,7/8))
# x = equation(12,18,-34,67)
# print(12*x + 18,-34*x + 67)
'''part02'''
# from math import sqrt
# def quad(a,b,c):
#     '''返回a*x**2 + b*x + c = 0形式的方程的解'''
#     x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
#     x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
#     return x1,x2
# print(quad(2,7,-15))
# print(2*1.5**2 + 7*1.5 - 15,2*(-5)**2 + 7*(-5) - 15)

# def g(x):
#     return 6*x**3 + 31*x**2 + 3*x - 10

# def plug():
#     x = -100
#     while x < 100:
#         if g(x) == 0:
#             print("x =",x)
#         x += 1
#     print("done.") 
# print(plug())

