import numpy as np
import matplotlib.pyplot as plt

# --- Parámetros ---
N = 40
n = np.arange(0, N, 1)
a1 = 3
a2 = 4

# --- Señales de entrada ---
x1 = np.zeros_like(n, dtype=float)
x1[0] = 1 # delta[n]
x2 = x1 # x2 también es delta[n], así x = (a1+a2)delta[n]

# --- Definición del Sistema T5[x(n)] = x(n+1) - x(1-n) ---
def sistema_T5(x_in):
    # x(n+1)
    x_shift_1 = np.roll(x_in, -1)
    # x(1-n) = x(- (n-1)) (Reflejo y desplazamiento)
    x_flip = np.flip(x_in)
    x_shift_2 = np.roll(x_flip, -1)
    return x_shift_1 - x_shift_2

# --- Salidas del sistema ---
x = a1 * x1 + a2 * x2 
y1 = sistema_T5(x1)
y2 = sistema_T5(x2)
y = sistema_T5(x)
y_comb = a1 * y1 + a2 * y2

# ... (El código continúa con el muestreo y la generación de las figuras)
