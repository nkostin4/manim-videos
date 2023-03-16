from manim import *
from scipy.integrate import odeint
# config.background_color = "#FF00BF"
config.background_color = "#00004F"

# Define constants
a = 0.2; b = 0.2; c = 5.7

# Initial conditions
xinit1 = 2.144246637147772105e+01; yinit1 = -1.671644998751870559e-01; zinit1 = 9.411339305791083021e+00
initialstate1 = np.array([0.21*xinit1 - 0.6, 0.21*yinit1, 0.21*zinit1 - 1.8])
# initial_state_4 = np.array([0.16*(1.143e+01) - 0.6, 0.16*(-1.142e+01), 0.16*(0.001) - 2.2])
# initial_state_5 = np.array([0.16*(1.144e+01) - 0.6, 0.16*(-1.141e+01), 0.16*(0.001) - 2.2])
# initial_state_6 = np.array([0.16*(1.145e+01) - 0.6, 0.16*(-1.140e+01), 0.16*(0.001) - 2.2])
initial_state_4 = np.array([1.143e+01, -1.142e+01, 0.001])
initial_state_5 = np.array([1.144e+01, -1.141e+01, 0.001])
initial_state_6 = np.array([1.145e+01, -1.140e+01, 0.001])

# Create array of time values to study
tinit = 0; tfin = 240; h = 0.02
t = np.arange(tinit, tfin, h)
prolonged = np.arange(0, 3600, 0.02) # prolonged time array for more analysis

# Governing system of differential equations
def f(state, t):
    x, y, z = state
    return np.array([-y + (-z), x + a*y, b + z*(x - c)])

# Governing system of differential equations (again)
# For new a, b, and c values
def g(statenew, tnew):
    xnew, ynew, znew = statenew
    return np.array([-ynew + (-znew), xnew + 0.1*ynew, 0.1 + znew*(xnew - 14)])

astates = odeint(f, initialstate1, t)
bstates = odeint(g, initialstate1, t)
dstates = odeint(g, initialstate1, prolonged)

ostates = odeint(g, initial_state_4, t)
pstates = odeint(g, initial_state_5, t)
qstates = odeint(g, initial_state_6, t)

class Thumbnail(ThreeDScene):

    def construct(self):

        axes = ThreeDAxes()

        x_coords = 0.30*cstates[:, 0] - 0.6
        y_coords = 0.30*cstates[:, 1]
        z_coords = 0.30*cstates[:, 2] - 3.20

        def coord(x,y,z):
            return np.array([x,y,z])

        self.tuples = list(zip(x_coords,y_coords,z_coords))

        trajectory = VMobject(stroke_width=0.45)
        trajectory.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples]])

        # self.add(axes)
        self.set_camera_orientation(phi=PI/2, theta=2*PI, distance = 2)
        self.add(trajectory)

        text3=MathTex("\\text{Rössler}").scale(8)
        text3.set_color(RED)
        frame = SurroundingRectangle(text3, buff=0.2)
        self.add_fixed_in_frame_mobjects(text3)
        self.wait(2)

class IntroText(Scene):

    def construct(self):
        intro = MathTex("\\text{The Rössler Attractor}").scale(2).set_color_by_gradient(WHITE, BLUE, RED)
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))

class IntroTextRU(Scene):

    def construct(self):
        intro_ru = MathTex("\\text{Аттрактор Рёсслера}").scale(2).set_color_by_gradient(WHITE, BLUE, RED)
        self.play(Write(intro_ru))
        self.wait(2)
        self.play(FadeOut(intro_ru))

class RoesslerSystem(Scene):

    def construct(self):
        main_text = MathTex(r'\text{The equations of the Rössler system are}').shift(2.8*UP)
        eqns = MathTex(r'\frac{dx}{dt} &= -y - z\\ \frac{dy}{dt} &= x + ay\\ \frac{dz}{dt} &= b + z(x - c)').shift(0.4*UP)
        brace = Brace(eqns, LEFT)
        params_text = MathTex("\\text{Roessler studied the chaotic attractor with }").shift(2*DOWN)
        params = MathTex("a = 0.2 \\text{, } b = 0.2 \\text{, and } c = 5.7.").next_to(params_text, DOWN)

        self.play(Write(main_text))
        self.play(Write(eqns), Write(brace))
        self.play(Write(params_text), Write(params))
        self.wait(3)

