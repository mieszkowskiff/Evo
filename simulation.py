from creature import Creature, distance
import random
import pygame as pg
import time




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

        # display
        pg.init()
        self.screen = pg.display.set_mode([1000, 1000])
        running = True
        start_time = time.time()
        while running:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            self.screen.fill((255, 255, 255))
            dt = time.time() - start_time
            self.move_frame(dt)
            self.draw_frame()
            start_time = time.time()
            pg.display.flip()
            if time.time() - self.simulation_start_time > 100:
                self.food_spawn_probability = 0
        pg.quit()

    def draw_frame(self):
        for creature in self.creatures:
            pg.draw.circle(
                self.screen, 
                (0, 0, 255), 
                creature.get_position(), 
                10
                )
        for food in self.foods:
            pg.draw.circle(
                self.screen, 
                (255, 0, 0), 
                food, 
                5
                )

    def cost(self, genes, dt):
        return (genes["velocity"]**2 + genes["vision"]**2 + genes["grab range"]**2 + genes["capacity"] + 100) * dt * 1e-6

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
    Simulation()