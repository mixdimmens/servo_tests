pos_lst = [25, 45, 190, 0, 10, 100, 15, 0]

while True:
    for pos in pos_lst:
        try:
            print(pos)
#            else:
#                break
        except (KeyboardInterrupt, SystemExit):
            print('nope')
            print('exiting!')
            raise
            