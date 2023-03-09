from manim import *
from scipy.integrate import odeint
# config.background_color = "#FF00BF"
config.background_color = "#00004F"

# Define constants
a = 0.2; b = 0.2; c = 5.7

# Initial conditions
xinit1 = 2.144246637147772105e+01; yinit1 = -1.671644998751870559e-01; zinit1 = 9.411339305791083021e+00
initialstate1 = np.array([0.21*xinit1 - 0.6, 0.21*yinit1, 0.21*zinit1 - 1.8])

# Create array of time values to study
tinit = 0; tfin = 240; h = 0.02
t = np.arange(tinit, tfin, h)

# Governing system of differential equations
def f(state, t):
    x, y, z = state
    return np.array([-y + (-z), x + a*y, b + z*(x - c)])

# Governing system of differential equations (again)
# For new a, b, and c values
def g(statenew, tnew):
    xnew, ynew, znew = statenew
    return np.array([-ynew + (-znew), xnew + 0.1*ynew, 0.1 + znew*(xnew - 14)])

states = odeint(f, initialstate1, t)
statesnew = odeint(g, initialstate1, t)

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

        text3=MathTex("\\text{Rössler}").scale(8)
        text3.set_color(RED)
        frame = SurroundingRectangle(text3, buff=0.2)
        self.add_fixed_in_frame_mobjects(text3)
        self.wait(2)

class IntroText(Scene):

    def construct(self):
        introtext=MathTex("\\text{The Rössler Attractor}").scale(2)
        introtext.set_color_by_gradient(WHITE, BLUE, RED)
        self.play(Write(introtext))
        self.wait(2)
        self.play(FadeOut(introtext))
        self.wait()

class IntroTextRU(Scene):

    def construct(self):
        introtextru=MathTex("\\text{Аттрактор Рёсслера}").scale(2)
        introtextru.set_color_by_gradient(WHITE, BLUE, RED)
        self.play(Write(introtextru))
        self.wait(2)
        self.play(FadeOut(introtextru))
        self.wait()

class RoesslerSystem(Scene):

    def construct(self):
        text1 = MathTex(r'\text{The equations of the Rössler system are}').shift(2.8*UP)
        xyzeqns = MathTex(r'\frac{dx}{dt} &= -y - z\\ \frac{dy}{dt} &= x + ay\\ \frac{dz}{dt} &= b + z(x - c)').shift(0.4*UP)
        brace1 = Brace(xyzeqns, LEFT)
        text2 = MathTex("\\text{Roessler studied the chaotic attractor with }").shift(2*DOWN)
        text3 = MathTex("a = 0.2 \\text{, } b = 0.2 \\text{, and } c = 5.7.").next_to(text2, DOWN)

        self.play(Write(text1))
        self.play(Write(xyzeqns), Write(brace1))
        self.play(Write(text2), Write(text3))
        self.wait(3)

class RoesslerSystemRU(Scene):

    def construct(self):
        atext1ru = Text('Система дифференциальных уравнений Рёсслера').scale(0.8).shift(2.8*UP)
        btext1ru = Text('Дифференциальные уравнения Рёсслера являются').scale(0.8).shift(2.8*UP)
        xyzeqnsru = MathTex(r'\frac{dx}{dt} &= -y - z\\ \frac{dy}{dt} &= x + ay\\ \frac{dz}{dt} &= b + z(x - c)').shift(0.4*UP)
        brace1ru = Brace(xyzeqnsru, LEFT)
        text2ru = Text('Сам Рёсслер изучал систему при постоянных').scale(0.8).shift(2*DOWN)
        atext3ru = MathTex("a = 0.2 \\text{, } b = 0.2,").next_to(text2ru, DOWN).shift(1.4*LEFT)
        btext3ru = Text(' и ').next_to(atext3ru, RIGHT).scale(0.75)
        ctext3ru = MathTex("c = 5.7").next_to(btext3ru, RIGHT)

        self.play(Write(btext1ru))
        self.play(Write(xyzeqnsru), Write(brace1ru))
        self.play(Write(text2ru), Write(atext3ru), Write(btext3ru), Write(ctext3ru))
        self.wait(3)