class RoesslerSystemRU(Scene):

    def construct(self):
        # Text('Система дифференциальных уравнений Рёсслера')
        main_text_ru = Text('Дифференциальные уравнения Рёсслера являются').scale(0.8).shift(2.8*UP)
        eqns_ru = MathTex(r'\frac{dx}{dt} &= -y - z\\ \frac{dy}{dt} &= x + ay\\ \frac{dz}{dt} &= b + z(x - c)').shift(0.4*UP)
        brace_ru = Brace(eqns_ru, LEFT)
        params_text_ru = Text('Сам Рёсслер изучал систему при постоянных').scale(0.8).shift(2*DOWN)
        params_ru = MathTex("a = 0.2 \\text{, } b = 0.2,").next_to(params_text_ru, DOWN).shift(1.4*LEFT)
        and_ru = Text(' и ').next_to(params_ru, RIGHT).scale(0.75)
        c_ru = MathTex("c = 5.7").next_to(and_ru, RIGHT)

        self.play(Write(main_text_ru))
        self.play(Write(eqns_ru), Write(brace_ru))
        self.play(Write(params_text_ru), Write(params_ru), Write(and_ru), Write(c_ru))
        self.wait(3)

class RoesslerSystemCont(Scene):

    def construct(self):
        main_text_cont = MathTex(r'\text{The equations of the Rössler system are}').shift(2.8*UP)
        eqns_cont = MathTex(r'\frac{dx}{dt} &= -y - z\\ \frac{dy}{dt} &= x + ay\\ \frac{dz}{dt} &= b + z(x - c)').shift(0.4*UP)
        brace_cont = Brace(eqns_cont, LEFT)
        roessler_params_text = MathTex(r'\text{Rössler studied the chaotic attractor with }').shift(2*DOWN)
        roessler_params = MathTex("a = 0.2 \\text{, } b = 0.2 \\text{, and } c = 5.7.").next_to(roessler_params_text, DOWN)
        alt_params_text = MathTex(r'\text{However, it is also common to use }').shift(2*DOWN)
        alt_params = MathTex("a = 0.1 \\text{, } b = 0.1 \\text{, and } c = 14.").next_to(alt_params_text, DOWN)
        copiedtext = VGroup(eqns_cont, brace_cont, roessler_params_text, roessler_params)

        self.add(main_text_cont, eqns_cont, brace_cont, roessler_params_text, roessler_params)
        self.wait(4)
        self.play(FadeOut(main_text_cont))
        self.play(copiedtext.animate.shift(1.4*UP))
        self.play(Write(alt_params_text), Write(alt_params))
        self.wait(4)

