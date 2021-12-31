


'''part01'''
# print(6>5)
# print(6>7)
# print(6 == 6)
# y = 3
# x = 4
# print(y > x)
# print(y < 10)

'''part02'''
# y = 7
# if y > 5:
#     print("yes!")

# y = 6
# if y > 7:
#     print("yes!")
# else:
#     print("no!")

# age =  50
# if age < 10:
#     print("What school do you go to?")
# elif 11 < age < 20:
#     print("You're cool!")
# elif 20 <= age < 30:
#     print("What job do you have?")
# elif 30 <= age < 40:
#     print("Are you married?")
# else:
#     print("Wow,you're old!")    

# print(20 % 3)
# print(20 % 5)

# def factors(num):
#     '''返回一个由num的因数组成的列表'''
#     factorList = []
#     for i in range(1,num + 1):
#         if num % i == 0:
#             factorList.append(i)
#     return factorList

# print(factors(120))


# #方法一：
# a=int(input("请输入一个数："))
# b=int(input("请输入另外一个数："))
# while(a%b!=0):
#     MOD=a%b
#     a=b
#     b=MOD

# print("gcd(a,b)=",b)

#方法二：
# def gcd(a,b):
#     if b!=0:
#         return gcd(b,a%b)
#     else:
#         return a

# print(gcd(15,8))
'''part03'''
# from turtle import *
# from random import randint
# speed(0)
# def wander():
#     while True:
#         fd(3)
#         if xcor() >= 200 or xcor() <= -200 or ycor() <= -200 or ycor() >= 200:
#             lt(randint(90,180))
# wander()
'''part04'''
# from random import randint
# def numberGame():
#     # 随机选择一个 1 到 100 的数
#     number = randint(1,100)
#     return number

# print(numberGame())
'''part05'''
# name = input("What's your name?")
# print(name)

# def greet():
#     name = input("What's your name?")
#     print("Hello,",name)
# greet()

# print("I'm thinking of a number between 1 and 100.")
# guess = int(input("What's your guess?"))
'''part06'''
# from random import randint
# def numberGame():
#     # 随机选择一个1到100的数
#     number = randint(1,100)
#     print("I'm thinking of a number between 1 and 100.")
#     guess = int(input("What's your guess?"))

#     if number == guess:
#         print("That's correct! The number was",number)
#     elif number > guess:
#         print("Nope. Higher.")
#     else:
#         print("Nope.Lower.")

# numberGame()
'''part07 猜数游戏'''
# from random import randint
# def numberGame():
#     # 随机选择一个 1 到 100 的数
#     number = randint(1,100)
#     print("I'm thinking of a number between 1 and 100.")
#     guess = int(input("What's your guess?"))

#     while guess:
#         if number == guess:
#             print("That's correct! The number was",number)
#             break
#         elif number > guess:
#             print("Nope. Higher.")
#         else:
#             print("Nope. Lower.")
#         guess = int(input("What's your guess?"))

# numberGame()
'''part08'''
# import math
# # print(dir(math))
# print(100*0.5,50*0.5,25*0.5,12.5*0.5,6.25*0.5,3.125*0.5,1.5625*0.5)
# def average(x,y):
#     return (x+y)/2

# print(average(7,8),7.5**2,average(7.5,8),7.75**2)
'''part09'''
def average(a,b):
    return (a+b)/2

def squareRoot(num,low,high):
    '''采用猜数游戏策略，通过在从low到high的范围内猜测，寻找num的平方根'''
    for i in range(20):
        guess = average(low,high)
        if guess**2 == num:
            print(guess)
        elif guess**2 > num: # “猜小一点儿。”
            high = guess
        else:# “猜大一点儿。”
            low = guess
    print(guess)
squareRoot(60,7,8)
print(7.745966911315918**2)



 