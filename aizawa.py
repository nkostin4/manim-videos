from manim import *
from scipy.integrate import odeint

# Numerically solve ODE
# Define constants
a = 0.95; b = 0.7; c = 0.6
d = 3.5; e = 0.25; g = 0.1

# Initial conditions
x_init_1 = 1.45e+00; y_init_1 = -1.25e-01; z_init_1 = 8.07e-01
initial_state_1 = np.array([x_init_1, y_init_1, z_init_1])

# Create array of time values to study
t_init = 0; t_fin = 420; h = 0.02
t = np.arange(t_init, t_fin, h)

# Governing system of differential equations
def f(state, t):
    x, y, z = state
    return np.array([(z - b)*x - d*y, d*x + (z - b)*y, c + a*z - ((z**3)/(3)) - ((x**2 + y**2)*(1 + e*z)) + g*z*(x**3)])

states = odeint(f, initial_state_1, t)

class IntroText(Scene):
    
    def construct(self):
        text=MathTex("\\text{The Aizawa Attractor}").scale(2)
        text.set_color_by_gradient(WHITE, BLUE, RED)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        self.wait()

class Thumbnail(ThreeDScene):
    
    def construct(self):

        axes = ThreeDAxes()
        
        x_coords = 1.9*states[:, 0]
        y_coords = 1.9*states[:, 1]
        z_coords = 1.9*states[:, 2] - 0.94

        def coord(x,y,z):
            return np.array([x,y,z])
        
        self.tuples = list(zip(x_coords,y_coords,z_coords))
        
        trajectory = VMobject(stroke_width=1.45)
        trajectory.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples]])
        
        # self.add(axes)
        self.set_camera_orientation(phi=PI/2, theta=2*PI, distance = 2)
        self.add(trajectory)

        text3=MathTex("\\text{Aizawa}").scale(8)
        text3.set_color(RED)
        self.add_fixed_in_frame_mobjects(text3)
        self.wait(2)
        
class AizawaRotate(ThreeDScene):

    def construct(self):           
        
        axes = ThreeDAxes()
        
        x_coords = 1.1*states[:, 0]
        y_coords = 1.1*states[:, 1]
        z_coords = 1.1*states[:, 2] - 0.94

        def coord(x,y,z):
            return np.array([x,y,z])
        
        self.tuples = list(zip(x_coords,y_coords,z_coords))
        
        trajectory = VMobject(stroke_width=0.85)
        trajectory.set_color(WHITE)
        trajectory.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples]])
        
        # self.add(axes)
        self.set_camera_orientation(phi=PI/2, theta=2*PI, distance = 2)
        self.play(Create(trajectory), run_time=36)
        # self.add(trajectory)
        self.wait(2)
        self.begin_ambient_camera_rotation(about = 'phi', rate = 2*PI/40)
        self.wait(20)
        self.stop_ambient_camera_rotation(about = 'phi')
        self.wait()
        self.play(FadeOut(trajectory), run_time = 2)
