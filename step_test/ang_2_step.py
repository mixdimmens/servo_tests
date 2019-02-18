class StepperAbsAngle:

    def __init__(self, shaft_position):
        self.shaft_position = shaft_position


    def AbsPosition(self, rotation_amount, direction):
        self.rotation_amount = rotation_amount
        self.direction = direction

        if self.direction == True:
            if self.rotation_amount % 200 == 0:
                self.rotation_amount = 0
        elif self.direction != True:
            if self.rotation_amount == 0:
                self.rotation_amount = 200

        elif self.rotation_amount > 200:
            self.rotation_amount = self.rotation_amount - ((self.rotation_amount // 200) * 200)
        
        if self.direction != True:
            self.rotation_amount = self.rotation_amount * -1
        
        self.shaft_position = self.shaft_position + self.rotation_amount

        if self.shaft_position == 200:
            self.shaft_position = 0

        return self.shaft_position

    def __repr__(self):
         return '{}'.format(self.shaft_position)

stepper = StepperAbsAngle(0)

stepper.AbsPosition(30, False)
print(stepper)