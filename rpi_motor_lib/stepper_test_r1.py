# test program with notes for using RpiMotorLib to drive a stepper with an A4988
# notes added into program so we can quickly and easily actually make this work
# in the future - fingers crossed!
# library at https://github.com/gavinlyonsrepo/RpiMotorLib
# note : uses BCM pin numbers

## necessary libraries ##
import sys
import time
from RpiMotorLib import RpiMotorLib


## how to set up a motor instance ##

ms1 = 1 # gpio pin to ms1 on A4988
ms2 = 2 # gpio pin to ms2 on A4988
ms3 = 3 # gpio pin to ms3 on A4988
direction = 4 # connect to direction pin on A4988
step = 5 # connect to step pin on A4988
step_control_pins = (ms1, ms2, ms3) # needs a list (or array apparently) to put into 
# instatiation

# instantiate!
motor = RpiMotorLib.A4988Nema(direction, step, step_control_pins, 'A4988')


## how to make the motor move ##

clockwise = True # bool value, default is False - true makes it go clockwise
steptype = 'Half' # string, options are Full, Half, 1/4, 1/8, or 1/16
steps = int(400 * .75) # int of how many steps to take in command, default is 1 rev
stepdelay = .05 # float value  of pause inbetween steps (in seconds) - .05 is default (and 
# sounds reasonable)
verbose = False # bool value - lib example says it "write[sic] pin action" - prints it?
initdelay = .05 # the time the program waits after initializing the GPIO pins, but before 
# making the motor start to move - also in seconds
motor.motor_go(clockwise, steptype, steps, stepdelay, verbose, initdelay)

time.sleep(1)
#turn back 270deg
clockwise = False
motor.motor_go(clockwise, steptype, steps, stepdelay, verbose, initdelay)

time.sleep(1)
# turn back agian 180deg
motor.motor_go(True, "Half", 200, .05, False, .05)


# clean dem pins, yo!
GPIO.cleanup()
print('pins cleaned up! exiting.')