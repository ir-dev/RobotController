from EPuckBehaviours.behaviour import Behaviour
from EPuckCapabilities.navigationCapability import NavigationCapability

class FollowLeftHandWallBehaviour(Behaviour):
    
    def __init__(self, robot, max_velocity, no_detection_distance):      
        super().__init__(robot)
        self.navigator = NavigationCapability(robot, max_velocity)
        self.max_velocity = max_velocity
        self.no_detection_distance = no_detection_distance
        
    def _update_dist_vector(self):
        self.distVector = self.robot.getProximitySensorValues()
        
    def _is_sensing_obstacle(self):
        return self._is_sensing_obstacle_for_sensors(0, len(self.distVector))
    
    def _is_sensing_obstacle_for_sensors(self, min_range, max_range=None):
        """
            :param min_range: minimum range of sensors to check (inclusive)
            :param max_range: maximum range of sensors to check (exclusive)
        """
        max_range = max_range or min_range + 1
        return min(self.distVector[min_range:max_range]) < self.no_detection_distance
        
    def is_applicable(self):
        self._update_dist_vector()
        
        return self._is_sensing_obstacle()
        
    def execute(self):
        self._update_dist_vector()
        
        # sensors 2-3 are the front sensors
        if self._is_sensing_obstacle_for_sensors(2, 3+1):
            print("obstacle in front: rotate right")
            self.robot.setMotorSpeeds(self.max_velocity, -self.max_velocity)
            return
        
        # sensors 1 is the left front sensor
        if self._is_sensing_obstacle_for_sensors(1):
            print("obstacle in front left: turn slightly right")
            self.robot.setMotorSpeeds(self.max_velocity, self.max_velocity*(3/4))
            return
        
        # when there is any obstacle sensed (this behaviour applies) and the left sensor is not sensing an obstacle, this will rotate the robot left
        # otherwise, the robot will drive while holding threshold distance towards left hand obstacle
        print("robot following wall on left side")
        x = min(max(self.distVector[0], 0), 0.02)
        self.navigator.navigate_robot(0.02-x, x_origin=0.01, x_min=0, x_max=0.02)

