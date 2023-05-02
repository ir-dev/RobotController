from EPuckBehaviours.behaviour import Behaviour
from EPuckCapabilities.rotationCapabilty import RotationCapabilty


class FindPuckBehaviour(Behaviour):
    
    def __init__(self, robot, rotate_velocity):
        super().__init__(robot)
        self.rotator = RotationCapabilty(robot, rotate_velocity)
    
    def is_applicable(self):
        return True

    def execute(self):
        self.rotator.rotate_robot()
