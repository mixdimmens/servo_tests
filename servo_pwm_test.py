## https://learn.adafruit.com/adafruit-16-channel-pwm-servo-hat-for-raspberry-pi/using-the-python-library
## ^^ where this from ^^
## go there if it dont work


import time
import board
import busio
import adafruit_pca9685
i2c = busio.I2C(board.SCL. boad.SDA)
hat = adafruit_pca9685.PCA9865(i2c)

## set hat freq. - this will not varry across pins. function input is the freq in hz
hat.frequency = 60

## set channel variable by calling
number = 0 ## variable for hat.channel call
varibale_name = hat.channel[number]

for i in range(5)
    print(i)
    time.sleep(5) ## long delay so we know where we are
    
    ## set duty cycle of a channel by calling .duty_cycle(value). value can be between 0 and 0xffff
    varibale_name.duty_cycle = 0xffff ## full duty cyle

    time.sleep(1)
    ## duty cycles dont like to go to zero for servos - chintzy servos want 2% (or there abouts)
    ## at minimum - zero causes erratic behavior
    varibale_name.duty_cycle = 0x5ff

    time.sleep(1)

print('done!')