class RoesslerSystemContRU(Scene):

    def construct(self):
        # Text('Система дифференциальных уравнений Рёсслера')
        main_text_cont_ru = Text('Дифференциальные уравнения Рёсслера являются').scale(0.8).shift(2.8*UP)
        eqns_cont_ru = MathTex(r'\frac{dx}{dt} &= -y - z\\ \frac{dy}{dt} &= x + ay\\ \frac{dz}{dt} &= b + z(x - c)').shift(0.4*UP)
        brace_cont_ru = Brace(eqns_cont_ru, LEFT)
        roessler_params_text_ru = Text('Сам Рёсслер изучал систему при постоянных').scale(0.8).shift(2*DOWN)
        roessler_params_ru = MathTex("a = 0.2 \\text{, } b = 0.2,").next_to(roessler_params_text_ru, DOWN).shift(1.4*LEFT)
        and1_ru = Text(' и ').next_to(roessler_params_ru, RIGHT).scale(0.75)
        c1_ru = MathTex("c = 5.7").next_to(and1_ru, RIGHT)
        alt_params_text_ru = Text('но также часто используются и значения').scale(0.8).shift(2*DOWN)
        alt_params_ru = MathTex(r'a = 0.1 \text{, } b = 0.1,').next_to(alt_params_text_ru, DOWN).shift(1.4*LEFT)
        and2_ru = Text(' и ').next_to(alt_params_ru).scale(0.75)
        c2_ru = MathTex("c = 14.").next_to(and2_ru, RIGHT)
        copiedtext_ru = VGroup(eqns_cont_ru, brace_cont_ru, roessler_params_text_ru, roessler_params_ru, and1_ru, c1_ru)

        self.add(main_text_cont_ru, eqns_cont_ru, brace_cont_ru, roessler_params_text_ru, roessler_params_ru, and1_ru, c1_ru)
        self.wait(4)
        self.play(FadeOut(main_text_cont_ru))
        self.play(copiedtext_ru.animate.shift(1.4*UP))
        self.play(Write(alt_params_text_ru), Write(alt_params_ru), Write(and2_ru), Write(c2_ru))
        self.wait(4)

class OttoRoessler(Scene):

    def construct(self):
        otto = ImageMobject("otto.jpg").scale(1)
        otto.to_edge(RIGHT, buff = 1)
        otto_roessler = MathTex(r'\text{Otto Rössler}').shift(4.0*LEFT).shift(2.0*UP)
        biochemist = MathTex(r'\text{Famous German biochemist}').next_to(otto_roessler, 4*DOWN).scale(0.6)

        self.add(otto)
        self.add(otto_roessler, biochemist)
        self.wait(4)

class OttoRoesslerRU(Scene):

    def construct(self):
        otto_ru = ImageMobject("otto.jpg").scale(1)
        otto_ru.to_edge(RIGHT, buff = 1)
        otto_roessler_ru = Text('Отто Рёсслер').shift(4.0*LEFT).shift(2.0*UP)
        biochemist_ru = Text('известный немецкий биохимик').next_to(otto_roessler_ru, 4*DOWN).scale(0.5)

        self.add(otto_ru)
        self.add(otto_roessler_ru, biochemist_ru)
        self.wait(4)

