from EPuckBehaviours.behaviour import Behaviour
from EPuckCapabilities.driveTowardsPuckCapability import DriveTowardsPuckCapability

class DetachLeftHandWallBehaviour(Behaviour):
    
    def __init__(self, robot, max_velocity, camera_resolution, no_detection_distance):        
        super().__init__(robot)
        self.puck_driver = DriveTowardsPuckCapability(robot, max_velocity, camera_resolution)
        self.no_detection_distance = no_detection_distance
        
    def _update_dist_vector(self):
        self.distVector = self.robot.getProximitySensorValues()
    
    # NOTE: this method is duplicated from followLeftHandWallBehaviour.py and may be refactored    
    def _is_sensing_obstacle_for_sensors(self, min_range, max_range=None):
        """
            :param min_range: minimum range of sensors to check (inclusive)
            :param max_range: maximum range of sensors to check (exclusive)
        """
        max_range = max_range or min_range + 1
        return min(self.distVector[min_range:max_range]) < self.no_detection_distance
        
    def is_applicable(self):
        self._update_dist_vector()
        
        return self._is_sensing_obstacle_for_sensors(0) and not self._is_sensing_obstacle_for_sensors(1, 3+1) and True if self.puck_driver.get_puck() else False
        
    def execute(self):
        print ("detach execute")
        puck = self.puck_driver.get_puck()
        if not puck:
            return
        
        self.puck_driver.drive_to_puck(puck)
