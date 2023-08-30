import random
import math
import numpy as np


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

class Creature:
    def __init__(self):

        # position
        self.position = (random.uniform(0, 1000), random.uniform(0, 1000))
        self.direction = random.uniform(-math.pi, math.pi)

        # hunger = 0 => dies
        self.hunger = 1



        # genes:

        self.genes = {

            # how fast creature moves
            "velocity": random.uniform(0, 100),

            # how far does creature see food
            "vision": random.uniform(0, 100),

            # how far can grab food
            "grab range": random.uniform(0, 10),
        }

        
    def get_position(self):
        return self.position

    def move(self, simulation, dt):
        min_distance = 2000
        nearest_food_position = (0, 0)
        for food in simulation.foods:
            if distance(self.position, food) < min_distance:
                min_distance = distance(self.position, food)
                nearest_food_position = food
        if min_distance < self.genes["vision"]:
            self.direction = math.atan2(
                (nearest_food_position[1] - self.position[1]),
                (nearest_food_position[0] - self.position[0])
                )
        else:
            self.direction += random.uniform(-math.pi, math.pi) / 40
        self.position = (
            self.position[0] + math.cos(self.direction) * self.genes["velocity"] * dt, 
            self.position[1] + math.sin(self.direction) * self.genes["velocity"] * dt
        )
        if self.hunger > 2.2:
            self.reproduce(simulation)
            self.hunger -= 1.2
    
    def reproduce(self, simulation):
        descendant = Creature()
        descendant.position = self.position
        descendant.genes = {
            "velocity":  np.random.normal(self.genes["velocity"], 3),
            "vision": np.random.normal(self.genes["vision"], 3),
            "grab range": np.random.normal(self.genes["grab range"], 3)
        }
        simulation.creatures.append(descendant)
        




    

    

