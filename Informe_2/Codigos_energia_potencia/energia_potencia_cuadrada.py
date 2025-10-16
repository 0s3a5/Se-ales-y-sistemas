import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square

fs = 1000
n_full = np.arange(-2000, 4000)
A = 3
f = 5

# Señal cuadrada
x_full = A * square(2 * np.pi * f * n_full / fs)

# Respuesta al impulso (Exponencial creciente)
n_h = np.arange(0, fs)
h = np.exp(n_h / fs)

# Convolución
y_full = np.convolve(x_full, h) / fs
# n_y_full = np.arange(n_full[0] + n_h[0], n_full[-1] + n_h[-1] + 1)

# Funciones de energía y potencia
def energia(signal):
    return np.sum(signal**2)

def potencia(signal):
    return np.mean(signal**2)

# Calcular energía y potencia
energia_x = energia(x_full)
potencia_x = potencia(x_full)
energia_y = energia(y_full)
potencia_y = potencia(y_full)

# Impresión de resultados
print(f"Energia de la señal de entrada x[n]: {energia_x:.4f}")
print(f"Potencia de la señal de entrada x[n]: {potencia_x:.4f}")
print(f"Energia de la señal de salida y[n]: {energia_y:.4f}")
print(f"Potencia de la señal de salida y[n]: {potencia_y:.4f}")
