## hey, this one works! imagine that, sitting down and planning makes things go way smoother ##
## code to track absolute angle of stepper shaft based on origin position, or on zereoed coordinate* ##
## coordinate system:
            #                150
            #                 |
            #                 |
            #                 |
            # 100 ____________|___________ 0
            #                 |\
            #                 | \
            #       outside   |  \    inside
            #                 |   \
            #                 50   self.stepper_position
            # clockwise = True
            # 
## * zeroed coordinate coming soon 
# import RpiMotorLib



# class StepperAbsPos(A4988Nema):
class StepperAbsPos: # for debugging the class, yo
    def __init__(self, direction_pin, step_pin, mode_pins, stepper_position = 0, motor_type="A4988"):
        self.direction_pin = direction_pin
        self.step_pin = step_pin
        self.mode_pins = mode_pins
        self.stepper_position = stepper_position
        self.motor_type = motor_type

    ## method golbal zeroes stepper absolute position
    def new_home(self):
        self.stepper_position = 0

    ## tracks movement of an object in a revolution ##
    def abs_position(self, steps, direction):
        steps_per_rev = 200
        self.steps = steps
        self.direction = direction
        if self.stepper_position > steps_per_rev:
            print('problem! motor position is {}, which is greater than the number of steps per revolution ({})'.format(self.stepper_position, steps_per_rev))
        else:
            if direction == True:
                self.stepper_position = self.stepper_position + self.steps
                if self.stepper_position == steps_per_rev:
                    self.stepper_position = 0
                elif self.stepper_position > steps_per_rev:
                    reducer = (self.stepper_position // steps_per_rev) * steps_per_rev
                    self.stepper_position = self.stepper_position - reducer
            
            else:
                self.stepper_position = self.stepper_position + (self.steps * -1)
                # print(self.stepper_position)
                if self.stepper_position < 0:
                    if self.stepper_position >= -199:
                        self.stepper_position = steps_per_rev + self.stepper_position
                    else:
                        reducer = (self.stepper_position // -steps_per_rev) * steps_per_rev
                        # print(reducer)
                        self.stepper_position = steps_per_rev + (self.stepper_position + reducer)
        if self.stepper_position == steps_per_rev:
            self.stepper_position = 0

    def opposite_pole(self, stepper_position):
        self.opposing_pole = 0
        if self.stepper_position == 0 or self.stepper_position == 200:
            self.opposing_pole = 100
        elif self.stepper_position < 100:
            self.opposing_pole = self.stepper_position + 100
        elif self.stepper_position >= 100:
            self.opposing_pole = self.stepper_position - 100
        return self.opposing_pole

    def abs_motor_go(self, end_position, steptype, stepdelay, initdelay, extra_revs = 0):
        self.end_position = end_position
        self.extra_revs = extra_revs
        inner_steps = 0
        outer_steps = 0

        if self.stepper_position > end_position:
            inner_steps = self.stepper_position - self.end_position
            outer_steps = (200 - self.stepper_position) + self.end_position
            print('inner steps {}, outer steps {}'.format(inner_steps, outer_steps))
        elif end_position > self.stepper_position:
            inner_steps = self.end_position - self.stepper_position
            outer_steps = (200 - self.end_position) + self.stepper_position
            print('inner steps {}, outer steps {}'.format(inner_steps, outer_steps))

        if inner_steps == outer_steps:
            self.direction = True
        elif inner_steps > outer_steps:
            if self.stepper_position > self.end_position:
                self.direction = True
            elif self.end_position > self.stepper_position:
                self.direction = False
        elif outer_steps > inner_steps:
            if self.stepper_position > self.end_position:
                self.direction = False
            elif self.end_position > self.stepper_position:
                self.direction = True

        print('direction {}'.format(self.direction))            
        if outer_steps == inner_steps and self.extra_revs == 0:
            pass
        elif outer_steps == inner_steps and self.extra_revs != 0:
            self.extra_revs = self.extra_revs * 200
            # self.motor_go(self.direction, self.extra_revs, steptype, stepdelay, False, initdelay)
            print('moved {} (previous rotation direction)'.format(self.extra_revs))
        elif outer_steps < inner_steps:
            outer_steps += (self.extra_revs * 200)
            # self.motor_go(self.auto_direction, outer_steps, steptype, stepdelay, False, initdelay)]
            print('moved {} (outer steps)'.format(outer_steps))
            self.abs_position(outer_steps, self.direction)
        elif inner_steps < outer_steps:
            inner_steps += (self.extra_revs * 200)
            # self.motor__go(self.auto_direction, inner_steps, steptype, stepdelay, False, initdelay)
            print('moved {} (inner steps)'.format(inner_steps))
            self.abs_position(inner_steps, self.direction)

    def __repr__(self):
        return "abs pos: {}".format(self.stepper_position)


## demo instance, dummy: ##

# #fill in the blanks:
# direction_pin = 19
# step_pin = 26
# mode_pins = (25,26,27)
# stepper_position = 0

# stepper = StepperAbsPos(direction_pin, step_pin, mode_pins, stepper_position, "A4988")

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

# step_type = 'Half'
# step_delay = .005
# init_delay = .005

# print(1)
# stepper.abs_motor_go(50, step_type, step_delay, init_delay)
# print(stepper)
# print('')

# print(2)
# stepper.abs_motor_go(100, step_type, step_delay, init_delay)
# print(stepper)
# print('')

# print(3)
# stepper.abs_motor_go(50, step_type, step_delay, init_delay)
# print(stepper)
# print('')

# print(4)
# stepper.abs_motor_go(70, step_type, step_delay, init_delay)
# print(stepper)
# print('')

# print(5)
# stepper.abs_motor_go(180, step_type, step_delay, init_delay)
# print(stepper)
# print('')

# print(6)
# stepper.abs_motor_go(5, step_type, step_delay, init_delay)
# print(stepper)
# print('')

# print(7)
# stepper.abs_motor_go(0, step_type, step_delay, init_delay)
# print(stepper)
# print('')

# print(8)
# stepper.abs_motor_go(100, step_type, step_delay, init_delay, 1)
# print(stepper)
# print('')