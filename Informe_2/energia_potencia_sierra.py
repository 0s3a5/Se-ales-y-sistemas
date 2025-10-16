import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

# Parámetros
fs = 1000
dt = 1 / fs
n = np.arange(-1000, 3000, 20)
t_input = n * dt
f = 5

# Señal diente de sierra discreta (entrada)
x = sawtooth(2 * np.pi * f * t_input, 0.5)

# Escalón unitario discreto u[n]
def escalon(n_in):
    return np.where(n_in >= 0, 1, 0)

h = escalon(n)

# Convolución discreta
y = np.convolve(x, h) * dt # Multiplicación por dt (aproximación a conv. continua)
# n_output = np.arange(len(y)) + n[0]

# Funciones de energía y potencia
def energia(signal):
    return np.sum(signal**2)

def potencia(signal):
    return np.mean(signal**2)

# Calcular energía y potencia
energia_x = energia(x)
potencia_x = potencia(x)
energia_y = energia(y)
potencia_y = potencia(y)

# Impresión de resultados
print(f"Energia de la señal de entrada x[n]: {energia_x:.4f}")
print(f"Potencia de la señal de entrada x[n]: {potencia_x:.4f}")
print(f"Energia de la señal de salida y[n]: {energia_y:.4f}")
print(f"Potencia de la señal de salida y[n]: {potencia_y:.4f}")
