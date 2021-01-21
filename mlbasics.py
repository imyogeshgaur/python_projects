import numpy
import matplotlib.pyplot as plt
happy=[0,0,0,0,0]
a=numpy.mean(happy)
b=numpy.median(happy)
c=numpy.std(happy)
d=numpy.var(happy)
print(a)
print(b)
print(c)
print(d)
x=numpy.random.normal(5.0,1.0,1000)#to make a normal distribution
plt.hist(x,100)
plt.show()
y=numpy.random.normal(10,2,1000)
plt.scatter(x,y)
plt.show()
sad=[1,2,3,4,5]
plt.scatter(happy,sad)
plt.show()
from sklearn.metrics import r2_score
a=[1,2,3,5,6,7,8,9,10,12,13,14,15,16,17,18,19,21,22]
b=[100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
mymodel=numpy.poly1d(numpy.polyfit(x,y,3))
speed=mymodel(17)
print(speed)



