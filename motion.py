#!/usr/bin/env python

import cv2

class motion():
    def __init__(self):
        # Construct the camera capture object
        from camera import camera
        self.cam = camera()
        # Using container to store images
        from container import dataContainer
        self.imgContainer = dataContainer()
        # Contruct a alarm object
        from alarm import alarm
        self.eventAlarm = alarm()
        # Construct the image processing strategy
        from strategy import strategyConstructor
        self.strategyConstruction = strategyConstructor(self.eventAlarm)
        # check if X11 DISPLAY exist
        self._isgui = self._checkGUI()

    def detect(self):
        # Store initial n images to image container
        for i in range(3):
            # Capture a image
            self.fetchImage()

        while True:
            # reset alarm
            self.eventAlarm.reset()
            # Runing the image process strategies
            for strategy in self.strategyConstruction.listStrategy():
                strategy.execute(self.imgContainer)
            # Display image
            self.showImage()
            # Check alarm
            if self.eventAlarm.isalarm():
                self.eventAlarm.alarm()
            # Capture new image
            self.fetchImage()
        # Close window and exit the program
        self.closeWindow()

    def fetchImage(self):
        # Capture a image
        ret, image = self.cam.read()
        self.imgContainer.insert ({"Original": image })

    def showImage(self):
        # Display the image results:
        if (self._isGUI()):
            cv2.imshow ("Original Image", self.imgContainer.pop("Original") )
            cv2.imshow ("Image process", self.imgContainer.pop("Process") )
            cv2.waitKey(20)
        else:
            self.imgContainer.pop("Original")
            self.imgContainer.pop("Process")

    def closeWindow(self):
        # Close all cv2 window
        if (self._isGUI()):
            cv2.destroyAllWindows()
        else:
            exit()

    def _checkGUI(self):
        # check if X11 DISPLAY exist
        import os
        return os.environ.has_key('DISPLAY')

    def _isGUI(self):
        # check X11 DISPLAY exist
        return self._isgui

# Run the program
if __name__ == "__main__":
    Motion = motion()
    Motion.detect()
