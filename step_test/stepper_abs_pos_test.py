import sys
import time
#from RpiMotorLib import A4988Nema
import RpiMotorLib
from stepper_abs_pos import StepperAbsPos as StepperAbsPos

## demo instance, dummy: ##

# #fill in the blanks:
direction__pin = 19
step__pin = 26
mode__pins = (25,26,27)
stepper__position = 0

stepper = StepperAbsPos(direction__pin, step__pin, mode__pins, stepper__position, "A4988")

# #test absolute position change
# stepper.abs_position(635, False)
# print('stepper position 1: {}'.format(stepper))
# stepper.abs_position(135, True)
# print('stepper position 2: {}'.format(stepper))
# stepper.abs_position(135, True)
# print('stepper position 3: {}'.format(stepper))
# stepper.new_home()
# print(stepper)

# print(stepper)

step_type = 'Half'
step_delay = .005
init_delay = .005

print(1)
stepper.abs_motor_go(50, step_type, step_delay, init_delay)
print(stepper)
print('')

print(2)
stepper.abs_motor_go(100, step_type, step_delay, init_delay)
print(stepper)
print('')

print(3)
stepper.abs_motor_go(50, step_type, step_delay, init_delay)
print(stepper)
print('')

print(4)
stepper.abs_motor_go(70, step_type, step_delay, init_delay)
print(stepper)
print('')

print(5)
stepper.abs_motor_go(180, step_type, step_delay, init_delay)
print(stepper)
print('')

print(6)
stepper.abs_motor_go(5, step_type, step_delay, init_delay)
print(stepper)
print('')

print(7)
stepper.abs_motor_go(0, step_type, step_delay, init_delay)
print(stepper)
print('')

print(8)
stepper.abs_motor_go(100, step_type, step_delay, init_delay, 1)
print(stepper)
print('')