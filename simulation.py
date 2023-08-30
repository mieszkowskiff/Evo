from creature import Creature, distance
import random
import pygame as pg
import time
from display import Displayer




class Simulation:

    def __init__(self):

        # constants
        self.starting_food = 10
        self.starting_creatures = 4
        self.food_spawn_probability = 0.01
        self.simulation_start_time = time.time()

        # objects
        self.foods = [(random.uniform(0, 1000), random.uniform(0, 1000)) for i in range(self.starting_food)]
        self.creatures = [Creature() for i in range(self.starting_creatures)]

    def run(self):
        displayer = Displayer()
        dt = 0.001
        while not displayer.quit():

            start_time = time.time()
            self.move_frame(dt)
            displayer.display_frame(self)






            dt = time.time() - start_time
    
            

        


    def cost(self, genes, dt):
        return (1/10 * genes["velocity"]**2 + genes["vision"]**2 + genes["grab range"]**2 + genes["capacity"] + 100) * dt * 1e-6

    def move_frame(self, dt):
        for creature in self.creatures[:]:
            creature.move(self, dt)
            for food in self.foods[:]:
                if distance(food, creature.position) < creature.genes["grab range"]:
                    creature.hunger = min(creature.hunger + 1, creature.genes["capacity"])
                    self.foods.remove(food)
                    
            creature.hunger -= self.cost(creature.genes, dt)
            if creature.hunger < 0:
                self.creatures.remove(creature)
                print("creature died")
                



        if random.uniform(0, 1) < self.food_spawn_probability:
            self.foods.append((random.uniform(0, 1000), random.uniform(0, 1000)))



if __name__ == "__main__":
    simulation1 = Simulation()
    simulation1.run()