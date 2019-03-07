#!/usr/bin/env python3
"""A python 3 library for various
 motors and servos to connect to a raspberry pi"""
# ========================= HEADER ===================================
# title             :rpiMotorlib.py
# description       :A python 3 library for various motors
# and servos to connect to a raspberry pi
# This file is for stepper motor tested on
# 28BYJ-48 unipolar stepper motor with ULN2003  = BYJMotor class
# Bipolar Nema stepper motor with L298N = BYJMotor class.
# Bipolar Nema Stepper motor A4988  Driver = A4988Nema class
# Bipolar Nema Stepper motor DRV8825 Driver = A4988Nema class
# Bipolar Nema Stepper motor A3967 Easy Driver = A3967EasyNema class
# author            :Gavin Lyons
# Date created      :See changelog at url
# Version           ;See changelog at url
# url               :https://github.com/gavinlyonsrepo/RpiMotorLib
# mail              :glyons66@hotmail.com
# python_version    :3.4.2

# ========================== IMPORTS ======================
# Import the system modules needed to run rpiMotorlib.py
import sys
import time
import RPi.GPIO as GPIO

# ==================== CLASS SECTION ===============================


class A4988Nema(object):
    """ Class to control a Nema bi-polar stepper motor with a A4988 also tested with DRV8825"""
    def __init__(self, direction_pin, step_pin, mode_pins, motor_type="A4988"):
        """ class init method 3 inputs
        (1) direction type=int , help=GPIO pin connected to DIR pin of IC
        (2) step_pin type=int , help=GPIO pin connected to STEP of IC
        (3) mode_pins type=tuple of 3 ints, help=GPIO pins connected to
        Microstep Resolution pins MS1-MS3 of IC
        (4) motor_type type=string, help=TYpe of motor two options: A4988 or DRV8825
        """
        self.motor_type = motor_type
        self.direction_pin = direction_pin
        self.step_pin = step_pin
        self.mode_pins = mode_pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def resolution_set(self, steptype):
        """ method to calculate step resolution
        based on motor type and steptype"""
        if self.motor_type == "A4988":
            resolution = {'Full': (0, 0, 0),
                          'Half': (1, 0, 0),
                          '1/4': (0, 1, 0),
                          '1/8': (1, 1, 0),
                          '1/16': (1, 1, 1)}
        elif self.motor_type == "DRV8825":
            resolution = {'Full': (0, 0, 0),
                          'Half': (1, 0, 0),
                          '1/4': (0, 1, 0),
                          '1/8': (1, 1, 0),
                          '1/16': (0, 0, 1),
                          '1/32': (1, 0, 1)}
        else: 
            print("Error invalid motor_type: {}".format(steptype))
            quit()
        
        # error check stepmode
        if steptype in resolution:
            pass
        else:
            print("Error invalid steptype: {}".format(steptype))
            quit()

        GPIO.output(self.mode_pins, resolution[steptype])

    def motor_go(self, clockwise=False, steptype="Full",
                 steps=200, stepdelay=.005, verbose=False, initdelay=.05):
        """ motor_go,  moves stepper motor based on 6 inputs

         (1) clockwise, type=bool default=False
         help="Turn stepper counterclockwise"
         (2) steptype, type=string , default=Full help= type of drive to
         step motor 5 options
            (Full, Half, 1/4, 1/8, 1/16)
         (3) steps, type=int, default=200, help=Number of steps sequence's
         to execute. Default is one revolution , 200 in Full mode.
         (4) stepdelay, type=float, default=0.05, help=Time to wait
         (in seconds) between steps.
         (5) verbose, type=bool  type=bool default=False
         help="Write pin actions",
         (6) initdelay, type=float, default=1mS, help= Intial delay after
         GPIO pins initialized but before motor is moved.

        """
        # setup GPIO
        GPIO.setup(self.direction_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.output(self.direction_pin, clockwise)
        GPIO.setup(self.mode_pins, GPIO.OUT)
        try:
            # dict resolution
            self.resolution_set(steptype)

            time.sleep(initdelay)

            for i in range(steps):
                GPIO.output(self.step_pin, True)
                time.sleep(stepdelay)
                GPIO.output(self.step_pin, False)
                time.sleep(stepdelay)
                if verbose:
                    print("Steps count {}".format(i))

        except KeyboardInterrupt:
            print("User Keyboard Interrupt : RpiMotorLib:")
        except Exception as motor_error:
            print(sys.exc_info()[0])
            print(motor_error)
            print("RpiMotorLib  : Unexpected error:")
        else:
            # print report status
            if verbose:
                print("\nRpiMotorLib, Motor Run finished, Details:.\n")
                print("Motor type = {}".format(self.motor_type))
                print("Clockwise = {}".format(clockwise))
                print("Step Type = {}".format(steptype))
                print("Number of steps = {}".format(steps))
                print("Step Delay = {}".format(stepdelay))
                print("Intial delay = {}".format(initdelay))
                print("Size of turn in degrees = {}"
                      .format(degree_calc(steps, steptype)))
        finally:
            # cleanup
            GPIO.output(self.step_pin, False)
            GPIO.output(self.direction_pin, False)
            for pin in self.mode_pins:
                GPIO.output(pin, False)


def degree_calc(steps, steptype):
    """ calculate and returns size of turn in degree
    , passed number of steps and steptype"""
    degree_value = {'Full': 1.8,
                    'Half': 0.9,
                    '1/4': .45,
                    '1/8': .225,
                    '1/16': 0.1125,
                    '1/32': 0.05625}
    degree_value = (steps*degree_value[steptype])
    return degree_value


def importtest(text):
    """ testing import """
    # print(text)
    text = " "


class StepperAbsPos(A4988Nema):
    stepper_position = 0
    direction = True
#class StepperAbsPos: # for debugging the class, yo
    # note stepper_position must preceed motor_type or sepper _ will default to <str> type
    def __init__(self, direction_pin, step_pin, mode_pins, motor_type):
        super(A4988Nema).__init__(direction_pin, step_pin, mode_pins, motor_type)

    ## method golbal zeroes stepper absolute position
    def new_home(self):
        self.stepper_position = 0

    ## tracks movement of an object in a revolution ##
    def abs_position(self, steps, direction):
        steps_per_rev = 200
        self.steps = steps
#        self.direction = direction
        if self.stepper_position > steps_per_rev:
            print('problem! motor position is {}, which is greater than the number of steps per revolution ({})'.format(self.stepper_position, steps_per_rev))
        else:
            if direction == True:
                self.stepper_position = int(self.stepper_position + self.steps)
                if self.stepper_position == steps_per_rev:
                    self.stepper_position = 0
                elif self.stepper_position > steps_per_rev:
                    reducer = int((self.stepper_position // steps_per_rev) * steps_per_rev)
                    self.stepper_position = int(self.stepper_position - reducer)
            
            else:
                self.stepper_position = int(self.stepper_position + (self.steps * -1))
                # print(self.stepper_position)
                if self.stepper_position < 0:
                    if self.stepper_position >= -199:
                        self.stepper_position = int(steps_per_rev + self.stepper_position)
                    else:
                        reducer = (self.stepper_position // -steps_per_rev) * steps_per_rev
                        # print(reducer)
                        self.stepper_position = int(steps_per_rev + (self.stepper_position + reducer))
        if self.stepper_position == steps_per_rev:
            self.stepper_position = 0

    def opposite_pole(self, stepper_position):
        #pylint: disable=unused-argument
        self.opposing_pole = 0
        if self.stepper_position == 0 or self.stepper_position == 200:
            self.opposing_pole = 100
        elif self.stepper_position < 100:
            self.opposing_pole = self.stepper_position + 100
        elif self.stepper_position >= 100:
            self.opposing_pole = self.stepper_position - 100
        return self.opposing_pole

    def abs_motor_go(self, end_position, steptype, stepdelay, initdelay, extra_revs = 0):
        self.end_position = end_position
        self.extra_revs = extra_revs
        inner_steps = 0
        outer_steps = 0
        print(type(self.direction_pin))

        if self.stepper_position > self.end_position:
            inner_steps = self.stepper_position - self.end_position
            outer_steps = (200 - self.stepper_position) + self.end_position
            print('inner steps {}, outer steps {}'.format(inner_steps, outer_steps))
        elif self.end_position > self.stepper_position:
            inner_steps = self.end_position - self.stepper_position
            outer_steps = (200 - self.end_position) + self.stepper_position
            print('inner steps {}, outer steps {}'.format(inner_steps, outer_steps))

        if inner_steps == outer_steps:
            self.direction = True
        elif inner_steps > outer_steps:
            if self.stepper_position > self.end_position:
                self.direction = True
            elif self.end_position > self.stepper_position:
                self.direction = False
        elif outer_steps > inner_steps:
            if self.stepper_position > self.end_position:
                self.direction = False
            elif self.end_position > self.stepper_position:
                self.direction = True

        print('direction {}'.format(self.direction))            
        if outer_steps == inner_steps and self.extra_revs == 0:
            pass
        elif outer_steps == inner_steps and self.extra_revs != 0:
            self.extra_revs = self.extra_revs * 200
            A4988Nema.motor_go(self.direction, steptype, self.extra_revs, stepdelay, False, initdelay, 0)
            print('moved {} (previous rotation direction)'.format(self.extra_revs))
        elif outer_steps < inner_steps:
            outer_steps += (self.extra_revs * 200)
            A4988Nema.motor_go(self.direction, steptype, outer_steps, stepdelay, False, initdelay, 0)
            print('moved {} (outer steps)'.format(outer_steps))
            self.abs_position(outer_steps, self.direction)
        elif inner_steps < outer_steps:
            inner_steps += (self.extra_revs * 200)
            print(self.direction_pin)
            A4988Nema.motor_go(self.direction, steptype, inner_steps, stepdelay, False, initdelay, 0)
            print('moved {} (inner steps)'.format(inner_steps))
            self.abs_position(inner_steps, self.direction)

    def __repr__(self):
        return "abs pos: {}".format(self.stepper_position)

        
# ===================== MAIN ===============================


if __name__ == '__main__':
    importtest("main")
else:
    importtest("Imported {}".format(__name__))


# ===================== END ===============================
