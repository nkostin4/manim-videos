from manim import *

class FirstRotating(Scene):

    def construct(self):
    
        arcs = VGroup()
    
        radii = np.linspace(0.2, 3.8, 50)
        colors = [RED, BLUE]
        
        for i in range(50):
            bin_alter = (len(colors) - i) % 2
            arc = Arc(radius = radii[i], angle = TAU/2, stoke_width=4, color=colors[bin_alter])
            arcs.add(arc)
            
        self.play(Write(arcs))
        # self.play(GrowFromCenter(arcs))
        self.wait(1)
        
        # self.play(*[(Rotating(j, about_point = ORIGIN, radians = 26.315789*PI*j.get_arc_length(), rate_function = linear, run_time=200)) for j in arcs])
        # self.play(*[(Rotating(j, about_point = ORIGIN, radians = (get_arc_length())/j, rate_function = linear, run_time=200)) for j in arcs])
        self.play(*[(Rotating(j, about_point = ORIGIN, radians = 100*j.get_arc_length(), rate_function = linear, run_time=100)) for j in arcs])
        
        self.wait()
