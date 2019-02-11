# attempt to use PWM to control servo B)

import time
import RPi.GPIO as GPIO


print('hiya!')
print('lets get this started. perftcount: {}'.format(time.perf_counter()))

# converts angles to input value for servo object input:
def servo_ang(angle):
    # full range for servo input : 2.5 - 12.5
    if angle <= 180:
        out = ((float(int((angle * (1.05 / 18) + 0) * 10))) / 10)
        out += 2.5
        if out > 12.5:
          out = 12.5
          return out
        else:
          return out
    else:
        print('angle out of range!')
#print(servo_ang(10))


pin = 8 # only pwm hardware pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT, initial = 0)
freq = 50 # in hz
servo = GPIO.PWM( pin , freq)
servo.start(servo_ang(90))

print('loop starting at: {}'.format(time.perf_counter()))
count = 1
try:
    while count < 3:
        print(count)

        servo.ChangeDutyCycle(servo_ang(20))
        time.sleep(1)

        servo.ChangeDutyCycle(servo_ang(100))
        time.sleep(2)

        #servo.ChangeDutyCycle(servo_ang(0))
        #time.sleep(2)

        count += 1

except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()

servo.stop()
print('{} cycles executed. completed at: {}'.format(count, time.perf_counter()))
GPIO.cleanup()


    