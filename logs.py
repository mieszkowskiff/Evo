import numpy as np
import pickle


class Log:
    def __init__(self, simulation):
        self.log = []
        self.simulation = simulation
        self.keys = list(self.simulation.creatures[0].genes.keys())


    def compress(self, creature):
        return [creature.genes[item] for item in creature.genes]
    
    def save_frame(self):
        self.log.append(np.array([self.compress(creature) for creature in self.simulation.creatures], dtype = np.float16))

    def save_log(self, filename = "logs.obj"):
        file = open(filename, 'wb')
        pickle.dump((self.log, self.simulation.cost, self.simulation.food_spawn_probability, self.keys), file)
        file.close()

    def read_log(self, filename = "logs.obj"):
        with open(filename, "rb") as file:
            return pickle.load(file)


