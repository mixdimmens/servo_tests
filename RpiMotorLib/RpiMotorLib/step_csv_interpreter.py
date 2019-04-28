import csv


# csv_lst = [self.inner_steps, self.outer_steps, self.direction_pin, self.extra_revs]
csvfile = 'step_simulation.csv'
values = []
with open(csvfile, ) as csvfile:
    readr = csv.reader(csvfile, delimiter=',', quotechar= '|')

    for row in readr:
        values.append(row)

print(values)



