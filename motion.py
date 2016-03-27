#!/usr/bin/env python

# Parsing command parameters and generate parameter dictionary
pass

# Construct the camera capture object
from camera import camera
cam = camera()

# Using container to store images
from container import dataContainer
imgContainer = dataContainer()

# Construct the image processing strategy
from strategy import strategyConstructor
strategyConstruction = strategyConstructor()

# Construct the iterator contains the camera object and strategy
pass

# Run the program
if __name__ == "__main__":
    import cv2

    # Store initial n images to image container
    for i in range(3):
        # Capture a image
        ret, image = cam.read()
        imgContainer.insert ({"Original": image })

    while True:
        # Runing the image process strategies
        for strategy in strategyConstruction.listStrategy():
            strategy.execute(imgContainer)

        # Display the image results:
        cv2.imshow ("Original Image", imgContainer.pop("Original") )
        cv2.imshow ("Image process", imgContainer.pop("Process") )
        cv2.waitKey(20)

        # Capture new image
        ret, image = cam.read()
        imgContainer.insert ({"Original": image })

    # Exist the program
    cv2.destroyAllWindows()
