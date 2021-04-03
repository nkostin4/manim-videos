from manim import *
config.frame_height = 80
config.frame_width = 80*(16/9)

class IntroText(Scene):
    
    def construct(self):
        
        title = MathTex("\\text{Osculating Circles}").scale(2)
        title.set_color_by_gradient(GOLD, GOLD)
        self.play(Write(title), run_time=0.8)
        self.wait(2)
        self.play(title.animate.shift(2.8*UP).scale(0.75), run_time=2)
        self.wait()

        top_text = MathTex("\\text{The }", "\\text{osculating circle } ", "\\text{of a }", "\\text{curve } C", "\\text{ at a given }", "\\text{point } P", "\\text{ is}")
        top_text[1].set_color(GOLD)
        top_text[3].set_color(BLUE)
        top_text[5].set_color(RED)
        middle_text = MathTex("\\text{the }", "\\text{circle }", "\\text{that has the same tangent as }", "C", "\\text{ at }", "\\text{ point } P")
        middle_text[1].set_color(GOLD)
        middle_text[3].set_color(BLUE)
        middle_text[5].set_color(RED)
        middle_text.shift(1.0*DOWN)
        bottom_text = MathTex("\\text{as well as the same curvature.}")
        bottom_text.shift(2.0*DOWN)

        self.play(FadeIn(top_text), FadeIn(middle_text), FadeIn(bottom_text))
        self.wait(3)
        self.play(FadeOut(top_text), FadeOut(middle_text), FadeOut(bottom_text))
        self.play(FadeOut(title))
        self.wait()

class CoolPicture(Scene):

    def construct(self):

        path = ParametricFunction(lambda t: [2*np.cos(t)+np.cos(2*t), 2*np.sin(t)-np.sin(2*t), 0], t_min=0, t_max=TAU, stroke_width=10, color=BLUE)

        self.add(path)

        def get_radius(t):
            return 4*np.sqrt(2)*np.sqrt(np.absolute(1-np.cos(3*t)))

        def get_center(t):
            f = np.array([2*np.cos(t)+np.cos(2*t),-2*np.sin(t)-2*np.sin(2*t),-2*np.cos(t)-4*np.cos(2*t)])
            g = np.array([2*np.sin(t)-np.sin(2*t),2*np.cos(t)-2*np.cos(2*t),-2*np.sin(t)+4*np.sin(2*t)])
            k = (f[1]*g[2] - f[2]*g[1])/((f[1]**2 + g[1]**2)**(3/2))
            x_c = (1/(k*np.sqrt(f[1]**2 + g[1]**2)))*(-g[1])
            y_c = (1/(k*np.sqrt(f[1]**2 + g[1]**2)))*(f[1])
            # x_center = ff[0] - ((ff[1]**2 + gg[1]**2)*gg[1])/(ff[1]*gg[2] - ff[2]*gg[1])
            # y_center = gg[0] + ((ff[1]**2 + gg[1]**2)*ff[1])/(ff[1]*gg[2] - ff[2]*gg[1])
            # x_center = ((ff[1]**2 + gg[1]**2)*gg[1])/(ff[1]*gg[2] - ff[2]*gg[1])
            # y_center = ((ff[1]**2 + gg[1]**2)*ff[1])/(ff[1]*gg[2] - ff[2]*gg[1])
            return [x_c, y_c]

        t_vals = np.linspace(0.01, 2*np.pi/3, 25)
        R = get_radius(t_vals)
        Q = get_center(t_vals)

        for i in range(np.size(t_vals)):
            circ = Circle(radius = R[i], color=GOLD).shift(Q[0][i], Q[1][i], 0)
            self.add(circ)

class AlmostTriangle(Scene):

    def construct(self):

        path = ParametricFunction(lambda t: [2*np.cos(t)+np.cos(2*t), 2*np.sin(t)-np.sin(2*t), 0], t_min=0, t_max=TAU, stroke_width=10, color=BLUE)

        moving_dot = Dot(radius=0.8, color=RED)
        moving_dot.move_to(path.point_from_proportion(0))

        t_offset = 0
        rate = 0.25

        def go_around(mob, dt):
            t_offset += (dt*rate)
            mob.move_to(path.point_from_proportion(self.t_offset % 1))

        self.curve = VGroup()
        self.curve.add(Line(self.curve_start,self.curve_start))

        def get_curve():
            last_line = self.curve[-1]

        # self.add(curve)
        # self.play(MoveAlongPath(moving_dot, curve), rate_func=linear, run_time=10)
        self.wait()
