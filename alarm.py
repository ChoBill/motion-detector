#!/usr/bin/env python 

from datetime import datetime
import os 

class alarm():
    def __init__(self):
        # initial status is False (no alarm)
        self.status = False
        # Alarm period is 5 sec.
        self.alarmPeriod = 3
        # Set alarm audio file 
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.alarmAudioFile = self.path + "/audio/motion_alarm.wav"
        # Initial time
        self.time = datetime.fromtimestamp(0)

    def reset(self):
        # Reset the alarm status
        self.status = False

    def set(self):
        # Set the alarm status
        self.status = True

    def isalarm(self):
        # Retrun the alarm status
        if self.status:
            # If status is True, checking the delta time 
            # Avoiding many alarm in a short period
            deltaTime = datetime.now() - self.time
            if deltaTime.total_seconds() > self.alarmPeriod:
                self.time = datetime.now()
                return True
        return False

    def alarm(self):
        # Playing the alarm voice
        print "alarm..."
        alarmCMD = "aplay " + self.alarmAudioFile + " &"
        os.system ( alarmCMD )
        pass

