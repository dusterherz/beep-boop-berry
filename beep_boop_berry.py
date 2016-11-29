"""Beep Boop Berry

This module can make your Raspberry sing if you have a Piezzo-Beeper connected
to it.

Todo:
    * EVERYTHING
    * Make some examples
    * A tutorial to connect a buzzer and make it sing the Imperial March
"""

from Enum import IntEnum
from RPi.GPIO as GPIO
import time


class BeepBoop():
    """
    The main class of the module. Without that, you can't make a sound. It needs
    the pin where the buzzer is connected to be initialize.

    Attributes :
        pin (int): the pin where the buzzer is connected
    """
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def beep(time):
        """
            Make your beeper to sing a small *Beep*.
            time is the duration of the beep in seconds
        """
        delay = 1 / 440 / 2
        cycles = int(duration * pitch)

        for i in range(cycles):
            GPIO.output(self.pin, True)
            time.sleep(delay)
            GPIO.output(self.pin, False)
            time.sleep(delay)

    def beeps(time, repeat):
        """
            Make your beeper to sing multiples *Beep*.
            time is the duration of the beep in seconds
            repeat correspond to the numer of time the beeper must beep.

        """

        for i in range(repeat):
            self.beep(time)
