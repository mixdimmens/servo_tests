import csv
import matplotlib.pyplot as plt

# - imported csv row values - #
# testr.abs_motor_go(end_position[n], steptype, stepdelay, initdelay, extra_revs= 0, stepper_position= 0)
csvfile = 'step_simulation.csv'
values = []
with open(csvfile ) as csvfile:
    readr = csv.reader(csvfile, delimiter=',', quotechar= '|')
    for row in readr:
        values.append(row)

## - change row value to plot different movements from csv file - ##
row = 1

# - pyplot setup - #
rmax = 2
rticks = [0.5, 1, 1.5, 2]
rlabel = -90
title = 'hows this look?'
plots = plt.subplot(111, projection='polar')
plots.set_rmax(rmax)
plots.set_rticks(rticks)
plots.set_rlabel_position(rlabel)
plots.set_title(title)

# - end position  ray- #
end_ray = [i for i in range(200)]
end_angle = int(values[row][0])/200 * 360
print(end_angle)
step_end_pos = [end_angle for i in range(200)]
# print(step_end_pos)
plots.plot(step_end_pos, end_ray, label= 'end position')

# - start position ray - #
start_ray = [i for i in range(200)]
if row > 0:
    start_angle = int(values[row-1][0]) /200 * 360
    step_start_pos = [start_angle for i in range(200)]
else:
    step_start_pos = [0 for i in range(200)]
plots.plot(step_start_pos, start_ray, label= 'start position')

# - inner move - $
inner_tracer = [i for i in range(int(values[row][0]))]
inner_rad = [.075 for i in range(int(values[row][0]))]
# plots.plot(inner_rad, inner_tracer, label= 'inner tracer')

# - outer position - #
outer_tracer = [i for i in range(int(values[0][1]))]
outer_radius = 1.5

plt.legend()
plt.show()