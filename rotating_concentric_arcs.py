from manim import *
config.frame_height = 8
config.frame_width = 8*(16/9)
# config.background_color = "#040080"

class Thumbnail(Scene):

    def construct(self):

        rotating = Tex(r"\text{Rotating}").scale(5.4).set_color("#FFFFFF")
        concentric = Tex(r"\text{Concentric}").scale(5.4).set_color("#0000FF")
        arcs = Tex(r"\text{Arcs}").scale(5.4).set_color("#FF0000")
        circle = Circle(color=GOLD, stroke_width=36).scale(6.90)
        VGroup(rotating, concentric, arcs).arrange(DOWN)
        self.add(circle)
        self.play(FadeIn(rotating), FadeIn(concentric, shift=DOWN), FadeIn(arcs, shift=4*DOWN))
        self.wait()


class Intro(Scene):

    def construct(self):

        title = Tex(r"\text{Rotating Concentric Arcs}").scale(1.4)
        top = Tex(r"\text{In the following animations, the frequency}").scale(1)
        middle = Tex(r"\text{of rotation of each concentric half-circle}").scale(1)
        bottom = Tex(r"\text{is proportional to its radius.}").scale(1)
        visit = Tex(r"\text{Visit }\texttt{https://github.com/nkostin4/manim-videos}\text{ for the source code}").shift(2*(16/9)*DOWN).scale(0.8)
        VGroup(top, middle, bottom).arrange(DOWN)

        self.play(FadeIn(title))
        self.wait(2)
        self.play(title.animate.shift(3*LEFT + 2*(16/9)*UP))
        self.play(FadeIn(top), FadeIn(middle, shift=DOWN), FadeIn(bottom, shift=4*DOWN))
        self.wait(4)
        self.play(FadeIn(visit))
        self.wait(1.2)
        self.play(FadeOut(title), FadeOut(top), FadeOut(middle), FadeOut(bottom))


class ThreeColorsText(Scene):

    def construct(self):

        text = Tex(r"\text{Three Colors}").scale(49)
        text.set_color_by_gradient(WHITE, BLUE, RED)
        self.play(FadeIn(text))
        self.wait(2.4)
        self.play(FadeOut(text))
        self.wait(1)

class ThreeColorsRotating(Scene):

    def construct(self):

        arcs = VGroup()

        radii = np.linspace(2, 100, 50)
        colors = [BLUE, RED, WHITE]

        for i in range(np.size(radii)):
            bin_alter = (len(colors) - i) % 3
            # arc = Arc(radius = radii[i], angle = TAU/2, stroke_width=900, color=colors[bin_alter])
            arc = ParametricFunction(lambda u: np.array([radii[i]*np.cos(u), radii[i]*np.sin(u), 0]), color=colors[bin_alter], stroke_width=63, t_range = np.array([0, PI, 0.01]))
            # arc = ParametricFunction(lambda u: [radii[i]*np.cos(u), radii[i]*np.sin(u), 0], t_min = 0, t_max = PI, stroke_width = 60, color=colors[bin_alter])
            arcs.add(arc)

        self.play(Write(arcs))
        # self.add(arcs)
        self.wait(1)

        # self.play(*[(Rotating(j, about_point = ORIGIN, radians = 2*j.get_arc_length(), rate_function = linear, run_time=400)) for j in arcs])
        self.play(*[(Rotating(j, about_point = ORIGIN, radians = 2*PI*(np.linalg.norm(j.get_last_point())), rate_function = linear, run_time=100)) for j in arcs])

        self.wait(4)

class TwoColorsText(Scene):

    def construct(self):

        text = Tex(r"\text{Two Colors}").scale(49)
        text.set_color_by_gradient(PINK, GREEN)
        self.play(FadeIn(text))
        self.wait(2.4)
        self.play(FadeOut(text))
        self.wait(1)

class TwoColorsRotating(Scene):

    def construct(self):

        arcs = VGroup()

        radii = np.linspace(2, 100, 50)
        colors = [GREEN, PINK]

        for i in range(np.size(radii)):
            bin_alter = (len(colors) - i) % 2
            arc = ParametricFunction(lambda u: np.array([radii[i]*np.cos(u), radii[i]*np.sin(u), 0]), color=colors[bin_alter], stroke_width=63, t_range = np.array([0, PI, 0.01]))
            arcs.add(arc)

        self.play(Write(arcs))
        self.wait(1)

        self.play(*[(Rotating(j, about_point = ORIGIN, radians = 2*PI*(np.linalg.norm(j.get_last_point())), rate_function = linear, run_time=100)) for j in arcs])

        self.wait(4)
