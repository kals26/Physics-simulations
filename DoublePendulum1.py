# Double pendulum
# Equations of motion:
# d(omega1)/dt= 1/l1*(cos^2(m2)-m1-m2)[l1*m2*cos(theta1-theta2)*sin(theta1-theta2)*omega1^2+ l2*m2*sin(theta1-theta2)*onega2^2-m2*g*cos(theta1-theta2)*sin(theta2)+(m1+m2)*g*sin(theta1)]
# d(omega2)/dt= 1/l2*(cos^2(m2)-m1-m2)[l2*m2*cos(theta1-theta2)*sin(theta1-theta2)*omega2^2+ l1*(m1+m2)*sin(theta1-theta2)*omega1^2+ (m1+m2)*g*sin(theta1)*cos(theta1-theta2)- (m1+m2)*g*sin(theta1)]
# omega1= d(theta1)/dt
# omega2= d(theta2)/dt
import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import cos, sin, pi
import time

start= time.time()
g = 9.81 # Acceleration due to gravity

def Polar(z, t, L1, L2, m1, m2, g): # to solve for angular velocities and angular displacement
    theta1, w1, theta2, w2 = z
    cos12 = cos(theta1 - theta2)
    sin12 = sin(theta1 - theta2)
    sin1 = sin(theta1)
    sin2 = sin(theta2)
    xi = cos12**2*m2 - m1 - m2
    w1dot = ( L1*m2*cos12*sin12*w1**2 + L2*m2*sin12*w2**2
            - m2*g*cos12*sin2  + (m1 + m2)*g*sin1)/(L1*xi)
    w2dot = -( L2*m2*cos12*sin12*w2**2 + L1*(m1 + m2)*sin12*w1**2
            + (m1 + m2)*g*sin1*cos12  - (m1 + m2)*g*sin2 )/(L2*xi)
    return w1, w1dot, w2, w2dot
def Cartesian(theta1, w1, theta2, w2, L1, L2):
    # Convert from polar to cartesian
    x1 = L1 * sin(theta1)
    y1 = -L1 * cos(theta1)
    x2 = x1 + L2 * sin(theta2)
    y2 = y1 - L2 * cos(theta2)
    vx1 = L1*cos(theta1)*w1
    vy1 = L1*sin(theta1)*w1
    vx2 = vx1 + L2*cos(theta2)*w2
    vy2 = vy1 + L2*sin(theta2)*w2
    return x1, y1, x2, y2, vx1, vy1, vx2, vy2

# initial conditions
L1, L2 = 1., 2.
m1, m2 = 3., 1.
z0 = [pi/2, 0, pi/2, 0] # pendulum be in x=0 initially with angular velocities zero.
tstop=50
dt= 0.1
t = np.arange(0, tstop, dt)

# Perform simulation
z = odeint(Polar, z0, t, args=(L1, L2, m1, m2, g))

# To get plotting arrays
theta1, w1, theta2, w2 = z[:,0], z[:,1], z[:,2], z[:,3]
x1, y1, x2, y2, vx1, vy1, vx2, vy2 = Cartesian(theta1, w1, theta2, w2, L1, L2)


'''# To get the movement of both bobs:
plt.plot(x1, y1, label=r"m1 movement", c='y')
plt.plot(x2, y2, label=r"m2 movement", c='g')
plt.plot([0, x1[0], x2[0]], [0, y1[0], y2[0]], "-o", label="Starting position", c='m')
plt.ylabel(r"y coordinate")
plt.xlabel(r"x coordinate")
plt.legend()'''

