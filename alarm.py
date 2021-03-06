#!/usr/bin/env python3 

from datetime import datetime
import os 

class alarm():
    '''
    Set/Reset the alarm, and play the alarm voice.
    '''
    def __init__(self):
        '''
        Initial the alarm object
        '''
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
        '''
        Reset the alarm status
        '''
        self.status = False

    def set(self):
        '''
        Set the alarm status
        '''
        self.status = True

    def isalarmHysteresis(self):
        '''
        Retrun the alarm status with delay
        Returns:
            [True|False]
        '''
        if self.status:
            # If status is True, checking the delta time 
            # Avoiding many alarm in a short period
            deltaTime = datetime.now() - self.time
            if deltaTime.total_seconds() > self.alarmPeriod:
                self.time = datetime.now()
                return True
        return False

    def isalarm(self):
        '''
        Retrun the alarm status
        Returns:
            [True|False]

        '''
        return self.status

    def alarm(self):
        '''
        Playing the alarm voice
        '''
        print ("alarm...")
        alarmCMD = "aplay " + self.alarmAudioFile + " &"
        os.system ( alarmCMD )
        pass

