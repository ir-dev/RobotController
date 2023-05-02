class RotationCapabilty:
    def __init__(self, robot, rotate_velocity):
        """
            :param rotate_velocity:  the velocity (and direction) in rad/s to rotate with
        """
        self.robot = robot
        self.rotate_velocity = rotate_velocity
 
    def rotate_robot(self):
        self.robot.setMotorSpeeds(self.rotate_velocity, -self.rotate_velocity)
        
    def rotate_reverse_robot(self):
        self.robot.setMotorSpeeds(-self.rotate_velocity, self.rotate_velocity)
