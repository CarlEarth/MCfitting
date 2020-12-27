import math
import random 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import sys

def linear(a, b, x): #Define the Target function
   return a*x+b

def xisquare_f(input,data,sigma): #xisquare=(yth-yexp)^2/s^2
    return (input-data)**2.0/sigma**2.0

def likelihood_f(input,data,sigma):
    #gaussian likelihood function
    #f(x,s)=(2pi*s^2)^-0.5*exp(-xisquare^2/2)
    return math.exp(-((input-data)**2.0/sigma**2.0)/2.0)/(2.0*math.pi*(yexp[j][2])**2.0)**0.5

yexp=[[-5.0,-6.6,0.7], #The fake data (x,y,sigma)
      [-4.0,-3.5,0.6],
      [-3.0,-2.5,0.5],
      [-2.0,-0.1,0.5],
      [-1.0, 2.1,0.5],
      [0.0,4.1,0.5],
      [1.0,6.3,0.4],
      [2.0,7.9,0.4],
      [3.0,10.0,0.4],
      [4.0,11.6,0.4]]
y=(np.array(yexp)).transpose()

#------------ Set for figure export----------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x1=[]
x2=[]
x3=[]
ax.set_xlabel('coefficient a')
ax.set_ylabel('coefficient b')
ax.set_zlabel('Likelihood')
#------------ Set for figure export----------
result=[]
xibest=sys.float_info.max # Given a large initial xisquare
for i in range(0,40000):# The number of the sample points
    xitotal=0.0 # initial total xisquare
    liketotal=1.0 # initial total likelohood
    a=random.uniform(1.75,2.25) #random a.b
    b=random.uniform(3.75,4.25)
    for j in range(0,10):
        yth=linear(a,b,yexp[j][0])
        xisquare=xisquare_f(yth,yexp[j][1],yexp[j][2])
        likelihood=likelihood_f(yth,yexp[j][1],yexp[j][2])
        xitotal= xitotal+xisquare #(Sum(xisquare))
        liketotal=liketotal*likelihood #(likelihood*likelihood*...))
    result.append([a,b,xitotal,liketotal])#save the result
    x1.append(a)
    x2.append(b)
    x3.append(liketotal)
    if (xibest > xitotal):
       xibest=xitotal
       likebest=liketotal
       abest=a
       bbest=b
#    if (liketotal > 1.0):
#       print(a,b,xitotal,liketotal)
ax.scatter(x1, x2, x3, c='g', marker='o',s=0.05)
plt.show()
plt.savefig('image%d'%(j))

print('Bestfit: y=',abest,'x+',bbest)
print('Xi square =',xibest)
s=("Data points and fitting result")
plt.title(s)
plt.errorbar(y[0],y[1],yerr=y[2],fmt='o')
plt.plot(y[0], y[0]*abest + bbest)
plt.show()
