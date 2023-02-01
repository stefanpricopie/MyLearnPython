import numpy as np

# Difference between np.random.random and numpy.random.uniform
# See https://stackoverflow.com/questions/13213496/what-does-depending-on-rounding-exactly-mean/13213524#13213524

np.random.random()          # has no arguments, returns a float in [0, 1)
np.random.uniform(5, 10)    # can have arguments, can return float in [5, 10) or in [5, 10] depending on rounding