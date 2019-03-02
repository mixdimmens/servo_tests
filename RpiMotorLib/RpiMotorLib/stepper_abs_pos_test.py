import stepper_abs_pos
import RpiMotorLib

## demo instance, dummy: ##

# #fill in the blanks:

ms1 = 11 # gpio pin to ms1 on A4988
ms2 = 9 # gpio pin to ms2 on A4988
ms3 = 10 # gpio pin to ms3 on A4988
direction = 26 # connect to direction pin on A4988
step = 19 # connect to step pin on A4988
step_control_pins = (ms1, ms2, ms3) # needs a list (or array apparently) to put into 
stepper_pos = 0

## confirm A4988Nema classworks independently:


stepper_tester = RpiMotorLib.A4988Nema(direction, step, step_control_pins, 'A4988')

stepper_tester.motor_go()
#except AttributeError:
#    print("it's not working, yo! wtf?")
#except NameError:
#    print("now we're really confused")
#else:
#    print("it's wworking here!")


#print(type(direction__pin))
stepper = stepper_abs_pos.StepperAbsPos(direction, step, step_control_pins, "A4988")

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

#try:
print(1)
print(stepper)
print('')

    # no movement - need to debug
print(2)
stepper.abs_motor_go(100, step_type, step_delay, init_delay)
print(stepper)
print('')

print(3)
stepper.abs_motor_go(50, step_type, step_delay, init_delay)
print(stepper)
print('')
#except AttributeError:
#    print("we're still getting this fucking error, wtf?")
#else:
#    print("well, it's working now for an unkown reason")

#print(4)
#stepper.abs_motor_go(70, step_type, step_delay, init_delay)
#print(stepper)
#print('')
#
#print(5)
#stepper.abs_motor_go(180, step_type, step_delay, init_delay)
#print(stepper)
#print('')
#
#print(6)
#stepper.abs_motor_go(5, step_type, step_delay, init_delay)
#print(stepper)
#print('')
#
#print(7)
#stepper.abs_motor_go(0, step_type, step_delay, init_delay)
#print(stepper)
#print('')
#
#print(8)
#stepper.abs_motor_go(100, step_type, step_delay, init_delay, 1)
#print(stepper)
#print('')