class RoesslerRotate(ThreeDScene):

    def construct(self):

        # Using (a, b, c) = (0.2, 0.2, 5.7)
        xyzeqnsrotate = MathTex(r'\dot{x} &= -y - z\\ \dot{y} &= x + 0.2y\\ \dot{z} &= 0.2 + z(x - 5.7)').scale(0.8).shift(5*LEFT).shift(2.5*UP)

        # to be used later
        # with DecimalNumber
        xeqnrotate = MathTex(r'x = ').shift(4*RIGHT).shift(0.05*DOWN)
        yeqnrotate = MathTex(r'y = ').next_to(xeqnrotate, 1.38*DOWN)
        zeqnrotate = MathTex(r'z = ').next_to(yeqnrotate, 1.15*DOWN)

        axes = ThreeDAxes()

        # Get x, y, and z coordinates
        # from states numpy array from earlier
        x_coords = 0.21*astates[:, 0] - 0.6
        y_coords = 0.21*astates[:, 1]
        z_coords = 0.21*astates[:, 2] - 1.8

        def coord(x,y,z):
            return np.array([x,y,z])

        self.tuples = list(zip(x_coords,y_coords,z_coords))

        trajectory = VMobject(stroke_width=2.00)
        trajectory.set_color(WHITE)
        trajectory.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples]])

        sphere = Surface(lambda u, v: np.array([ 0.05*np.cos(u)*np.cos(v), 0.05*np.cos(u)*np.sin(v), 0.05*np.sin(u) ]), v_range = [0, TAU], u_range = [-PI/2, PI/2], fill_color = RED, fill_opacity = 0.3)
        # Here we go. This sphere traces out the trajectory as it grows
        # it works. it is not pretty, but it definitely works
        # first timestamp at 11^2
        # it's what I do

        # Draw x, y, and z axes
        # this part is totally dumb
        # like it's beyond the pale that I can't think of a better soln
        xtempold = 0.21*np.array([[-1, 0, 0], [20, 0, 0]]) - np.array([[0.6, 0, 1.8], [0.6, 0, 1.8]])
        ytempold = 0.21*np.array([[0, -1, 0], [0, 20, 0]]) - np.array([[0.6, 0, 1.8], [0.6, 0, 1.8]])
        ztempold = 0.21*np.array([[0, 0, -1], [0, 0, 20]]) - np.array([[0.6, 0, 1.8], [0.6, 0, 1.8]])
        xaxisold = Line(xtempold.tolist()[0], xtempold.tolist()[1])
        yaxisold = Line(ytempold.tolist()[0], ytempold.tolist()[1])
        zaxisold = Line(ztempold.tolist()[0], ztempold.tolist()[1])
        xaxislabelold = MathTex(r'x').next_to(xaxisold.get_end(), RIGHT)
        yaxislabelold = MathTex(r'y').next_to(yaxisold.get_end(), RIGHT)
        zaxislabelold = MathTex(r'z').next_to(zaxisold.get_end(), RIGHT)

        xdecimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).shift(5.3*RIGHT)
        ydecimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(xdecimal, DOWN)
        zdecimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(ydecimal, DOWN)

        # use add_updater to get value for decimal numbers
        xdecimal.add_updater(lambda d: d.set_value((trajectory.get_end()[0] + 0.6)/0.21))
        ydecimal.add_updater(lambda d: d.set_value((trajectory.get_end()[1] + 0.0)/0.21))
        zdecimal.add_updater(lambda d: d.set_value((trajectory.get_end()[2] + 1.8)/0.21))
        # xdecimal.add_updater(lambda d: d.set_value(trajectory.get_end()[0]))
        # ydecimal.add_updater(lambda d: d.set_value(trajectory.get_end()[1]))
        # zdecimal.add_updater(lambda d: d.set_value(trajectory.get_end()[2]))

        def update_sphere(mob):
            mob.move_to(trajectory.get_end())

        # self.add(axes)

        # set camera orientation
        self.set_camera_orientation(phi = 2.5*PI/6, theta = 19*PI/12, distance = 4.6)

        sphere.add_updater(update_sphere)

        self.add_fixed_in_frame_mobjects(xyzeqnsrotate)
        self.add_fixed_in_frame_mobjects(xeqnrotate, yeqnrotate, zeqnrotate)
        self.add_fixed_in_frame_mobjects(xdecimal, ydecimal, zdecimal)
        # GitHub issue 1884
        xdecimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        ydecimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        zdecimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        # GitHub issue 1884 also
        self.add(xaxisold, yaxisold, zaxisold)
        self.add_fixed_orientation_mobjects(xaxislabelold, yaxislabelold, zaxislabelold)
        self.add(sphere)
        self.play(Create(trajectory), run_time=40)
        # self.add(trajectory) # uncomment to see end result
        self.wait(2)
        self.remove(xeqnrotate, yeqnrotate, zeqnrotate)
        self.remove(xdecimal, ydecimal, zdecimal)
        self.begin_ambient_camera_rotation(about = 'theta', rate = 2*PI/40)
        self.wait(40)
        self.stop_ambient_camera_rotation(about = 'theta')
        self.wait()
        self.play(FadeOut(trajectory), FadeOut(xaxisold), FadeOut(yaxisold), FadeOut(zaxisold), FadeOut(xaxislabelold), FadeOut(yaxislabelold), FadeOut(zaxislabelold), run_time = 2)

