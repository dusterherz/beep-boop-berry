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
        A = 440.0
        Ad = 466.16
        B = 493.88
        C = 261.63
        D = 293.66
        Dd = 311.13
        E = 329.63
        F = 349.23
        Fd = 369.99
        G = 392.0
        Gd = 415.30
        blank = 0

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
            timeOn is the duration of the beep in seconds
            timeOff is the duration of the silence in secons
            repeat correspond to the number of time the beeper must beep.

        """

        self.notes(BeepBoop.Note.A, timeOn, timeOff, repeat)

    def note(self, note, time):
        """
            Make your beeper sing a single note.
            note is a note from the enum Note
            time is the duration he the beep in seconds
        """

        if note == BeepBoop.Note.blank:
            sleep(time)

        delay = 1.0 / note / 2.0
        cycles = int(time * note)

        for i in range(cycles):
            GPIO.output(self.pin, True)
            sleep(delay)
            GPIO.output(self.pin, False)
            sleep(delay)

    def notes(self, note, timeOn, timeOff, repeat):
        """
            Make your beeper sing multiples notes.
            time is the duration of the beep in seconds
            timeOff is the duration of the silence in secons
            repeat correspond to the number of time the beeper must beep.
        """

        for i in range(repeat):
            self.note(note, timeOn)
            sleep(timeOff)

    def song(self, notes):
        """
            Make a song !
            notes is a list of dict like {"note":BeepBoop.Note.A, "time":1}
            See beep.py in folder Examples if you want a example !
        """

        for note in notes:
            self.note(note['note'], note['time'])
