## hey, this one works! imagine that, sitting down and planning makes things go way smoother ##
## code to track absolute angle of stepper shaft based on origin position, or on zereoed coordinate ##
import RpiMotorLib


class StepperAbsPos(A4988Nema):
    def __init__(self, stepper_position):
        self.stepper_position = stepper_position

    def new_home(self):
        self.stepper_position = 0

    ## tracks movement of an object in a revolution ##
    ## will need to modify so it can feed into abs_move_calc
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
                print(self.stepper_position)
                if self.stepper_position < 0:
                    if self.stepper_position >= -199:
                        self.stepper_position = steps_per_rev + self.stepper_position
                    else:
                        reducer = (self.stepper_position // -steps_per_rev) * steps_per_rev
                        print(reducer)
                        self.stepper_position = steps_per_rev + (self.stepper_position + reducer)
        if self.stepper_position == steps_per_rev:
            self.stepper_position = 0

    ## figures out the difference between where the motor is and where the motor wants to go.
    ## two modes, shortest path, and user chosen direction of rotation.
    def abs_move_calc(self, end_position):
        self.end_position = end_position
        
        self.abs_pos_to_home = self.steps - self.stepper_position
        self.end_position_to_home = self.steps - self.end_position

        if self. abs_pos_to_home == self.end_position_to_home:
            pass
        elif self.abs_pos_to_home > self.end_position_to_home:
            self.direction = True
            self.abs_move = self.stepper_position - self.end_position
        elif self.end_position_to_home > self.abs_pos_to_home:
            self.direction = False
            self.abs_move = self.end_position - self.stepper_position
        
        try:
            self.motor_go(self.direction, self.steptype, self.abs_move, self.stepdelay, self.verbose, self.initdelay)

            self.abs_position(self.abs_move, self.direction)
        
        except:
            KeyboardInterrupt

    def __repr__(self):
        return '{}'.format(self.stepper_position)

stepper = StepperAbsPos(201)

stepper.abs_position(635, False)
print('stepper position 1: {}'.format(stepper))
stepper.abs_position(135, True)
print('stepper position 2: {}'.format(stepper))
stepper.abs_position(135, True)
print('stepper position 3: {}'.format(stepper))
# stepper.new_home()
# print(stepper)
