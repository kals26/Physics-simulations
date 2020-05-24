# Pendulum Simulation
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


time=np.linspace(0,20,100)
theta0=[0,3]
#b=0.2
g=9.81
m=1
l=1
def Equation(theta,time,g,l,m):
 theta1=theta[0]
 theta2=theta[1]
 dtheta1dt=theta2
 dtheta2dt=-(g/l)*math.sin(theta1)
 dthetadt=[dtheta1dt,dtheta2dt]
 return dthetadt
theta=odeint(Equation,theta0,time,args=(g,l,m))
#print("What is theta:\n",theta)
'''x= np.array(theta)
y=np.array(time)
plt.plot(x,y)
plt.show()'''
#Seriously don't know what this graph is about.
#plotting the pendulum

'''x0=0
y0=0'''


'''x1=l*math.sin()
y1=-l*math.cos()'''

  
  
'''plt.plot([-1,1],[0,0],linewidth=2,c='black')
plt.scatter(x1,y1,s=50,c='purple')
plt.plot([x0,x1],[y0,y1],c='blue')
plt.title('Simple Pendulum', loc='center')
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.savefig('Plot000.png')'''





