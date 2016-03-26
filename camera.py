#!/usr/bin/env python

import cv2

class camera():
    def __init__(self, device=0, image_size=[]):
        self.device = device
        self.image_size = image_size
        self.cam = cv2.VideoCapture(device)

    def read(self):
        return self.cam.read()


if __name__ == "__main__":
    cam = camera()
    ret, image = cam.read()
    cv2.imshow ("Image Test", image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

