import numpy as np
import matplotlib.pyplot as plt
import time

def QuantumWalk(N, theta, phi):
    P = 2*N+1
    
    coin0 = np.array([1,0]) # |0>
    coin1 = np.array([0,1]) #|1>

    # hadamard coin operator

    C00 = np.outer(coin0, coin0)  # |0><0| 
    C11 = np.outer(coin1, coin1)  # |1><1| 
        
    zeta = np.pi/2
    xi = 0

    C_hat = np.array([[np.exp(1j*xi)*np.cos(theta),  np.exp(1j*zeta)*np.sin(theta)],[ np.exp(-1j*zeta)*np.sin(theta), -1*np.exp(1j*xi)*np.cos(theta)]])

    #shift operators
    ShiftR = np.roll(np.eye(P), 1)
    ShiftL = np.roll(np.eye(P), -1)
    S_hat = np.kron(ShiftR, C00) + np.kron(ShiftL,C11)

    # walk operator
    U = np.dot(np.kron(np.eye(P),C_hat), S_hat)

    # initial state
    posn0 = np.zeros(P)
    posn0[N] = 1     # array indexing starts from 0, so index N is the central posn
    
    phi = np.radians(phi)
    psi0 = np.kron(posn0,(coin0*np.cos(phi)+coin1*np.sin(phi)))

    # do N steps of walking
    psiN = np.dot(np.linalg.matrix_power(U,N),psi0)

    # measurements
    probs = np.empty(P)
    for k in range(P):
        posn = np.zeros(P)
        posn[k] = 1
        M_hat_k = np.kron( np.outer(posn,posn), np.eye(2))
        proj =   np.dot(M_hat_k,psiN)
        probs[k] = proj.dot(proj.conjugate()).real

    return probs
    

    

theta = 45
phi = 45
Etime = []
for i in range(1,100):
    N = i
    start = time.time()
    _ = QuantumWalk(N, theta, phi)
    Etime.append(time.time()-start)

plt.plot(Etime)
plt.title('How long does it take to run a QW program?')
plt.xlabel('N')
plt.ylabel('Time of execution')
print('Total Execution time' ,time.time() - start, 'seconds')
plt.show()