class RoesslerSystemCont(Scene):

    def construct(self):
        textc1 = MathTex(r'\text{The equations of the Rössler system are}').shift(2.8*UP)
        xyzeqnsc = MathTex(r'\frac{dx}{dt} &= -y - z\\ \frac{dy}{dt} &= x + ay\\ \frac{dz}{dt} &= b + z(x - c)').shift(0.4*UP)
        bracec1 = Brace(xyzeqnsc, LEFT)
        textc2 = MathTex(r'\text{Rössler studied the chaotic attractor with }').shift(2*DOWN)
        abcrvalsc = MathTex("a = 0.2 \\text{, } b = 0.2 \\text{, and } c = 5.7.").next_to(textc2, DOWN)
        textc3 = MathTex(r'\text{However, it is also common to use }').shift(2*DOWN)
        abccvalsc = MathTex("a = 0.1 \\text{, } b = 0.1 \\text{, and } c = 14.").next_to(textc3, DOWN)
        copiedtext = VGroup(xyzeqnsc, bracec1, textc2, abcrvalsc)

        self.add(textc1, xyzeqnsc, bracec1, textc2, abcrvalsc)
        self.wait(4)
        self.play(FadeOut(textc1))
        self.play(copiedtext.animate.shift(1.4*UP))
        self.play(Write(textc3), Write(abccvalsc))
        self.wait(4)

class RoesslerSystemContRU(Scene):

    def construct(self):
        atextc1ru = Text('Система дифференциальных уравнений Рёсслера').scale(0.8).shift(2.8*UP)
        btextc1ru = Text('Дифференциальные уравнения Рёсслера являются').scale(0.8).shift(2.8*UP)
        xyzeqnscru = MathTex(r'\frac{dx}{dt} &= -y - z\\ \frac{dy}{dt} &= x + ay\\ \frac{dz}{dt} &= b + z(x - c)').shift(0.4*UP)
        bracec1ru = Brace(xyzeqnscru, LEFT)
        textc2ru = Text('Сам Рёсслер изучал систему при постоянных').scale(0.8).shift(2*DOWN)
        atextc3ru = MathTex("a = 0.2 \\text{, } b = 0.2,").next_to(textc2ru, DOWN).shift(1.4*LEFT)
        btextc3ru = Text(' и ').next_to(atextc3ru, RIGHT).scale(0.75)
        ctextc3ru = MathTex("c = 5.7,").next_to(btextc3ru, RIGHT)
        textc4ru = Text('но также часто используются и значения').scale(0.8).shift(2*DOWN)
        atextc5ru = MathTex(r'a = 0.1 \text{, } b = 0.1,').next_to(textc4ru, DOWN).shift(1.4*LEFT)
        btextc5ru = Text(' и ').next_to(atextc5ru).scale(0.75)
        ctextc5ru = MathTex("c = 14.").next_to(btextc5ru, RIGHT)
        copiedtextru = VGroup(xyzeqnscru, bracec1ru, textc2ru, atextc3ru, btextc3ru, ctextc3ru)

        self.add(btextc1ru, xyzeqnscru, bracec1ru, textc2ru, atextc3ru, btextc3ru, ctextc3ru)
        self.wait(4)
        self.play(FadeOut(btextc1ru))
        self.play(copiedtextru.animate.shift(1.4*UP))
        self.play(Write(textc4ru), Write(atextc5ru), Write(btextc5ru), Write(ctextc5ru))
        self.wait(4)

