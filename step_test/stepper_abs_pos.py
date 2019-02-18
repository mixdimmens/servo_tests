## hey, this one works! imagine that, sitting down and planning makes things go way smoother ##
## code to track absolute angle of stepper shaft based on origin position, or on zereoed coordinate ##

class StepperAbsPos:
    def __init__(self, stepper_position):
        self.stepper_position = stepper_position

    def new_home(self):
        self.stepper_position = 0

    def abs_position(self, steps, direction):
        self.steps = steps
        self.direction = direction
        if self.stepper_position > 200:
            print('problem! motor position is {}, which is greater than 200'.format(self.stepper_position))
        else:
            if direction == True:
                self.stepper_position = self.stepper_position + self.steps
                if self.stepper_position == 200:
                    self.stepper_position = 0
                elif self.stepper_position > 200:
                    reducer = (self.stepper_position // 200) * 200
                    self.stepper_position = self.stepper_position - reducer
            
            else:
                self.stepper_position = self.stepper_position + (self.steps * -1)
                print(self.stepper_position)
                if self.stepper_position < 0:
                    if self.stepper_position >= -199:
                        self.stepper_position = 200 + self.stepper_position
                    else:
                        reducer = (self.stepper_position // -200) * 200
                        print(reducer)
                        self.stepper_position = 200 + (self.stepper_position + reducer)
        if self.stepper_position == 200:
            self.stepper_position = 0

    def __repr__(self):
        return '{}'.format(self.stepper_position)

stepper = StepperAbsPos(0)

stepper.abs_position(635, False)
print('stepper position 1: {}'.format(stepper))
stepper.abs_position(135, True)
print('stepper position 2: {}'.format(stepper))
stepper.abs_position(135, True)
print('stepper position 3: {}'.format(stepper))
# stepper.new_home()
# print(stepper)
