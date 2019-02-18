# def angle_to_step(angle):
#     #self.angle = int(input('enter angle of change from current position'))
#     steps = int((angle * 200)/360)
#     print(steps)

# # angle_to_step(720)


# shaft_position = 0

# def shaft_position_counter(steps, direction, total_spin):
    
#     if direction == True:
#         total_spin += steps
#     elif direction != True:
#         total_spin = total_spin - steps
#     return total_spin

# # shaft_position = shaft_position_counter(200, True, shaft_position)
# # shaft_position = shaft_position_counter(100, False, shaft_position)
# # shaft_position = shaft_position_counter(50, True, shaft_position)
# # print(shaft_position_counter(30, False, shaft_position))
# # shaft_position = shaft_position_counter(30, False, shaft_position)
# # print('shaft position: {}'.format(shaft_position))

# shaft_position = 0

# print('shaft position: {}'.format(shaft_position))
# shaft_angle = shaft_position_counter
# shaft_angle(300, True, shaft_position)
# print(shaft_angle(120, False, shaft_position))

class ShaftPositionCounter:
    def __init__(self, shaft_position):
        self.shaft_position = shaft_position
    
    ## track position of shaft relative to location upon initialization
    def ShaftPositionChange(self, delta_rotation, direction):
        self.delta_rotation = delta_rotation
        self.direction = direction

        # if self.shaft_position == 0 and self.direction != True:
        #     self.shaft_position = 200

        if self.delta_rotation > 200 or self.delta_rotation < -200:
            reducer = (self.delta_rotation // 200) * 200
            self.delta_rotation = self.delta_rotation - reducer

        if self.direction != True:
            self.delta_rotation = self.delta_rotation * -1
            print(self.delta_rotation)
        
        if self.shaft_position == 0 and self.direction != True:
            self.shaft_position = 200

        self.shaft_position += self.delta_rotation
        
        if self.shaft_position == 200:
            self.shaft_position = 0
        elif self.shaft_position > 200:
            reducer = (self.shaft_position // 200) * 200
            self.shaft_position = self.shaft_position - reducer

        return self.shaft_position

    ## output angle change from current location. arguments using initialization 
    ## coordinates as final position decription. direction determined by argument
 #   def ShaftPositionRelative(self,relative_position_end, direction):

    
    def __repr__(self):
        return '{}'.format(self.shaft_position)

# shaft = ShaftPositionCounter(0)
# shaft.ShaftPositionChange(100, True)
# print('move 1 {}'.format(shaft))
# shaft.ShaftPositionChange(300, False)
# print('move 2 {}'.format(shaft))
# shaft.ShaftPositionChange(150, True)
# print('move 3 {}'.format(shaft))
# shaft.ShaftPositionChange(300, False)
# print('move 4 {}'.format(shaft))

shaft = ShaftPositionCounter(0)
shaft.ShaftPositionChange(75, False)
print('move 1 {}'.format(shaft))
shaft.ShaftPositionChange(125, True)
print('move 2 {}'.format(shaft))
shaft.ShaftPositionChange(175, False)
print('move 3 {}'.format(shaft))
shaft.ShaftPositionChange(200, False)
print('move 4 {}'.format(shaft))