#!/usr/bin/env python

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

    def detect(self):
        import cv2
        # Store initial n images to image container
        for i in range(3):
            # Capture a image
            ret, image = self.cam.read()
            self.imgContainer.insert ({"Original": image })

        while True:
            # reset alarm
            self.eventAlarm.reset()

            # Runing the image process strategies
            for strategy in self.strategyConstruction.listStrategy():
                strategy.execute(self.imgContainer)

            # Display the image results:
            cv2.imshow ("Original Image", self.imgContainer.pop("Original") )
            cv2.imshow ("Image process", self.imgContainer.pop("Process") )
            cv2.waitKey(20)

            # Check alarm
            if self.eventAlarm.isalarm():
                self.eventAlarm.alarm()

            # Capture new image
            ret, image = self.cam.read()
            self.imgContainer.insert ({"Original": image })

        # Exist the program
        cv2.destroyAllWindows()

# Run the program
if __name__ == "__main__":
    Motion = motion()
    Motion.detect()
