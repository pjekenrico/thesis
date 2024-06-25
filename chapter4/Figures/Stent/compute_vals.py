import numpy as np


# Define the parameters
def compute_lw(w, L, d, Nw):
    return L / (np.sqrt(1 - (np.pi * d / (w * Nw)) ** 2))


def compute_l(w, lw, d, Nw):
    return lw * (np.sqrt(1 - (np.pi * d / (w * Nw)) ** 2))


# PED 3.25
d_nom = 3.25
w = 0.2315
Nw = 48
lw = compute_lw(w, 20, d_nom, Nw)
L1 = compute_l(w, lw, 3, Nw)
print("PED 3.25: lw = ", lw, "L1 = ", L1)

# PED 3.75
d_nom = 3.75
w = 0.2636
lw = compute_lw(w, 16, d_nom, Nw)
L1 = compute_l(w, lw, 3.5, Nw)
print("PED 3.75: lw = ", lw, "L1 = ", L1)

# PED 4.75
d_nom = 4.75
w = 0.3283
lw = compute_lw(w, 30, d_nom, Nw)
L1 = compute_l(w, lw, 4.5, Nw)
print("PED 4.75: lw = ", lw, "L1 = ", L1)