class OttoRoessler(Scene):

    def construct(self):
        otto = ImageMobject("otto.jpg").scale(1)
        otto.to_edge(RIGHT, buff = 1)
        otto0 = MathTex(r'\text{Otto Rössler}').shift(4.0*LEFT).shift(2.0*UP)
        otto1 = MathTex(r'\text{Famous German biochemist}').next_to(otto0, 4*DOWN).scale(0.6)

        self.add(otto)
        self.add(otto0, otto1)
        self.wait(4)

class OttoRoesslerRU(Scene):

    def construct(self):
        otto = ImageMobject("otto.jpg").scale(1)
        otto.to_edge(RIGHT, buff = 1)
        otto0ru = Text('Отто Рёсслер').shift(4.0*LEFT).shift(2.0*UP)
        otto1ru = Text('известный немецкий биохимик').next_to(otto0ru, 4*DOWN).scale(0.5)

        self.add(otto)
        self.add(otto0ru, otto1ru)
        self.wait(4)

class RoesslerRotate(ThreeDScene):

    def construct(self):

        xyzeqnsrotate = MathTex(r'\dot{x} &= -y - z\\ \dot{y} &= x + 0.2y\\ \dot{z} &= 0.2 + z(x - 5.7)').scale(0.8)
        xyzeqnsrotate.shift(5*LEFT)
        xyzeqnsrotate.shift(2.5*UP)

        xeqnrotate = MathTex(r'x = ').shift(4*RIGHT).shift(0.05*DOWN)
        yeqnrotate = MathTex(r'y = ').next_to(xeqnrotate, 1.38*DOWN)
        zeqnrotate = MathTex(r'z = ').next_to(yeqnrotate, 1.15*DOWN)

        axes = ThreeDAxes()

        x_coords = 0.21*states[:, 0] - 0.6
        y_coords = 0.21*states[:, 1]
        z_coords = 0.21*states[:, 2] - 1.8

        def coord(x,y,z):
            return np.array([x,y,z])

        self.tuples = list(zip(x_coords,y_coords,z_coords))

        trajectory = VMobject(stroke_width=2.00)
        trajectory.set_color(WHITE)
        trajectory.set_points_smoothly([*[coord(x,y,z) for x,y,z in self.tuples]])

        xdecimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).shift(5.3*RIGHT)
        ydecimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(xdecimal, DOWN)
        zdecimal = DecimalNumber(0, show_ellipsis = False, num_decimal_places = 3, include_sign = True).next_to(ydecimal, DOWN)

        xdecimal.add_updater(lambda d: d.set_value(trajectory.get_end()[0]))
        ydecimal.add_updater(lambda d: d.set_value(trajectory.get_end()[1]))
        zdecimal.add_updater(lambda d: d.set_value(trajectory.get_end()[2]))

        # decimals = VGroup(xdecimal, ydecimal, zdecimal)

        # self.add(axes)

        self.set_camera_orientation(phi = 2.5*PI/6, theta = 19*PI/12, distance = 4.6)

        self.add_fixed_in_frame_mobjects(xyzeqnsrotate)
        self.add_fixed_in_frame_mobjects(xeqnrotate, yeqnrotate, zeqnrotate)
        self.add_fixed_in_frame_mobjects(xdecimal, ydecimal, zdecimal)
        # GitHub issue 1884
        xdecimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        ydecimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))
        zdecimal.add_updater(lambda v: self.add_fixed_in_frame_mobjects(v))


        self.play(Create(trajectory), run_time=40)
        # self.add(trajectory)
        self.wait(4)
        self.begin_ambient_camera_rotation(about = 'theta', rate = 2*PI/40)
        self.wait(40)
        self.stop_ambient_camera_rotation(about = 'theta')
        self.wait()
        self.play(FadeOut(trajectory), run_time = 2)

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
        xcoordsnew = 0.16*statesnew[:, 0] - 0.6
        ycoordsnew = 0.16*statesnew[:, 1]
        zcoordsnew = 0.16*statesnew[:, 2] - 2.2

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
