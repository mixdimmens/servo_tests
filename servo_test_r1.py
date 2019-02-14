import time
import Rpi.GPIO as GPIO

servo_pin = 8 # or whatever it is - lets check
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT, initial = 0)
freq = 50 # value translates to hz
servo = GPIO.PWM(servo_pin, freq)
servo.start(7.5)

t_m = time.strftime('%M', time.localtime())
t_s = time.strftime('%S', time.localtime())
print(t_m)
print(t_s)

if t_s < 30:
    while t_m < t_m + 1:
        servo.ChangeDutyCycle(14)
        print('duty cycle 14')
        time.sleep(2)

        servo.ChangeDutyCycle(2.5)
        print('duty cycle 2.5')
        time.sleep(3)

        print('restart cycle! sleep time 1 sec before restart')
        time.sleep(1)
elif t_s > 30:
    while t_m < t_m + 2:
        servo.ChangeDutyCycle(14)
        print('duty cycle 14')
        time.sleep(2)

        servo.ChangeDutyCycle(2.5)
        print('duty cycle 2.5')
        time.sleep(3)

        print('restart cycle! sleep time 1 sec before restart')
        time.sleep(1)

GPIO.cleanup()
print('pins cleaned! - end of program, yo')
