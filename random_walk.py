from random import choice

class RandomWalk:
    """Generates random walk"""

    def __init__(self, num_points=5000):
        self.num_points = num_points

        #all start at 0,0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all the points in the walk"""

        #keep filling the walk until reach the point limit
        while len(self.x_values) < self.num_points:
            # for x
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_steps = x_direction * x_distance

            # for x
            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4])
            y_steps = y_direction * y_distance

            #ignore 0 steps
            if x_steps == 0 and y_steps == 0:
                continue

            # the new position from the last point 
            x = self.x_values[-1] + x_steps
            y = self.y_values[-1] + y_steps

            self.x_values.append(x)
            self.y_values.append(y)
