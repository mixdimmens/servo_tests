def angle_to_step(angle):
    #angle = int(input('enter angle of change from current position'))
    steps = int((angle * 200)/360)
    print(steps)

angle_to_step(300)