class RoesslerRotateNew(ThreeDScene):

    def construct(self):

        # Now using (a, b, c) = (0.1, 0.1, 14)
        xyzeqnsrotatenew = MathTex(r'\dot{x} &= -y - z\\ \dot{y} &= x + 0.1y\\ \dot{z} &= 0.1 + z(x - 14)').scale(0.8).shift(5*LEFT).shift(2.5*UP)

        # to be used later
        # with DecimalNumber
        xeqnrotatenew = MathTex(r'x = ').shift(4*RIGHT).shift(0.05*DOWN)
        yeqnrotatenew = MathTex(r'y = ').next_to(xeqnrotatenew, 1.38*DOWN)
        zeqnrotatenew = MathTex(r'z = ').next_to(yeqnrotatenew, 1.15*DOWN)

        axes = ThreeDAxes()

        # Get x, y, z coordinates
        # from statesnew numpy array from earlier
        xcoordsnew = 0.16*bstates[:, 0] - 0.6
        ycoordsnew = 0.16*bstates[:, 1]
        zcoordsnew = 0.16*bstates[:, 2] - 2.2

        def coord(x,y,z):
            return np.array([x,y,z])

        self.tuples = list(zip(xcoordsnew,ycoordsnew,zcoordsnew))

        trajectorynew = VMobject(stroke_width=2.00)
        trajectorynew.set_color(WHITE)
        trajectorynew.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples]])

        # Draw x, y, and z axes
        # this part is totally dumb
        # like it's beyond the pale that I can't think of a better soln
        xtemp = 0.16*np.array([[-1, 0, 0], [20, 0, 0]]) - np.array([[0.6, 0, 2.2], [0.6, 0, 2.2]])
        ytemp = 0.16*np.array([[0, -1, 0], [0, 20, 0]]) - np.array([[0.6, 0, 2.2], [0.6, 0, 2.2]])
        ztemp = 0.16*np.array([[0, 0, -1], [0, 0, 30]]) - np.array([[0.6, 0, 2.2], [0.6, 0, 2.2]])
        xaxis = Line(xtemp.tolist()[0], xtemp.tolist()[1])
        yaxis = Line(ytemp.tolist()[0], ytemp.tolist()[1])
        zaxis = Line(ztemp.tolist()[0], ztemp.tolist()[1])
        xaxislabel = MathTex(r'x').next_to(xaxis.get_end(), RIGHT)
        yaxislabel = MathTex(r'y').next_to(yaxis.get_end(), RIGHT)
        zaxislabel = MathTex(r'z').next_to(zaxis.get_end(), RIGHT)

        xdecimalnew = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).shift(5.3*RIGHT)
        ydecimalnew = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(xdecimalnew, DOWN)
        zdecimalnew = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(ydecimalnew, DOWN)

        # use add_updater to get value for decimal numbers
        xdecimalnew.add_updater(lambda d: d.set_value((trajectorynew.get_end()[0] + 0.6)/0.16))
        ydecimalnew.add_updater(lambda d: d.set_value((trajectorynew.get_end()[1] + 0.0)/0.16))
        zdecimalnew.add_updater(lambda d: d.set_value((trajectorynew.get_end()[2] + 2.2)/0.16))
        # xdecimalnew.add_updater(lambda d: d.set_value(trajectorynew.get_end()[0]))
        # ydecimalnew.add_updater(lambda d: d.set_value(trajectorynew.get_end()[1]))
        # zdecimalnew.add_updater(lambda d: d.set_value(trajectorynew.get_end()[2]))

        # self.add(axes)

        # set camera orientation
        self.set_camera_orientation(phi = 2.5*PI/6, theta = 19*PI/12, distance = 16)

        self.add_fixed_in_frame_mobjects(xyzeqnsrotatenew)
        self.add_fixed_in_frame_mobjects(xeqnrotatenew, yeqnrotatenew, zeqnrotatenew)
        self.add_fixed_in_frame_mobjects(xdecimalnew, ydecimalnew, zdecimalnew)
        # GitHub issue 1884
        xdecimalnew.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        ydecimalnew.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        zdecimalnew.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        # GitHub issue 1884 also 299 at 0223 also 303 at 0255 lmao also 303 at 2998
        self.add(xaxis, yaxis, zaxis)
        self.add_fixed_orientation_mobjects(xaxislabel, yaxislabel, zaxislabel)
        self.play(Create(trajectorynew), run_time=40)
        # self.add(trajectory) # uncomment to see end result
        self.wait(2)
        self.remove(xeqnrotatenew, yeqnrotatenew, zeqnrotatenew)
        self.remove(xdecimalnew, ydecimalnew, zdecimalnew)
        self.begin_ambient_camera_rotation(about = 'theta', rate = 2*PI/40)
        self.wait(40)
        self.stop_ambient_camera_rotation(about = 'theta')
        self.wait()
        self.play(FadeOut(trajectorynew), FadeOut(xaxis), FadeOut(yaxis), FadeOut(zaxis), FadeOut(xaxislabel), FadeOut(yaxislabel), FadeOut(zaxislabel), run_time = 2)

