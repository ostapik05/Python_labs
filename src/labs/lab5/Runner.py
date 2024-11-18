from shared.interfaces.RunnerInterface import RunnerInterface
from labs.lab5.bll.TorusSimulation import TorusSimulation

class Runner(RunnerInterface):
    @staticmethod
    def run():
        simulation = TorusSimulation()
        simulation.get_user_input()
        simulation.run()
