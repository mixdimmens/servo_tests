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

#import sys
#import time
#import RPi.GPIO as GPIO
#import RpiMotorLib
# from RpiMotorLib import A4988Nema as A4988Nema

# class StepperAbsPos(A4988Nema):
#     stepper_position = 0
#     direction = True
# #class StepperAbsPos: # for debugging the class, yo
#     # note stepper_position must preceed motor_type or stepper _ will default to <str> type
#     def __init__(self, direction_pin, step_pin, mode_pins, motor_type):
#         super().__init__(direction_pin, step_pin, mode_pins, motor_type)

#     ## method golbal zeroes stepper absolute position
#     def new_home(self):
#         self.stepper_position = 0

class StepTest():
    direction = True
    inner_steps = 0
    outer_steps = 0
    def __init__(self, stepper_position, direction_pin):
        self.stepper_position = stepper_position
        # self.end_position = end_position
        self.direction_pin = direction_pin
    ## tracks movement of an object in a revolution ##
    def abs_position(self, steps, direction):
        steps_per_rev = 200
        self.steps = steps
#        self.direction = direction
        if self.stepper_position > steps_per_rev:
            print('problem! motor position is {}, which is greater than the number of steps per revolution ({})'.format(self.stepper_position, steps_per_rev))
        else:
            if direction == True:
                self.stepper_position = int(self.stepper_position + self.steps)
                if self.stepper_position == steps_per_rev:
                    self.stepper_position = 0
                elif self.stepper_position > steps_per_rev:
                    reducer = int((self.stepper_position // steps_per_rev) * steps_per_rev)
                    self.stepper_position = int(self.stepper_position - reducer)
            
            else:
                self.stepper_position = int(self.stepper_position + (self.steps * -1))
                # print(self.stepper_position)
                if self.stepper_position < 0:
                    if self.stepper_position >= -199:
                        self.stepper_position = int(steps_per_rev + self.stepper_position)
                    else:
                        reducer = (self.stepper_position // -steps_per_rev) * steps_per_rev
                        # print(reducer)
                        self.stepper_position = int(steps_per_rev + (self.stepper_position + reducer))
        if self.stepper_position == steps_per_rev:
            self.stepper_position = 0

#     def opposite_pole(self, stepper_position):
#         #pylint: disable=unused-argument
#         self.opposing_pole = 0
#         if self.stepper_position == 0 or self.stepper_position == 200:
#             self.opposing_pole = 100
#         elif self.stepper_position < 100:
#             self.opposing_pole = self.stepper_position + 100
#         elif self.stepper_position >= 100:
#             self.opposing_pole = self.stepper_position - 100
#         return self.opposing_pole

    def abs_motor_go(self, end_position, steptype, stepdelay, initdelay, extra_revs= 0, stepper_position= 0):
        self.stepper_position = stepper_position
        self.end_position = end_position
        self.extra_revs = extra_revs
        self.inner_steps = 0
        self.outer_steps = 0
        steps_per_rev = 200
        # print(type(self.direction_pin))

        ## automatic steptype compensation :P
        if steptype == "Full":
            steps_per_rev = 200
        elif steptype == 'Half':
            steps_per_rev = 400
        elif steptype == '1/4':
            steps_per_rev = 800
        elif steptype == '1/8':
            steps_per_rev = 1600
        elif steptype == '1/16':
            steps_per_rev = 3200

### THIS CODE  HERE THO ###
        if self.stepper_position > self.end_position:
            self.inner_steps = self.stepper_position - self.end_position
            self.outer_steps = (steps_per_rev - self.stepper_position) + self.end_position
            # print('inner steps {}, outer steps {}'.format(self.inner_steps, self.outer_steps))
        elif self.end_position > self.stepper_position:
            self.inner_steps = self.end_position - self.stepper_position
            self.outer_steps = (steps_per_rev - self.end_position) + self.stepper_position
            # print('inner steps {}, outer steps {}'.format(self.inner_steps, self.outer_steps))

        if self.inner_steps == self.outer_steps:
            self.direction = True
        elif self.inner_steps > self.outer_steps:
            if self.stepper_position > self.end_position:
                self.direction = True
            elif self.end_position > self.stepper_position:
                self.direction = False
        elif self.outer_steps > self.inner_steps:
            if self.stepper_position > self.end_position:
                self.direction = False
            elif self.end_position > self.stepper_position:
                self.direction = True

        # print('direction {}'.format(self.direction))            
        if self.outer_steps == self.inner_steps and self.extra_revs == 0:
            pass
        elif self.outer_steps == self.inner_steps and self.extra_revs != 0:
            self.extra_revs = self.extra_revs * steps_per_rev
            # self.motor_go(self.direction, steptype, self.extra_revs, stepdelay, False, initdelay)
            # print('moved {} (previous rotation direction)'.format(self.extra_revs))
        elif self.outer_steps < self.inner_steps:
            self.outer_steps += (self.extra_revs * steps_per_rev)
            # self.motor_go(self.direction, steptype, self.outer_steps, stepdelay, False, initdelay)
            # print('moved {} (outer steps)'.format(self.outer_steps))
            self.abs_position(self.outer_steps, self.direction)
        elif self.inner_steps < self.outer_steps:
            self.inner_steps += (self.extra_revs * steps_per_rev)
            # print(self.direction_pin)
            # self.motor_go(self.direction, steptype, self.inner_steps, stepdelay, False, initdelay)
            # print('moved {} (inner steps)'.format(self.inner_steps))
            self.abs_position(self.inner_steps, self.direction)
### TO HERE ###
    def to_csv(self):
        csv_lst = [self.inner_steps, self.outer_steps, self.stepper_position, self.direction, self.extra_revs]
        return csv_lst

    def __repr__(self):
        return '{}, {}, {}, {}'.format(self.inner_steps, self.outer_steps, self.direction_pin, self.extra_revs)
        # return "abs pos: {}".format(self.stepper_position)

