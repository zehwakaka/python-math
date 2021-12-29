'''part01'''
# def average(a,b):
#     return a+b/2
# print(average(10,20))


'''part02'''
# x = 3
# y = float(x)
# z = int(y)
# print(x,y,z)

'''part03'''
# a = "hello"
# print(a+a,a*4)
# b = 2
# d = "hello"
# # print(b,b+d)
# b = '123'
# c = '4'
# print(b+c,'hello'+' 123')
# name = "marcia"
# print(3*name)

'''part04'''
# noun = 'dog'
# verb = 'bark'
# print(noun*verb)

'''part05'''
# print(3>2)
# b=5
# print(b==5)
# print(b==6)

'''part06'''
a = True
print(type(a))
b = 2
print(type(b))
c = 0.5
print(type(c))
name = "Steve"
print(type(name))
a = [1,2,3]
print(a)
b = []
print(b)
b.append(4)
print(b)
b.append(5)
b.append(True)
b.append("hello")

c = [7,True]
d = [8,'Python']
print(c+d)
print(2*d)

b = [4,5,True,'hello']
b.remove(5)
print(b)

a = [12,"apple",True,0.25]
for thing in a:
    print(thing)   #迭代器

for thing in a:
    print(thing,end='')

a = [12,"apple",True,0.25]
for thing in a:
    print(thing,end=',')

name_list = ['Abe','Bob','Chloe','Daphne']
score_list = [55,63,72,54]
print(name_list[0],score_list[0])

n = 2
print(name_list[n],score_list[n+1])

for i in range(4):
    print(name_list[i],score_list[i])

name_list = ['Abe','Bob','Chloe','Daphne']
for i,name in enumerate(name_list):
    print(name,"has index",i)

b = [4,True,'hello']
print(b[0],b[2])

myList = [1,2,3,4,5,6,7]
myList[1:6]

print(b[1:],b[:1],b[-1],b[-2])

c = [1,2,3,'hello']
print(c.index(1),c.index('hello'))

print(4 in c,3 in c)
d = 'Python'
print(len(d),d[0],d[1],d[-1],d[2:],d[:5],d[1:4])

running_sum = 0
running_sum += 3
print(running_sum)
running_sum += 5
print(running_sum)

running_sum = 0
for i in range(10):
    running_sum += 3
print(running_sum)

def mySum(num):
    running_sum = 0
    for i in range(1,num+1):
        running_sum += i
    return running_sum
print(mySum(100))

def mySum2(num):
    running_sum = 0
    for i in range(num+1):
        running_sum += i**2 +1
    return running_sum

print(mySum2(20))
print(sum([8,11,15]))
print(len([8,11,15]))

def average3(numList):
    return sum(numList)/len(numList)
print(average3([8,11,15]))







