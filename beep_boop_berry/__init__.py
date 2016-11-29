"""Beep Boop Berry

This module can make your Raspberry sing if you have a Piezzo-Beeper connected
to it.

Todo:
    * EVERYTHING
    * Make some examples
    * A tutorial to connect a buzzer and make it sing the Imperial March
"""

from enum import IntEnum
from time import sleep
import RPi.GPIO as GPIO


class BeepBoop():
    """
    The main class of the module. Without that, you can't make a sound. It needs
    the pin where the buzzer is connected to be initialize.

    Attributes :
        pin (int): the pin where the buzzer is connected
    """
    class Note(IntEnum):
        A = 440
        B = 494
        C = 262
        D = 294
        E = 330
        F = 349
        G = 392

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def beep(self, time):
        """
            Make your beeper sing a small *Beep*.
            time is the duration of the beep in seconds
        """
        self.note(BeepBoop.Note.A, time)

    def beeps(self, timeOn, timeOff, repeat):
        """
            Make your beeper sing multiples *Beep*.
            time is the duration of the beep in seconds
            repeat correspond to the numer of time the beeper must beep.

        """

        self.notes(BeepBoop.Note.A, timeOn, timeOff, repeat)

    def note(self, note, time):
        """
            Make your beeper sing a single note.*
            note is a note from the enum Note
            time is the duration he the beep in seconds
        """

        delay = 1 / note / 2
        cycles = int(time * note)

        for i in range(cycles):
            GPIO.output(self.pin, True)
            sleep(delay)
            GPIO.output(self.pin, False)
            sleep(delay)

    def notes(self, note, timeOn, timeOff, repeat):

        for i in range(repeat):
            self.note(note, timeOn)
            sleep(timeOff)
