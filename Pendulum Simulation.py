# Simulating a pendulum

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import time
import os # to launch imagemagick

# constants
print('Setting constants')
ti = 0
tf = 2.1
dt = 0.01
g = 9.81
L = 1
m = 1

# theta1 = angle
# theta2 = angular vel
# pass both to function as theta = [theta1, theta2]

def Equation(t,theta):
    dtheta2dt = (-1*g/L)*np.sin(theta[0])
    dtheta1dt = theta[1]
    return [dtheta1dt, dtheta2dt]

# init conditions
print('Setting initial conditions.')
theta_i = [np.pi/4, 0]
t = np.arange(ti,tf+dt,dt)
points = np.arange(0,len(t),1)

# solve and extract data
print('Solving the equation.')
theta12 = solve_ivp(Equation, [ti, tf+dt], theta_i, t_eval=t)
theta1 = theta12.y[0,:]
theta2 = theta12.y[1,:]

# plot and save image
print('Saving solution details.')
plt.plot(t,np.round(np.rad2deg(theta1),4),label='Angular displacement (degrees)')
plt.plot(t,np.round(np.rad2deg(theta2),4),label='Angular velocity (deg/s)')
plt.xlabel('Time')
plt.legend(loc='best')
#plt.show()
plt.savefig('Plots/VelDispPlot.png',format='png', dpi=1200)

# Now, on to simulation.
x = L*np.sin(theta1)
y = -L*np.cos(theta1) # Because we want it to face downwards - in 3rd and 4th quadrant

# define colours
N = len(points) # number of colours needed
cols = plt.cycler('color', plt.cm.Purples(np.linspace(0,1,N//4)))
cols = [row['color'] for row in list(cols)]
cols = list(reversed(cols)) + cols + list(reversed(cols)) + cols
diff = N - len(cols)
cols = cols + [cols[-1]]*diff

# start timing here
print('Plotting the plots.')
begin = time.time()
counter = 0
for point in points:
    plt.figure()
    plt.plot([0,x[point]], [0,y[point]])
    plt.plot(x[point],y[point],'o',markersize=30,markerfacecolor=cols[counter])
    plt.xlim(-L-0.2, L+0.2)
    plt.ylim(-L-0.2, L+0.2)
    plt.xlabel('X-direction')
    plt.ylabel('Y-direction')
    filenumber = point
    filenumber=format(filenumber, '04')
    plt.savefig('Plots/Image_{0}.png'.format(filenumber), dpi=100, format='png')
    plt.close()
    counter = counter +1
    print('Done with Plot {0}.'.format(counter))
durn = time.time()-begin
print('Done. This took {0} s.'.format(durn))
# launch Imagemagick
print('Launching Imagemagick for conversion.')
begin=time.time()
os.system('magick -verbose -limit file 5 -limit memory 40MiB -set delay 1x30 -loop 0 Plots/Image*.png Plots/TestAnim.gif')
durn = time.time()-begin
print('All Done. This took {0} s.'.format(durn))
