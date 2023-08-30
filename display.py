import pygame as pg
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def blit_text(surface, text, pos, font, color=pg.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.



class Displayer:
    def __init__(self, simulation):
        pg.init()
        self.creature_to_display = simulation.creatures[0]
        pg.display.set_caption('Simulation')
        self.font = pg.font.SysFont('Calibri', 20)

        self.creature_radius = 10
        self.creature_color = (0, 0, 255) # blue

        self.food_radius = 5
        self.food_color = (255, 0, 0) # red

        self.text_background = (125, 125, 125) #gray
        self.text_color = (0, 0, 0) # black

        self.screen = pg.display.set_mode([1000, 1000])

        
    
    def quit(self, simulation):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return True
            if event.type == pg.MOUSEBUTTONUP:
                self.click(simulation)
        return False

    def display_frame(self, simulation):
            self.screen.fill((255, 255, 255))
            for creature in simulation.creatures:
                circle = pg.Surface((self.creature_radius * 2, self.creature_radius * 2), pg.SRCALPHA)
                pg.draw.circle(circle, (0, 0, 255, 128), (self.creature_radius, self.creature_radius), self.creature_radius)
                self.screen.blit(circle, (creature.get_position()[0] - self.creature_radius, creature.get_position()[1] - self.creature_radius))

            for food in simulation.foods:
                pg.draw.circle(
                    self.screen, 
                    self.food_color, 
                    food, 
                    self.food_radius
                    )
            blit_text(
                self.screen, 
                f"""hunger: {self.creature_to_display.hunger}
velocity: {self.creature_to_display.genes["velocity"]}
vision: {self.creature_to_display.genes["vision"]}
grab range: {self.creature_to_display.genes["grab range"]}""",
    

                (0, 0), 
                self.font
                )
            pg.display.flip()
            
        

    def click(self, simulation):
        mouse_pos = pg.mouse.get_pos()
        for creature in simulation.creatures:
            if distance(creature.get_position(), mouse_pos) < self.creature_radius * 2:
                self.creature_to_display = creature
                

                


    
    def finish(self):
        pg.quit()
    
