# test program with notes for using RpiMotorLib to drive a stepper with an A4988
# notes added into program so we can quickly and easily actually make this work
# in the future - fingers crossed!
# runs without throwing errors - let's see if it will actualyl make a motor move!
# library at https://github.com/gavinlyonsrepo/RpiMotorLib
# note : uses BCM pin numbers

## necessary libraries ##
import sys
import time
import RPi.GPIO as GPIO
#from RpiMotorLib import RpiMotorLib
import RpiMotorLib


## how to set up a motor instance ##

# fix pin numbers!
ms1 = 18 # gpio pin to ms1 on A4988
ms2 = 23 # gpio pin to ms2 on A4988
ms3 = 24 # gpio pin to ms3 on A4988
direction = 25 # connect to direction pin on A4988
step = 8 # connect to step pin on A4988
step_control_pins = (ms1, ms2, ms3) # needs a list (or array apparently) to put into 
# instatiation

# instantiate!
print('starting!')
motor = RpiMotorLib.A4988Nema(direction, step, step_control_pins, "A4988")


## how to make the motor move ##
print('moving!')
rev_direction = True # bool value, default is False - true makes it go clockwise
step_type = 'Half' # string, options are Full, Half, 1/4, 1/8, or 1/16
steps = int(400 * .75) # int of how many steps to take in command, default is 1 rev
step_delay = .05 # float value  of pause inbetween steps (in seconds) - .05 is default (and 
# sounds reasonable)
verbose = False # bool value - lib example says it "write[sic] pin action" - prints it?
initdelay = .05 # the time the program waits after initializing the GPIO pins, but before 
# making the motor start to move - also in seconds
motor.motor_go(rev_direction, step_type, steps, step_delay, verbose, initdelay)

time.sleep(1)
#turn back 270deg
rev_direction = False
print('moving again!')
motor.motor_go(rev_direction, step_type, steps, step_delay, verbose, initdelay)

time.sleep(1)
print('one more move!')
# turn back agian 180deg
motor.motor_go(True, "Half", 200, .05, False, .05)


# clean dem pins, yo!
GPIO.cleanup()
print('pins cleaned up! exiting.')