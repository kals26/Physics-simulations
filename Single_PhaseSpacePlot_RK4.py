import numpy as np
from math import sin, cos , pi 
import matplotlib.pyplot as plt

k=-4
l=4

def fp(px,qx,H,t):
    return k*sin(qx)
def fq(px,qx,H,t):
    return l*sin(px)
def fH(px,qx,H,t): 
    H=k*cos(qx)+l*cos(px) 
    return k*cos(qx)+l*cos(px)

def RK4(px,qx,H,fx,fy,fz,t,h):
    k1px,k1qx,k1H = ( h*f(px,qx,H,t) for f in (fp,fq,fH) )
    pxs,qxs,Hs,ts = ( r+0.5*kr for r,kr in zip((px,qx,H,t),(k1px,k1qx,k1H,h)) )
    k2px,k2qx,k2H = ( h*f(pxs,qxs,Hs,ts) for f in (fp,fq,fH))
    pxs,qxs,Hs,ts = ( r+0.5*kr for r,kr in zip((px,qx,H,t),(k2px,k2qx,k2H,h)) )
    k3px,k3qx,k3H = ( h*f(pxs,qxs,Hs,ts) for f in (fp,fq,fH) )
    pxs,qxs,Hs,ts = ( r+kr for r,kr in zip((px,qx,H,t),(k3px,k3qx,k3H,h)) )
    k4px,k4qx,k4H  =( h*f(pxs,qxs,Hs,ts) for f in (fp,fq,fH) )
    #print(k4px, k4qx, k4H)
    return (r+(k1r+2*k2r+2*k3r+k4r)/6 for r,k1r,k2r,k3r,k4r in 
            zip((px,qx,H,t),(k1px,k1qx,k1H),(k2px,k2qx,k2H),(k3px,k3qx,k3H),(k4px,k4qx,k4H)))
   
tIn=0.
tFin=10.
h=0.01
deltaT=int(np.floor((tFin-tIn)/h))

t =  deltaT *[0.01]
px = deltaT * [0.01]
qx = deltaT * [0.01]
H =  deltaT* [0.01]

px[0],qx[0],t[0],H[0] =  1. , 1., 0., k*cos(1) + l*cos(1) #Initial condition
for i in range(1, deltaT):
    px[i],qx[i],H[i] = RK4(px[i-1],qx[i-1], H[i-1],fp,fq,fH, t[i-1], h)
    #print( px[i], qx[i])

plt.plot(px,qx,'m.', markersize=1.5)
plt.xlabel('qx')
plt.ylabel('px') 
plt.show()

'''from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(H, qx, px, 'g.',markersize=0.5)
ax.set_xlabel('q')
ax.set_ylabel('p')
ax.set_zlabel('H')
plt.title('check plot')

plt.show()'''














