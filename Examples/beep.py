import sys
sys.path.insert(0, '..')

from beep_boop_berry import BeepBoop

beep = BeepBoop(2)
beep.beep(1)
beep.beeps(1, 1, 5)
