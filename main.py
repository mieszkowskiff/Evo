from logs import Log
from simulation import Simulation


def main():
    log = Log(Simulation())
    print(log.read_log("/home/pc/Pulpit/python/Evo/extinction_simulation.obj"))




if __name__ == "__main__":
    main()