import csv
# import stepper_abs_pos

positions = []
csvfile = 'step_simulation.csv'
with open(csvfile) as csvfile:
    readr = csv.reader(csvfile, delimiter=',')
    for row in readr:
        positions.append(int(row[0]))

# print(positions)
direction_pin = 0
step_pin = 1
mode_pins = [2, 3, 4]
motor_type = "A4988"
steptype = 'Full'
stepdelay = .02
initdelay = .01
stepper = stepper_abs_pos(direction_pin, step_pin, mode_pins, motor_type)
for n in positions:
    holder = input('press enter for next step')
    stepper.stepper_abs_pos(n, steptype, stepdelay, initdelay)

