from random import choice


class RandomWalk:
    """Class that generates a random walk."""
    def __init__(self):
        """initialize related to walks."""
        self.nums = 5000

        self.x_values = [0]
        self.y_values = [0]

    def generate_walk(self):
        """Generate 5000 random walks"""
        while len(self.x_values) < self.nums:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_point = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_point = y_distance * y_direction

            if x_point == 0 and y_point == 0:
                continue

            x = self.x_values[-1] + x_point
            y = self.y_values[-1] + y_point

            self.x_values.append(x)
            self.y_values.append(y)
