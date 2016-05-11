#!/usr/bin/env python

import cv2

class camera():
    '''
    Camera capture class
    '''
    def __init__(self, device=0, image_size=[]):
        '''
        Initial the camera capture object
        '''
        self.device = device
        self.image_size = image_size
        self.cam = cv2.VideoCapture(device)

    def read(self):
        '''
        Read new image from camera
        Return:
            A cv2 image
        '''
        return self.cam.read()


if __name__ == "__main__":
    cam = camera()
    ret, image = cam.read()
    cv2.imshow ("Image Test", image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

