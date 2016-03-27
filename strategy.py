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

    def execute(self, imageContainer):
        # get the original image list from imageContainer
        images = imageContainer.get("Original")
        [image1, image2] = [images[0], images[-1]]
        # Calculate difference
        self.diffImage = cv2.absdiff (image1, image2)
        #return self.diffImage
        imageContainer.insert({"Process": self.diffImage})

# Define image blur 
class blurStrategy(alternativeStrategy):
    def __init__(self):
        self.blurSetting=(3,3)

    def execute(self, imageContainer):
        image = imageContainer.pop("Process")
        # Blur the image
        self.blurImage = cv2.blur(image, self.blurSetting)
        #return self.blurImage
        imageContainer.insert({"Process": self.blurImage})

# Define image threshod 
class thresStrategy(alternativeStrategy):
    def __init__(self):
        self.thresValue = 32
        self.thresMaxVal = 255

    def execute(self, imageContainer):
        image = imageContainer.pop("Process")
        # Apply threshold (enhanced)
        ret, self.thresImage = cv2.threshold(image, self.thresValue, self.thresMaxVal, cv2.THRESH_BINARY)
        #return self.thresImage
        imageContainer.insert({"Process": self.thresImage})


if __name__ == "__main__":
    from camera import camera
    cam = camera()

    # Construce the strategies object
    strategyList = []
    strategyList.append ( diffStrategy() )
    strategyList.append ( blurStrategy() )
    strategyList.append ( thresStrategy() )

    # Using container to store images
    from container import dataContainer
    imgContainer = dataContainer()

    # Store initial n images to image container
    for i in range(5):
        # Capture a image
        ret, image = cam.read()
        imgContainer.insert ({"Original": image.copy() })
        cv2.imshow ("Image original", image )
        cv2.waitKey(50)

    for strategy in strategyList:
        strategy.execute(imgContainer)

    cv2.imshow ("Image process", imgContainer.pop("Process") )
    cv2.waitKey(2000)

    cv2.destroyAllWindows()

