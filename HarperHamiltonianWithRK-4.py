# H = l cos p + k cos q

import numpy as np
import matplotlib.pyplot as plt
import time

# define basic change parameters
dt = 0.1
dx = 0.
dy = 0.

# Preallocate variables for speed
t = len(np.arange(0,100,dt)) # For what value of t should I find x(t) and y(t) ?
q = np.zeros(t) # Values of q(t)
p = np.zeros(t) # Values of p(t)

# Function to implement RK(4) method
def Rk4Method(flag, val):
    # We know that the function f(x) = flag*sin(val)
    f1 = dt*flag*np.sin(val)
    f2 = dt*flag*np.sin(val + (f1*0.5))
    f3 = dt*flag*np.sin(val + (f2*0.5))
    f4 = dt*flag*np.sin(val + f3)
    # Keep in mind that we have to return dx or dy!
    res = (f1 + 2*f2 + 2*f3 + f4)/6
    return res 

begin = time.time()
for i in np.arange(-10, 10,0.5):
    for j in np.arange(-10, 10, 0.5):
        # Show (i,j) for debugging purposes
        print('i = {0}, j = {1}. Time elapsed = {2} s.'.format(i,j, (time.time()-begin)), flush = True, end = '\r')
        q[0] = i*np.pi/2 # Set initial conditions
        p[0] = (j+0.5)*np.pi/2
        for k in range(t-1): # Create arrays!
            dq = np.sin( p[k] )*dt
            q[k+1] = q[k] + dq
            dp = -1*np.sin(q[k])*dt
            p[k+1] = p[k]+dp

        # Now, we can try out the RK(4) method.
        for k in range(t-1): 
            dq = Rk4Method(1, p[k])
            q[k+1] = q[k] + dq
            dp = Rk4Method(-1, q[k])
            p[k+1] = p[k]+dp
        
        plt.plot(q,p)
        plt.xlim(-100,100)
        plt.ylim(-100,100)

# Now that all the plotting is done, show!
plt.title('Phase space plot of Harper Hamiltonian')
plt.xlabel('Position (q)')
plt.ylabel('Momentum (p)')
#plt.savefig('HarperHamiltonianPhaseSpace.png', format='png', dpi=3200)
plt.show()





