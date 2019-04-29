import csv
import math
import matplotlib.pyplot as plt

def flip_ang(end_pos):
    ang_flipped = 360 - (int(end_pos) / 200 * 360)
    return ang_flipped

# - imported csv row values - #
# [end_position[n], self.inner_steps, self.outer_steps, self.stepper_position, self.direction, self.extra_revs]
csvfile = 'step_simulation.csv'
values = []
with open(csvfile ) as csvfile:
    readr = csv.reader(csvfile, delimiter=',', quotechar= '|')
    for row in readr:
        values.append(row)

## - change row value to plot different movements from csv file - ##
row = 1

# - end position calculations - #
end_ang = flip_ang(values[row][0])
end_rise = math.cos(end_ang)
end_run = math.sin(end_ang)
if end_run == 0:
    end_slope = 0
else:
    end_slope = end_rise/end_run
print('end angle: {}'.format(end_slope))
if end_ang >= 180:
    end_ang_x_pnts = [i for i in range(-10, 0 , 1)]
    end_ang_y_pnts = [end_slope * i for i in end_ang_x_pnts]
else:
    end_ang_x_pnts = [i for i in range(0, 10, 1)]
    end_ang_y_pnts = [end_slope * i for i in end_ang_x_pnts]

# - start position calcualtions - #
if row > 0:
    start_ang = flip_ang(values[row-1][0])
else:
    start_ang = 0
start_rise = math.cos(start_ang)
start_run = math.sin(start_ang)
if start_run == 0:
    start_slope = 0
else:
    start_slope = start_rise / start_run

print('start angle: {}'.format(start_slope))
if start_ang >= 180:
    start_ang_x_pnts = [i for i in range(-10, 1, 1)]
    start_ang_y_pnts = [start_slope * i for i in start_ang_x_pnts]
else:
    start_ang_x_pnts = [i for i in range(-1, 10, 1)]
    start_ang_y_pnts = [start_slope * i for i in start_ang_x_pnts]

# - direction of movment - #
if values[row][4] == True:
    direction = 'clockwise'
else:
    direction = 'counter-clockwise'

# - plot thst shit - #
pltr = plt.subplot(111)
pltr.plot(end_ang_x_pnts, end_ang_y_pnts, label= 'end position')
pltr.plot(start_ang_x_pnts, start_ang_y_pnts, label= 'start posistion')
plt.ylim(-10, 10)
plt.xlim(-10, 10)
plt.legend()
plt.title('start:{}, end:{}, inside:{}, outside:{}, direction: {}'.format(start_ang, end_ang, flip_ang(values[row][1]), flip_ang(values[row][2]), direction))
plt.show()