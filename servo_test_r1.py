## program to test-drive a tower SG90 hoobby servo - works
## check notes within code for topics of further R&D
#
import time
import RPi.GPIO as GPIO
#
servo_pin = 12 # board pin does not seem to use hardware
# PWM - research suggests only board pin 18 does so,
# although this informations may be for older model RPi's
# that being said, this pin (marked PWM0 as oppose to PWM1)
# does seem to preform more stabily than gpure software
# driven PWM on non PWM marked pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT, initial = 0)
freq = 50 # value translates to hz
servo = GPIO.PWM(servo_pin, freq)
servo.start(7.5)

t_m = int(time.strftime('%M', time.localtime()))
t_s = int(time.strftime('%S', time.localtime()))
print(t_m)
print(t_s)

time_var = True

#if t_s < 30:
while time_var == True:
    servo.ChangeDutyCycle(12)
    print('duty cycle 12')
    print(time.strftime('%M:%S', time.localtime()))
    time.sleep(2)

    servo.ChangeDutyCycle(2.5)
    print('duty cycle 2.5')
    print(time.strftime('%M:%S', time.localtime()))
    print('t_m: {}'.format(t_m))
    print('t_s: {}'.format(t_s))
    print(time_var)
    time.sleep(3)

    print('restart cycle! sleep time 1 sec before restart')
    time.sleep(1)
    if t_m + 1 == int(time.strftime('%M', time.localtime())) and t_s == int(time.strftime('%S', time.localtime())):
        time_var = False
#elif t_s > 30:
#    while t_m < t_m + 1:
#        servo.ChangeDutyCycle(12)
#        print('duty cycle 12')
#        print(time.strftime('%M:%S', time.localtime()))
#        time.sleep(2)
#
#        servo.ChangeDutyCycle(2.5)
#        print('duty cycle 2.5')
#        print(time.strftime('%M:%S', time.localtime()))
#        print('t_m: {}'.fomrat(t_m))
#        print(t_m + 1)
#        time.sleep(3)
#
#        print('restart cycle! sleep time 1 sec before restart')
#        time.sleep(1)

GPIO.cleanup()
print('pins cleaned! - end of program, yo')
