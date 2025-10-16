import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square # Asumiendo que square viene de scipy.signal

# Parámetros
fs = 1000
N_full = np.arange(-2000, 4000)
A = 3
f = 5

# Señal cuadrada x_full[n]
x_full = A * square(2 * np.pi * f * N_full / fs)

# Respuesta al impulso (Exponencial creciente)
n_h = np.arange(0, fs) # Rango de 0 a fs-1
h = np.exp(n_h / fs)

# Convolución discreta
y_full = np.convolve(x_full, h) / fs # Normalización por fs (aproximación a conv. continua)
n_y_full = np.arange(n_full[0] + n_h[0], n_full[-1] + n_h[-1] + 1)

# El código original incluye lógica compleja de plotting y subplots que omito por brevedad,
# pero las variables clave de la convolución son x_full, h, y_full y n_y_full.
