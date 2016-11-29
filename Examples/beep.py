import sys
sys.path.insert(0, '..')

from beep_boop_berry import BeepBoop

beep = BeepBoop(2)
boop = BeepBoop(5)
beep.beep(1)
boop.beep(5)
