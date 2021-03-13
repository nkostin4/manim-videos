from manim import *
import random
random.seed(2606)
#random.seed(2808)
config.frame_height = 8
config.frame_width = 8*(16/9)
# config.background_color = "#040080"

class RandomWalk(Scene):
    
    def construct(self):

        frame_width = config["frame_width"]
        frame_height = config["frame_height"]

        path = VMobject(color=BLUE)
        dot = Dot(color=RED, radius=0.04)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])

        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)

        path.add_updater(update_path)
        self.add(path, dot)
        self.wait(2)

        move = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
        x_fin = []
        y_fin = []

        for i in range(1, 900):

            # This is probably me being retarded

            x = dot.get_center()[0]
            y = dot.get_center()[1]

            i = random.choice(move)

            x_new = x + 0.25*i[0]
            y_new = y + 0.25*i[1]

            if y_new < frame_height/2 - 1 and y_new > -frame_height/2 + 1 and x_new < frame_width/2 - 1 and x_new > -frame_width/2 + 1:
                if i[0] == 0:
                    self.play(dot.animate.shift(0.25*i[1]*UP), run_time=0.08)
                    x_fin.append(dot.get_center()[0])
                    y_fin.append(dot.get_center()[1])
                else:
                    self.play(dot.animate.shift(0.25*i[0]*RIGHT), run_time=0.08)
                    x_fin.append(dot.get_center()[0])
                    y_fin.append(dot.get_center()[1])
            else:
                continue

        x_fin = np.array(x_fin)
        y_fin = np.array(y_fin)
        avg_dot = Dot([np.average(x_fin), np.average(y_fin), 0])

        self.play(FadeOut(dot))
        self.add(avg_dot)
        self.wait()

        text = MathTex(r"\text{Average position}").next_to(avg_dot, 0.75*DOWN).scale(0.75)
        self.play(FadeOut(path))
        self.add(text)
        self.wait(2)
        self.play(FadeOut(text))
        self.play(FadeIn(path))
        self.wait(2)
        self.play(FadeOut(path))
        self.play(FadeOut(avg_dot))
        self.wait()
