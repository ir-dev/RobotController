from EPuckCapabilities.navigationCapability import NavigationCapability


class DriveTowardsPuckCapability(NavigationCapability):
    
    def __init__(self, robot, max_velocity, camera_resolution):
        """
            :param camera_resolution: the resolution of the robots camera
        """
        super().__init__(robot, max_velocity)
        self.camera_resolution = camera_resolution
        
    def get_puck(self):
        return self._detectBox(self.camera_resolution, self.robot.getCameraImage())
    
    def drive_to_puck(self, puck_center):
        resolX = self.camera_resolution[0]
        self.navigate_robot(puck_center[0], x_origin=resolX/2, x_min=0, x_max=resolX)
        
    def _detectBox(self, resolution, image):
        """
            looks in current image for a black blob on a red background, from left to right
            :param resolution: the resolution of the robots camera
            :param image: a rgb image with black blobs on red background
            :return: the center of the blob, or False if no blob was found
        """
        resolX = resolution[0]
        resolY = resolution[1]
        
        minBlobWidth = 5
        xStart = -1
        xCenter = [-1]
        for y in range(resolY):
            blobwidth = 0
            for x in range(resolX):
                pixel = image.getpixel((x, y))
                if pixel == (0, 0, 0):  # black pixel: a box!
                    blobwidth += 1
                    if blobwidth == 1:
                        xStart = x
                else:
                    if blobwidth >= minBlobWidth:
                        xCenter[0] = xStart + blobwidth / 2
                        # print('blob detected at: ', xStart, y, ' with center at: ', xCenter[0])
                        return xCenter
                    elif blobwidth > 0:
                        blobwidth = 0
            if blobwidth >= minBlobWidth:
                xCenter[0] = xStart + blobwidth / 2
                # print('blob detected at: ', xStart, y, ' with center at: ', xCenter[0])
                return xCenter

        return False
