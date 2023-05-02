class NavigationCapability:
    def __init__(self, robot, max_velocity):
        """
            :param robot: the robot to navigate
            :param max_velocity: the maximum velocity to drive in rad/s
        """
        self.robot = robot
        self.max_velocity = max_velocity
 
    def navigate_robot(self, x, x_origin, x_min, x_max):
        """ Motor speed calculation based on actual x to navigate towards x_origin """
        assert x_min <= x <= x_max
        assert x_min <= x_origin <= x_max
        
        # setup the coordinate system with y as velocity and x as distance to x_origin
        yMin = -self.max_velocity
        yMax = self.max_velocity
        xMin = x_min - x_origin
        xMax = x_max - x_origin
        # This is the deviation from the origin (within xMin and xMax)
        xDeviation = x - x_origin
        
        # xDeviation < 0 means the robot must correct to the left
        if xDeviation < 0:
            # k = (y2 - y1) / (x2 - x1)
            # left motor proportional to deviation
            # right motor is max speed
            slopeLeft = (yMax - yMin) / (0 - xMin)
            speedLeft = slopeLeft*xDeviation + yMax
            speedRight = yMax
        else:
            # k = (y2 - y1) / (x2 - x1)
            # left motor is max speed
            # right motor proportional to deviation
            slopeRight = (yMin - yMax) / (xMax - 0)
            speedLeft = yMax
            speedRight = slopeRight*xDeviation + yMax
            
        self.robot.setMotorSpeeds(speedLeft, speedRight) 
