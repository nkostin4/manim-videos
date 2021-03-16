from manim import *

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
