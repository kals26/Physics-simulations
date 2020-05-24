from scipy.integrate import solve_ivp

def ode(t, C):
    Ca, Cb, Cc = C
    dCadt = -k1 * Ca
    dCbdt = k1 * Ca - k2 * Cb
    dCcdt = k2 * Cb
    return [dCadt, dCbdt, dCcdt]

C0 = [1.0, 0.0, 0.0]
k1 = 1
k2 = 1

sol = solve_ivp(ode, (0, 10), C0)


import matplotlib.pyplot as plt

plt.plot(sol.t, sol.y.T)
'''plt.legend(['A', 'B', 'C'])
plt.xlabel('Time')
plt.ylabel('C')'''

# Trying a basic neural net to mimick a system of ODE'S

import autograd.numpy as np
from autograd import grad, elementwise_grad, jacobian
import autograd.numpy.random as npr
from autograd.misc.optimizers import adam

def init_params(scale, layer_sizes, rs=npr.RandomState(0)):
    """Build a list of (weights, biases) tuples, one for each layer."""
    return [(rs.randn(insize, outsize) * scale,   # weight matrix
             rs.randn(outsize) * scale)           # bias vector
            for insize, outsize in zip(layer_sizes[:-1], layer_sizes[1:])]

def function(x):
    
    return x / (1.0 + np.exp(-x))

def C(params, inputs):
    "Neural network functions"
    for W, b in params:
        outputs = np.dot(inputs, W) + b
        inputs = function(outputs)
    return outputs

# initial guess for the weights and biases
params = init_params(0.1, layer_sizes=[1, 8, 3])
def obj_soln(params, step):
    return np.sum((sol.y.T - C(params, sol.t.reshape([-1, 1])))**2)

params = adam(grad(obj_soln), params,
              step_size=0.001, num_iters=500)

plt.plot(sol.t.reshape([-1, 1]), C(params, sol.t.reshape([-1, 1])),
          '--')
plt.legend()
plt.xlabel('Time')
plt.ylabel('C')
plt.show()

