from configure.Configure import rows, cols
from .Hole import Hole

# creates a list of holes

holes = []

for x in range(rows*cols):
    holes.append(Hole())
