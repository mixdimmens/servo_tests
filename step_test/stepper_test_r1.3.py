# test program with notes for using RpiMotorLib to drive a stepper with an A4988
# and takes user input (as degrees) and outputs corresponding motor movements
# library at https://github.com/gavinlyonsrepo/RpiMotorLib
# note : uses BCM pin numbers

## necessary libraries ##
import sys
import time
import RPi.GPIO as GPIO
#from RpiMotorLib import RpiMotorLib
import RpiMotorLib

## convert angle to steps in ya want to ##
def angle_to_step():
    angle = int(input('enter angle of change from current position'))
    steps = int((angle * 200)/360)
    return(steps)

## how to set up a motor instance ##

ms1 = 11 
ms2 = 9 
ms3 = 10
direction = 26
step = 19 
step_control_pins = (ms1, ms2, ms3) 

# instantiate!
print('starting!')
motor = RpiMotorLib.A4988Nema(direction, step, step_control_pins, "A4988")

count = 0
## how to make the motor move ##
while count < 5:
    ## control variables for motor_go method
    rev_direction = True 
    step_type = '1/8' 
    steps = angle_to_step() 
    step_delay = .001 
    verbose = False 
    initdelay = .005 
        
    print('moving!')
    motor.motor_go(rev_direction, step_type, steps, step_delay, verbose, initdelay)

    time.sleep(1)
    #turn back 270deg
    steps = angle_to_step()
    rev_direction = False
    print('moving again!')
    motor.motor_go(rev_direction, step_type, steps, step_delay, verbose, initdelay)

    time.sleep(1)
#    half_steps = int (steps / 2)
    print('one more move!')
    # turn back agian 180deg
    motor.motor_go(True, "1/4", int((steps / 2)), .001, False, .05)
    
    count += 1
    print(count)
    if count % 2 != 0:
        time.sleep(1)

# clean dem pins, yo!
GPIO.cleanup()
print('pins cleaned up! exiting.')

