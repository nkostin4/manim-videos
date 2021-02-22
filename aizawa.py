from manim import *
from scipy.integrate import odeint

# Numerically solve ODE
# Define constants
a = 0.95; b = 0.7; c = 0.6
d = 3.5; e = 0.25; f = 0.1

# Initial conditions
x_init_1 = 0.1; y_init_1 = 0.1; z_init_1 = 0.1
initial_state_1 = np.array([x_init_1, y_init_1, z_init_1])

# Create array of time values to study
t_init = 0; t_fin = 60; h = 0.02
t = np.arange(t_init, t_fin, h)

# Governing system of differential equations
def f(state, t):
    x, y, z = state
    return np.array([sigma*(y - x), x*(rho - z) - y, x*y - beta*z])
    return np.array([(z - b)*x - d*y, d*x + (z - b)*y, c + a*z - ((z**3)/(3)) - ((x**2 + y**2)*(1 + e*z)) + f*z*(x**3)])

states_1 = odeint(f, initial_state_1, t)
        
class SimpleAizawa(ThreeDScene):
    CONFIG = {
        'x_min' : -100,
        'x_max' : 100,
        
        'y_min' : -100,
        'y_max' : 100,
        
        'z_min' : -100,
        'z_max' : 100,
        
        'exclude_zero_label' : True,
        
        'axes_color': WHITE,
        
        'stroke_width' : 0.02
    }
        
    def construct(self):           
        
        axes = ThreeDAxes()
        
        x_coords = 0.149*states[:, 0]
        y_coords = 0.149*states[:, 1]
        z_coords = 0.149*states[:, 2] - 3.6
        
        def coord(x,y,z):
            return np.array([x,y,z])
        
        self.tuples = list(zip(x_coords,y_coords,z_coords))
        
        trajectory = VMobject()
        trajectory.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples]])
        
        # self.add(axes)
        self.set_camera_orientation(phi=PI/2, theta=PI, distance = 30)
        self.begin_ambient_camera_rotation(rate=PI/36)
        self.play(ShowCreation(trajectory), run_time=20)
        self.stop_ambient_camera_rotation()
        self.wait(4)
        self.play(
            FadeOut(trajectory),
            run_time = 2
        )
