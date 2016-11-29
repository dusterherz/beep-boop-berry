import sys
sys.path.insert(0, '..')

from beep_boop_berry import BeepBoop

beep = BeepBoop(2)

# make a simple beep
beep.beep(0.5)

# make multiple beep
beep.beeps(0.1, 0.5, 2)

# make a specific note
beep.note(BeepBoop.Note.A, 1)

# make multiple specific notes
beep.notes(BeepBoop.Note.C, 0.5, 0.5, 4)

# Come to the dark side of the Force. We have cookies !
beep.song([{"note": BeepBoop.Note.G, "time": 1}, {"note": BeepBoop.Note.G, "time": 1}, {"note": BeepBoop.Note.G, "time": 1},
 {"note": BeepBoop.Note.Dd, "time": 0.5}, {"note": BeepBoop.Note.Ad, "time": 0.5}, {"note": BeepBoop.Note.G, "time": 1},
 {"note": BeepBoop.Note.Dd, "time": 0.5}, {"note": BeepBoop.Note.Ad, "time": 0.5}, {"note": BeepBoop.Note.G, "time": 1.5}])
