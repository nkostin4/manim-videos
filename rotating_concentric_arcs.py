from manim import *
config.frame_height = 225
config.frame_width = 225*(16/9)

class FirstRotating(Scene):

    def construct(self):
    
        arcs = VGroup()
    
        radii = np.linspace(2, 100, 50)
        colors = [RED, BLUE]
        
        for i in range(np.size(radii)):
            bin_alter = (len(colors) - i) % 2
            # arc = Arc(radius = radii[i], angle = TAU/2, width=900, color=colors[bin_alter])
            arc = ParametricFunction(lambda t: [radii[i]*np.cos(t), radii[i]*np.sin(t), 0], t_min = 0, t_max = PI, stroke_width = 60, color=colors[bin_alter])
            arcs.add(arc)
            
        self.play(Write(arcs))
        # self.add(arcs)
        self.wait(1)
        
        # self.play(*[(Rotating(j, about_point = ORIGIN, radians = 2*j.get_arc_length(), rate_function = linear, run_time=400)) for j in arcs])
        self.play(*[(Rotating(j, about_point = ORIGIN, radians = 2*PI*(np.linalg.norm(j.get_last_point())), rate_function = linear, run_time=50)) for j in arcs])
        
        self.wait(4)
