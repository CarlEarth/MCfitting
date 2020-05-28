import math
import random 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def linear(a, b, x): #Define the Target function
   return a*x+b
yexp=[[-5.0,-6.1,0.3], #The fake data (x,y,sigma)
      [-4.0,-3.7,0.2],
      [-3.0,-2.2,0.15],
      [-2.0,-0.1,0.15],
      [-1.0, 2.1,0.15],
      [0.0,4.1,0.15],
      [1.0,6.3,0.15],
      [2.0,7.9,0.18],
      [3.0,10.0,0.2],
      [4.0,11.6,0.3]]
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
xibest=100000000.0 # Given a large initial xisquare
for i in range(0,40000):# The number of the sample points
    xitotal=0.0 # initial total xisquare
    liketotal=1.0 # initial total likelohood
    a=random.uniform(1.75,2.25) #random a.b
    b=random.uniform(3.75,4.25)
    for j in range(0,10):
        yth=linear(a,b,yexp[j][0])
        #xisquare=(yth-yexp)^2/s^2
        xisquare=(yth-yexp[j][1])**2.0/(yexp[j][2])**2.0
        #gaussian likelihood function f(x,s)=(2pi*s^2)^-0.5*exp(-x^2/2)
        likelihood= math.exp(-xisquare/2.0)/(2.0*math.pi*(yexp[j][2])**2.0)**0.5
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

print'Bestfit: y=',abest,'x+',bbest
print'Xi square =',xibest 
