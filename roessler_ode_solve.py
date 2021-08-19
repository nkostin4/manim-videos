import numpy as np
from scipy.integrate import odeint

# Numerically solve ODE
# Define constants
a = 0.1; b = 0.1; c = 14

# Initial conditions
x_init_1 = 1.1; y_init_1 = 1.1; z_init_1 = 0.1
initial_state_1 = np.array([x_init_1, y_init_1, z_init_1])

# Create array of time values to study
t_init = 0; t_fin = 360; h = 0.02
t = np.arange(t_init, t_fin, h)

# Governing system of differential equations
def f(state, t):
    x, y, z = state
    return np.array([(-y) + (-z), x + a*y, b + z*(x - c)])

states = odeint(f, initial_state_1, t)

np.savetxt('roessler.csv', states, delimiter = ',')
