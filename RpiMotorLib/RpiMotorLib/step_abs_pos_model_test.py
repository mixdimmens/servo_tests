import random
import csv
import step_abs_pos_model_class_test
# from RpiMotorLib import step_abs_pos_model_class_test
# import StepTest

cycles = 100

stepper_position = 0
direction_pin = 0
testr = step_abs_pos_model_class_test.StepTest(stepper_position, direction_pin)

end_position = []

for i in range(cycles):
    end_position.append(random.randint(0,200))
# print(end_position)

steptype = 'Full'
stepdelay = .01
initdelay = .01

with open('step_simulation_2.csv', 'w', newline= '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter= ',')
    for n in range(cycles):
        testr.abs_motor_go(end_position[n], steptype, stepdelay, initdelay, extra_revs= 0, stepper_position= 0)
        out_list = [end_position[n]]
        for m in testr.to_csv():
            out_list.append(m)
            print(m)
        csvwriter.writerow(out_list)
        # print(testr)
        # csvwriter.writerow()
        # print(testr)


