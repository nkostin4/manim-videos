from manim import *

class IntroText(Scene):
    
    def construct(self):
        
        text = MathTex("\\text{Osculating Circles}").scale(2)
        text.set_color_by_gradient(WHITE, BLUE, RED)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
        self.wait()

class AlmostTriangle(Scene):

    def construct(self):
