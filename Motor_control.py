import time
from time import sleep
#import RPi.GPIO as GPIO
#import l293d.driver as l293d

class MotorControl():
    '''
    controlling the motors in clockwise and anti-clockwise
    '''
    def __init__(self,main):
        self.mainw=main
    def motor_forward(self):
        #motor is clockwise direction
        while not self.mainw.stop.isChecked():
            print('motor is running in forward direction')
        else:
            print('the motor is stopped in the Motor control class')
    def motor_backward(self):
        #motor is running in anti-clockwise direction
        print('motor is running in backward direction')
    def motor_stop(self):
        #all motors are completely stooped
        print('all motors are completely stopped')
