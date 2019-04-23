#!/usr/bin/env python3
from RpiMotorLib import stepper_abs_pos
# import stepper_abs_pos
import RpiMotorLib

ms1 = 11 # gpio pin to ms1 on A4988
ms2 = 9 # gpio pin to ms2 on A4988
ms3 = 10 # gpio pin to ms3 on A4988
direction = 26 # connect to direction pin on A4988
step = 19 # connect to step pin on A4988
step_control_pins = (ms1, ms2, ms3) # needs a list (or array apparently) to put into 
stepper_pos = 0

stepper = stepper_abs_pos.StepperAbsPos(direction, step, step_control_pins, "A4988")

step_type = 'Full'
step_delay = .005
init_delay = .005
pos_lst = [25, 45, 190, 0, 10, 100, 15, 0]


while True:
    for pos in pos_lst:
        try:
            stepper.abs_motor_go(pos, step_type, step_delay, init_delay)
            print(pos)
        except (KeyboardInterrupt, SystemExit):
            print('nope')
            print('exiting!')
            raise
        