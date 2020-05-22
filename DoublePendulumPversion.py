import numpy as np
import scipy.integrate as integrate

class DoublePendulum:
    '''
    Double Pendulum Class

    initState is [theta1, omega1, theta2, omega2] in degrees,
    where theta1, omega1 is the angular position and velocity of the first
    pendulum arm, and theta2, omega2 is that of the second pendulum arm
    '''
    def __init__(self,
                 initState = [120, 0, -20, 0],
                 L1=1.0,  # length of pendulum 1 in m
                 L2=1.0,  # length of pendulum 2 in m
                 M1=1.0,  # mass of pendulum 1 in kg
                 M2=1.0,  # mass of pendulum 2 in kg
                 G=9.8,  # acceleration due to gravity, in m/s^2
                 origin=(0, 0)): 
        self.initState = np.asarray(initState, dtype='float')
        self.params = (L1, L2, M1, M2, G)
        self.origin = origin
        self.timeElapsed = 0

        self.state = self.initState * np.pi / 180.
    
    def Position(self):
        '''compute the current x,y positions of the pendulum arms'''
        (L1, L2, M1, M2, G) = self.params

        x = np.cumsum([self.origin[0],
                       L1 * np.sin(self.state[0]),
                       L2 * np.sin(self.state[2])])
        y = np.cumsum([self.origin[1],
                       -L1 * np.cos(self.state[0]),
                       -L2 * np.cos(self.state[2])])
        return (x, y)

    def Energy(self):
        '''compute the energy of the current state'''
        (L1, L2, M1, M2, G) = self.params

        x = np.cumsum([L1 * np.sin(self.state[0]),
                       L2 * np.sin(self.state[2])])
        y = np.cumsum([-L1 * np.cos(self.state[0]),
                       -L2 * np.cos(self.state[2])])
        vx = np.cumsum([L1 * self.state[1] * np.cos(self.state[0]),
                        L2 * self.state[3] * np.cos(self.state[2])])
        vy = np.cumsum([L1 * self.state[1] * np.sin(self.state[0]),
                        L2 * self.state[3] * np.sin(self.state[2])])

        U = G * (M1 * y[0] + M2 * y[1])
        K = 0.5 * (M1 * np.dot(vx, vx) + M2 * np.dot(vy, vy))

        return U + K

    def DstateDt(self, state, t):
        '''compute the derivative of the given state'''
        (M1, M2, L1, L2, G) = self.params

        dydx = np.zeros_like(state)
        dydx[0] = state[1]
        dydx[2] = state[3]

        cosDelta = np.cos(state[2] - state[0])
        sinDelta = np.sin(state[2] - state[0])

        den1 = (M1 + M2) * L1 - M2 * L1 * cosDelta * cosDelta
        dydx[1] = (M2 * L1 * state[1] * state[1] * sinDelta * cosDelta
                   + M2 * G * np.sin(state[2]) * cosDelta
                   + M2 * L2 * state[3] * state[3] * sinDelta
                   - (M1 + M2) * G * np.sin(state[0])) / den1

        den2 = (L2 / L1) * den1
        dydx[3] = (-M2 * L2 * state[3] * state[3] * sinDelta * cosDelta
                   + (M1 + M2) * G * np.sin(state[0]) * cosDelta
                   - (M1 + M2) * L1 * state[1] * state[1] * sinDelta
                   - (M1 + M2) * G * np.sin(state[2])) / den2
        
        return dydx

    def Step(self, dt):
        '''execute one time step of length dt and update state'''
        self.state = integrate.odeint(self.DstateDt, self.state, [0, dt])[1]
        self.timeElapsed += dt

#------------------------------------------------------------
