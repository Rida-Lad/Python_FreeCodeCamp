import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        
        drawn = random.sample(self.contents, num_balls)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    
    for _ in range(num_experiments):
        # Create a deep copy of the hat for each experiment
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count how many of each color we drew
        drawn_counts = {}
        for color in drawn_balls:
            drawn_counts[color] = drawn_counts.get(color, 0) + 1
        
        # Check if we got at least the expected balls
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break
        
        if success:
            successes += 1
    
    return successes / num_experiments