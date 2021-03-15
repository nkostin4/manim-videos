from manim import *
config.stroke_width = 90
config.frame_height = 225
config.frame_width = 225*(16/9)

class FirstRotating(ZoomedScene):

    def __init__(self, **kwargs):
        ZoomedScene.__init__(self, zoomed_factor=5, **kwargs)

    def construct(self):
    
        arcs = VGroup()
    
        radii = np.linspace(2, 100, 50)
        colors = [RED, BLUE]
        
        for i in range(np.size(radii)):
            bin_alter = (len(colors) - i) % 2
            arc = Arc(radius = radii[i], angle = TAU/2, width=900, color=colors[bin_alter])
            arcs.add(arc)
            
        # self.play(Write(arcs))
        self.add(arcs)
        self.wait(1)
        
        # self.play(*[(Rotating(j, about_point = ORIGIN, radians = 2*j.get_arc_length(), rate_function = linear, run_time=50)) for j in arcs])
        
        self.wait()
