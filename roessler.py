from manim import *
from scipy.integrate import odeint
config.background_color = "#0000FF"

# Numerically solve ODE
# Define constants
a = 0.2; b = 0.2; c = 5.7

# Initial conditions
x_init_1 = 2.144246637147772105e+01; y_init_1 = -1.671644998751870559e-01; z_init_1 = 9.411339305791083021e+00
initial_state_1 = np.array([0.21*x_init_1 - 0.6, 0.21*y_init_1, 0.21*z_init_1 - 1.8])

# Create array of time values to study
t_init = 0; t_fin = 520; h = 0.02
t = np.arange(t_init, t_fin, h)

# Governing system of differential equations
def f(state, t):
    x, y, z = state
    return np.array([-y + (-z), x + a*y, b + z*(x - c)])

states = odeint(f, initial_state_1, t)

class IntroText(Scene):
    
    def construct(self):
        text=MathTex("\\text{The R{\"o}ssler Attractor}").scale(2)
        text.set_color_by_gradient(WHITE, BLUE, RED)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        self.wait()

class Thumbnail(ThreeDScene):
    
    def construct(self):

        axes = ThreeDAxes()
        
        x_coords = 0.21*states[:, 0] - 0.6
        y_coords = 0.21*states[:, 1]
        z_coords = 0.21*states[:, 2] - 1.80

        def coord(x,y,z):
            return np.array([x,y,z])
        
        self.tuples = list(zip(x_coords,y_coords,z_coords))
        
        trajectory = VMobject(stroke_width=1.45)
        trajectory.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples]])
        
        # self.add(axes)
        self.set_camera_orientation(phi=PI/2, theta=2*PI, distance = 2)
        self.add(trajectory)

        text3=MathTex("\\text{R{\"o}ssler}").scale(8)
        text3.set_color(RED)
        frame = SurroundingRectangle(text3, buff=0.2)
        self.add_fixed_in_frame_mobjects(text3)
        self.wait(2)
        
class RoesslerRotate(ThreeDScene):

    def construct(self):           
        
        axes = ThreeDAxes()
        
        x_coords = 0.21*states[:, 0] - 0.6
        y_coords = 0.21*states[:, 1]
        z_coords = 0.21*states[:, 2] - 1.8

        def coord(x,y,z):
            return np.array([x,y,z])
        
        self.tuples = list(zip(x_coords,y_coords,z_coords))
        
        trajectory = VMobject(stroke_width=0.85)
        trajectory.set_color(WHITE)
        trajectory.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples]])
        
        # self.add(axes)
        self.set_camera_orientation(phi = 2.5*PI/6, theta = 19*PI/12, distance = 4.6)
        # self.play(Create(trajectory), run_time=5)
        self.add(trajectory)
        self.wait(4)
        # self.begin_ambient_camera_rotation(about = 'phi', rate = 2*PI/40)
        # self.wait(20)
        # self.stop_ambient_camera_rotation(about = 'phi')
        # self.wait()
        # self.play(FadeOut(trajectory), run_time = 2)

class RoesslerDot(ThreeDScene):

    def construct(self):           
        
        axes = ThreeDAxes()
        
        x_coords = 0.21*states[:, 0] - 0.6
        y_coords = 0.21*states[:, 1]
        z_coords = 0.21*states[:, 2] - 1.8

        def coord(x,y,z):
            return np.array([x,y,z])
        
        self.tuples = list(zip(x_coords,y_coords,z_coords))
        trajectory = VMobject()
        trajectory.set_points_as_corners([*[coord(x,y,z) for x,y,z in self.tuples]])

        path = VMobject(stroke_width=0.85)
        path.set_color(WHITE)
        dot = Dot()

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, dot)
        
        self.set_camera_orientation(phi = 2.5*PI/6, theta = 19*PI/12, distance = 4.6)

        self.play(
                MoveAlongPath(dot, trajectory, rate_func=rate_functions.ease_in_sine), run_time=10
            )
        self.wait(4)
