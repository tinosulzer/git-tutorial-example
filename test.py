import numpy as np

x = np.array([2., 3., 5.])

def potential(r):
    R = np.linalg.norm(r)

    return 1 / R

print("potential(x) == ", potential(x))