# To create a single plot with chaotic movement of bobs, angular velocity, angular disp variations.
def plot(x1, y1, x2, y2, theta1, theta2, t):
    figsize= 6
    dpi=600
    plt.figure(figsize=(2*figsize, figsize), dpi=dpi)
    plt.title('Double Pendulum Characteristics')

    # bob movement, the x-y graph
    L = 1.5*(L1 + L2)
    ax = plt.subplot(2, 2, (1, 3), autoscale_on=False, xlim=(-L, L), ylim=(-L, L))
    ax.plot(x1, y1, label=r"m1 movement",c='g')
    ax.plot(x2, y2, label=r"m2 movement",c='y')
    plt.ylabel(r"y-coordinate")
    plt.xlabel(r"x-coordinate")
    ax.legend()

    # theta vs time plot
    ax = plt.subplot(2, 2, 2)
    ax.plot(t, theta1, label=r"theta1", c='g')
    ax.plot(t, theta2, label=r"theta2",c='y')
    plt.ylabel(r"angular displacement,theta [rad]")
    plt.xlabel(r"time [s]")
    ax.legend()
    plt.xlim([0, np.max(t)])

    # omega vs time plot
    ax = plt.subplot(2, 2, 4)
    ax.plot(t, w1, label=r"omega1(t)",c='g')
    ax.plot(t, w2, label=r"omega2(t)",c='y')
    plt.ylabel(r"angular velocity,omega[rad/s]")
    plt.xlabel(r"time [s]")
    plt.xlim([0, np.max(t)])
    ax.legend()

# Plot the characteristics of a double pendulum
plot(x1, y1, x2, y2, theta1, theta2, t)
plt.savefig('DoublePendulumStat.png',format='png')

# Now to obtaining the phase space plot
def plot_phasespace(theta1, w1, theta2, w2):
  plt.figure()
  plt.plot(theta1, w1, label=r"theta1",c='g')
  plt.plot(theta2, w2, label=r"theta2",c='y')
  plt.legend()
  plt.xlabel(r"Angular displacement [rad]")
  plt.ylabel(r"Angular velocity [rad/s]")
  xlim = [np.min(theta1), np.max(theta1), np.min(theta2), np.max(theta2)]
  plt.xlim(np.min(xlim), np.max(xlim))

# Plot the phase space plot
plot_phasespace(theta1,w1,theta2,w2)
plt.title('Phase space diagram')
plt.savefig('PhaseSpacePlot.png',format='png')

# Now to animation, Creation of frames into a directory called frames.
from matplotlib.patches import Circle

# Plotted bob circle radius
r = 0.1
# Plot a trail, because it looks beautiful on tracing.
trail_secs = 1
# This corresponds to max_trail time points, this part taken online: Just make the animation look cool!
max_trail = int(trail_secs / dt)

def make_plot(i):
    # Plot and save an image of the double pendulum configuration for time
    
    ax.plot([0, x1[i], x2[i]], [0, y1[i], y2[i]], lw=2, c='k')
    # Circles representing the hang point of rod 1, and bobs 1 and 2.
    c0 = Circle((0, 0), r/2, fc='k', zorder=10)
    c1 = Circle((x1[i], y1[i]), r, fc='b', ec='b', zorder=10)
    c2 = Circle((x2[i], y2[i]), r, fc='r', ec='r', zorder=10)
    ax.add_patch(c0)
    ax.add_patch(c1)
    ax.add_patch(c2)

    # The trail will be divided into ns segments and plotted as a fading line.
    ns = 20
    s = max_trail // ns

    for j in range(ns):
        imin = i - (ns-j)*s
        if imin < 0:
            continue
        imax = imin + s + 1
        # The fading looks better if we square the fractional length along the
        # trail.
        alpha = (j/ns)**2
        ax.plot(x2[imin:imax], y2[imin:imax], c='r', solid_capstyle='butt',
                lw=2, alpha=alpha)

    # Save all the generated images now!
    ax.set_xlim(-L1-L2-r, L1+L2+r)
    ax.set_ylim(-L1-L2-r, L1+L2+r)
    ax.set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.savefig('frames_img{:04d}.png'.format(i//di), dpi=72)
    plt.cla()


# Makes an image every dt, corresponding to a frame rate of fps
fps = 10
di = int(1/fps/dt)
fig = plt.figure(figsize=(8.3333, 6.25), dpi=72)
ax = fig.add_subplot(111)

for i in range(0, t.size, di):
    print(i // di, '/', t.size // di)
    make_plot(i)
# Ends making frames!
# Frames get saved in frames directory of miniconda directory. Please create a frames directory.

# Count the time!
end= time.time()- start
print('All done{0}'.format(end))

# End!









