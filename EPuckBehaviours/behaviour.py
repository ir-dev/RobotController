from abc import ABC, abstractmethod

class Behaviour(ABC):
    def __init__(self, robot):
        """
            :param robot: the instance of the robot to apply the behaviour to
        """
        self.robot = robot

    @abstractmethod
    def is_applicable(self):
        pass

    @abstractmethod
    def execute(self):
        pass
 