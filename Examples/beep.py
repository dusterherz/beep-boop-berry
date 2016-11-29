import sys
sys.path.insert(0, '..')

from beep_boop_berry import BeepBoop

beep = BeepBoop(2)
beep.beep(0.5)
beep.beeps(0.1, 0.5, 2)
beep.note(BeepBoop.Note.A, 1)
beep.notes(BeepBoop.Note.C, 0.5, 0.5, 4)
