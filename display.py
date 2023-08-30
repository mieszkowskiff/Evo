import pygame as pg


class Displayer:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([1000, 1000])
    
    def quit(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return True
        return False

    def display_frame(self, simulation):
            self.screen.fill((255, 255, 255))
            for creature in simulation.creatures:
                pg.draw.circle(
                    self.screen, 
                    (0, 0, 255), 
                    creature.get_position(), 
                    10
                    )
            for food in simulation.foods:
                pg.draw.circle(
                    self.screen, 
                    (255, 0, 0), 
                    food, 
                    5
                    )
            pg.display.flip()
    
    def finish(self):
        pg.quit()
    