class RoesslerThree(ThreeDScene):

    def construct(self):

        # Now using three initial conditions
        threeeqns = MathTex(r'\dot{x} &= -y - z\\ \dot{y} &= x + 0.1y\\ \dot{z} &= 0.1 + z(x - 14)', color = ORANGE).scale(0.8).shift(5*LEFT).shift(2.5*UP)

        # ROFLMAO
        x1threeequals = MathTex(r'x = ', color = WHITE).shift(4*RIGHT).shift(2.5*UP)
        y1threeequals = MathTex(r'y = ', color = WHITE).next_to(x1threeequals, 1.38*DOWN)
        z1threeequals = MathTex(r'z = ', color = WHITE).next_to(y1threeequals, 1.15*DOWN)

        x2threeequals = MathTex(r'x = ', color = BLUE).shift(4*RIGHT).shift(0.0*DOWN)
        y2threeequals = MathTex(r'y = ', color = BLUE).next_to(x2threeequals, 1.38*DOWN)
        z2threeequals = MathTex(r'z = ', color = BLUE).next_to(y2threeequals, 1.15*DOWN)

        x3threeequals = MathTex(r'x = ', color = RED).shift(4*RIGHT).shift(2.5*DOWN)
        y3threeequals = MathTex(r'y = ', color = RED).next_to(x3threeequals, 1.38*DOWN)
        z3threeequals = MathTex(r'z = ', color = RED).next_to(y3threeequals, 1.15*DOWN)

        axes = ThreeDAxes()

        # get x, y, z coordinates for trajectory 1
        x1coords = 0.16*ostates[:, 0] - 0.6
        y1coords = 0.16*ostates[:, 1]
        z1coords = 0.16*ostates[:, 2] - 2.2

        # get x, y, z coordinates for trajectory 2
        x2coords = 0.16*pstates[:, 0] - 0.6
        y2coords = 0.16*pstates[:, 1]
        z2coords = 0.16*pstates[:, 2] - 2.2

        # get x, y, z coordinates for trajectory 3
        x3coords = 0.16*qstates[:, 0] - 0.6
        y3coords = 0.16*qstates[:, 1]
        z3coords = 0.16*qstates[:, 2] - 2.2

        # create a function to return numpy array given input coordinate
        def coord(x, y, z):
            return np.array([x, y, z])

        self.t1uples = list(zip(x1coords, y1coords, z1coords))
        self.t2uples = list(zip(x2coords, y2coords, z2coords))
        self.t3uples = list(zip(x3coords, y3coords, z3coords))

        t1rajectory = VMobject(stroke_width = 0.75).set_color(WHITE)
        t1rajectory.set_points_smoothly([*[coord(x, y, z) for x,y,z in self.t1uples]])
        t2rajectory = VMobject(stroke_width = 0.75).set_color(BLUE)
        t2rajectory.set_points_smoothly([*[coord(x, y, z) for x,y,z in self.t2uples]])
        t3rajectory = VMobject(stroke_width = 0.75).set_color(RED)
        t3rajectory.set_points_smoothly([*[coord(x, y, z) for x,y,z in self.t3uples]])

        # Draw x, y, and z axes
        # this part is totally dumb
        # like it's beyond the pale that I can't think of a better soln
        xthreetemp = 0.16*np.array([[-1, 0, 0], [20, 0, 0]]) - np.array([[0.6, 0, 2.2], [0.6, 0, 2.2]])
        ythreetemp = 0.16*np.array([[0, -1, 0], [0, 20, 0]]) - np.array([[0.6, 0, 2.2], [0.6, 0, 2.2]])
        zthreetemp = 0.16*np.array([[0, 0, -1], [0, 0, 30]]) - np.array([[0.6, 0, 2.2], [0.6, 0, 2.2]])
        xthreeaxis = Line(xthreetemp.tolist()[0], xthreetemp.tolist()[1]).set_color(ORANGE)
        ythreeaxis = Line(ythreetemp.tolist()[0], ythreetemp.tolist()[1]).set_color(ORANGE)
        zthreeaxis = Line(zthreetemp.tolist()[0], zthreetemp.tolist()[1]).set_color(ORANGE)
        xthreeaxislabel = MathTex(r'x').next_to(xthreeaxis.get_end(), RIGHT)
        ythreeaxislabel = MathTex(r'y').next_to(ythreeaxis.get_end(), RIGHT)
        zthreeaxislabel = MathTex(r'z').next_to(zthreeaxis.get_end(), RIGHT)

        # Yo
        x1decimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).shift(5.3*RIGHT).shift(2.5*UP)
        y1decimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(x1decimal, DOWN)
        z1decimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(y1decimal, DOWN)

        x2decimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).shift(5.3*RIGHT).shift(0.0*UP)
        y2decimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(x2decimal, DOWN)
        z2decimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(y2decimal, DOWN)

        x3decimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).shift(5.3*RIGHT).shift(2.5*DOWN)
        y3decimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(x3decimal, DOWN)
        z3decimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(y3decimal, DOWN)

        # use add_updater to get value for decimal numbers

        x1decimal.add_updater(lambda d: d.set_value((t1rajectory.get_end()[0] + 0.6)/0.16))
        y1decimal.add_updater(lambda d: d.set_value((t1rajectory.get_end()[1] + 0.0)/0.16))
        z1decimal.add_updater(lambda d: d.set_value((t1rajectory.get_end()[2] + 2.2)/0.16))

        x2decimal.add_updater(lambda d: d.set_value((t2rajectory.get_end()[0] + 0.6)/0.16))
        y2decimal.add_updater(lambda d: d.set_value((t2rajectory.get_end()[1] + 0.0)/0.16))
        z2decimal.add_updater(lambda d: d.set_value((t2rajectory.get_end()[2] + 2.2)/0.16))

        x3decimal.add_updater(lambda d: d.set_value((t3rajectory.get_end()[0] + 0.6)/0.16))
        y3decimal.add_updater(lambda d: d.set_value((t3rajectory.get_end()[1] + 0.0)/0.16))
        z3decimal.add_updater(lambda d: d.set_value((t3rajectory.get_end()[2] + 2.2)/0.16))

        # self.add(axes)

        # set camera orientation
        self.set_camera_orientation(phi = 2.5*PI/6, theta = 19*PI/12, distance = 16)

        self.add_fixed_in_frame_mobjects(threeeqns)
        self.add_fixed_in_frame_mobjects(x1threeequals, y1threeequals, z1threeequals, x2threeequals, y2threeequals, z2threeequals, x3threeequals, y3threeequals, z3threeequals)
        self.add_fixed_in_frame_mobjects(x1decimal, y1decimal, z1decimal, x2decimal, y2decimal, z2decimal, x3decimal, y3decimal, z3decimal)
        # GitHub issue 1884
        x1decimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        y1decimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        z1decimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        x2decimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        y2decimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        z2decimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        x3decimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        y3decimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        z3decimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        # GitHub issue 1884
        self.add(xthreeaxis, ythreeaxis, zthreeaxis)
        self.add_fixed_orientation_mobjects(xthreeaxislabel, ythreeaxislabel, zthreeaxislabel)
        # self.add(t1rajectory, t2rajectory, t3rajectory) # uncomment to see end result
        self.play(Create(t1rajectory), Create(t2rajectory), Create(t3rajectory), run_time=80)
        self.wait(10)
