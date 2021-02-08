#!/usr/bin/env python3

import cv2

class alternativeStrategy(object):
    '''
    A template strategy
    '''
    def __init__(self):
        pass

    def execute(self):
        print("Please implement an execution method." )

# Define each image process strategy
class diffStrategy(alternativeStrategy):
    '''
    Compare difference of images
    '''
    def __init__(self):
        pass

    def execute(self, imageContainer):
        # get the original image list from imageContainer
        images = imageContainer.get("Original")
        [image1, image2] = [images[0], images[-1]]
        # Calculate difference
        self.diffImage = cv2.absdiff (image1, image2)
        # save the processed image
        imageContainer.insert({"Process": self.diffImage})

class blurStrategy(alternativeStrategy):
    '''
    Apply blur to the image
    '''
    def __init__(self):
        self.blurSetting=(3,3)

    def execute(self, imageContainer):
        image = imageContainer.pop("Process")
        # Blur the image
        self.blurImage = cv2.blur(image, self.blurSetting)
        # save the processed image
        imageContainer.insert({"Process": self.blurImage})

class thresStrategy(alternativeStrategy):
    '''
    Apply threshold to the image
    '''
    def __init__(self):
        self.thresValue = 32
        self.thresMaxVal = 255

    def execute(self, imageContainer):
        image = imageContainer.pop("Process")
        # Apply threshold (enhanced)
        ret, self.thresImage = cv2.threshold(image, self.thresValue, self.thresMaxVal, cv2.THRESH_BINARY)
        # save the processed image
        imageContainer.insert({"Process": self.thresImage})

class findContoursStrategy(alternativeStrategy):
    '''
    Find contour and set alarm if needed
    '''
    def __init__(self, alarm):
        self.alarm = alarm

    def execute(self, imageContainer):
        image = imageContainer.pop("Process")
        # convert to gray scale 
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Find contours
        max_contours=0
        contours, hierarchy = cv2.findContours(gray_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)
        for contour in contours:
            x,y,w,h = cv2.boundingRect(contour)
            # Filter out the small boundaries
            if w*h > 225:
                cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
                # Enable alarm
                self.alarm.set()
                # Record the max contour
                if w*h > max_contours:
                    max_contours = w*h
        # save the processed image
        imageContainer.insert({"Process": image})

class strategyConstructor():
    '''
    Constuctor of these image processing strategies
    '''
    def __init__(self, alarm):
        self.strategyList = []
        # Actually these strategies are the basic operation of motion detection
        self.strategyList.append ( diffStrategy() )
        self.strategyList.append ( blurStrategy() )
        self.strategyList.append ( thresStrategy() )
        self.strategyList.append ( findContoursStrategy(alarm) )

    def listStrategy(self):
        return self.strategyList

if __name__ == "__main__":
    from camera import camera
    cam = camera()

    # Construce the strategies object
    strategyConstruction = strategyConstructor()

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

    for strategy in strategyConstruction.listStrategy():
        strategy.execute(imgContainer)

    cv2.imshow ("Image process", imgContainer.pop("Process") )
    cv2.waitKey(2000)

    cv2.destroyAllWindows()

