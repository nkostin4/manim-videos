from manim import *

class FirstRotating(ZoomedScene):
    CONFIG = {
                "zoomed_factor": 0.1
            }

    def construct(self):
    
        arcs = VGroup()
    
        radii = np.linspace(2, 100, 50)
        colors = [RED, BLUE]
        
        for i in range(np.size(radii)):
            bin_alter = (len(colors) - i) % 2
            arc = Arc(radius = radii[i], angle = TAU/2, stoke_width=4, color=colors[bin_alter])
            arcs.add(arc)
            
        self.play(Write(arcs))
        self.wait(1)
        
        # self.play(*[(Rotating(j, about_point = ORIGIN, radians = 26.315789*PI*j.get_arc_length(), rate_function = linear, run_time=200)) for j in arcs])
        self.play(*[(Rotating(j, about_point = ORIGIN, radians = 2*j.get_arc_length(), rate_function = linear, run_time=50)) for j in arcs])
        
        self.wait()
