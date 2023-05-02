# -*- coding: utf-8 -*-
"""
minimal template for BasicEPuck.ePuckVRep
for usage with ePuckS5V12.ttm

@author: hoch ralph
"""
from enum import Enum
import time
from BasicEPuck.ePuckVRep import EPuckVRep
from EPuckBehaviours.detachLeftHandWallBehaviour import DetachLeftHandWallBehaviour
from EPuckBehaviours.driveToPuckBehaviour import DriveToPuckBehaviour
from EPuckBehaviours.findPuckBehaviour import FindPuckBehaviour
from EPuckBehaviours.followLeftHandWallBehaviour import FollowLeftHandWallBehaviour

# maximum velocity = ~2 Rad
JOINT_MAX_VELOCITY = 120 * 3.1415 / 180
CAMERA_RESOLUTION = (64, 64)

class Velocity(float, Enum):
    QUARTER = JOINT_MAX_VELOCITY/4
    HALF = JOINT_MAX_VELOCITY/2
    FULL = JOINT_MAX_VELOCITY

def main():
    robot = EPuckVRep('ePuck', port=19999, synchronous=False)

    robot.enableCamera()
    robot.enableAllSensors()
    robot.setSensesAllTogether(False)  # we want fast sensing, so set robot to sensing mode where all sensors are sensed

    noDetectionDistance = 0.05 * robot.getS()  # maximum distance that proximity sensors of ePuck may sense
    
    behaviours = [
        DetachLeftHandWallBehaviour(robot,  max_velocity=Velocity.HALF.value, camera_resolution=CAMERA_RESOLUTION, no_detection_distance=noDetectionDistance),
        FollowLeftHandWallBehaviour(robot, max_velocity=Velocity.HALF.value, no_detection_distance=noDetectionDistance),
        DriveToPuckBehaviour(robot, max_velocity=Velocity.HALF.value, camera_resolution=CAMERA_RESOLUTION),
        FindPuckBehaviour(robot, rotate_velocity=Velocity.QUARTER.value)
    ]

    # main sense-act cycle
    while robot.isConnected():
        robot.fastSensingOverSignal()
        
        for behaviour in behaviours:
            if (behaviour.is_applicable()):
                behaviour.execute()
                break

        time.sleep(0.01)

    robot.disconnect()


if __name__ == '__main__':
    main()
