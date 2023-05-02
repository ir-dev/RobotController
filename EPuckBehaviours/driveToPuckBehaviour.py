from EPuckBehaviours.behaviour import Behaviour
from EPuckCapabilities.driveTowardsPuckCapability import DriveTowardsPuckCapability

class DriveToPuckBehaviour(Behaviour):
    
    def __init__(self, robot, max_velocity, camera_resolution):
        super().__init__(robot)
        self.puck_driver = DriveTowardsPuckCapability(robot, max_velocity, camera_resolution)
        
    def is_applicable(self):
        return True if self.puck_driver.get_puck() else False

    def execute(self):
        puck = self.puck_driver.get_puck()
        if not puck:
            return
        
        self.puck_driver.drive_to_puck(puck)
