#!/usr/bin/env python

import cv2

# Define a template for alternative strategy
class alternativeStrategy(object):
    def __init__(self):
        pass

    def execute(self):
        print("Please implement an execution method." )

# Define each image process strategy
# Define image difference 
class diffStrategy(alternativeStrategy):
    def __init__(self):
        pass

    def execute(self, images):
        image1 = images[0]
        image2 = images[1]
        # Calculate difference
        self.diffImage = cv2.absdiff (image1, image2)
        return self.diffImage

# Define image blur 
class blurStrategy(alternativeStrategy):
    def __init__(self):
        self.blurSetting=(3,3)

    def execute(self, images):
        # Blur the image
        self.blurImage = cv2.blur(images[0], self.blurSetting)
        return self.blurImage

# Define image threshod 
class thresStrategy(alternativeStrategy):
    def __init__(self):
        self.thresValue = 32
        self.thresMaxVal = 255

    def execute(self, images):
        # Apply threshold (enhanced)
        ret, self.thresImage = cv2.threshold(images[0], self.thresValue, self.thresMaxVal, cv2.THRESH_BINARY)
        return self.thresImage


if __name__ == "__main__":
    from camera import camera
    cam = camera()

    # Construce the strategies object
    strategyList = []
    strategyList.append ( diffStrategy() )
    strategyList.append ( blurStrategy() )
    strategyList.append ( thresStrategy() )

    # Capture a image
    ret, image1 = cam.read()

    cv2.imshow ("Image Test", image1)
    cv2.waitKey(1000)

    # Capture another image
    ret, image2 = cam.read()

    # Processing image
    processImage = [image1, image2]
    for strategy in strategyList:
        processImage.insert (0, strategy.execute(processImage) )

    cv2.imshow ("Image process", processImage[0])
    cv2.waitKey(1000)

    cv2.destroyAllWindows()

