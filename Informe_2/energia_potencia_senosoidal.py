import numpy as np
import matplotlib.pyplot as plt

n_input = np.arange(-40, 41)
n_impulse = np.arange(0, 10)
f = 0.05

# Señales
x = np.sin(2 * np.pi * f * n_input)
h = np.exp(-n_impulse)
y = np.convolve(x, h)

# Rango de salida (necesario solo si se graficara)
# n_output = np.arange(n_input[0] + n_impulse[0], n_input[-1] + n_impulse[-1] + 1)

# Cálculo de energía
energia_x = np.sum(np.abs(x)**2)
energia_y = np.sum(np.abs(y)**2)

# Cálculo de potencia media
potencia_x = energia_x / len(x)
potencia_y = energia_y / len(y)

# Impresión de resultados
print(f"Energia de la señal de entrada x[n]: {energia_x:.4f}")
print(f"Energia de la señal de salida y[n]: {energia_y:.4f}")
print(f"Potencia media de x[n]: {potencia_x:.4f}")
print(f"Potencia media de y[n]: {potencia_y:.4f}")
