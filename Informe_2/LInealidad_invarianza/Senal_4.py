import numpy as np
import matplotlib.pyplot as plt

# --- Parámetros ---
N = 51
k = 4 # Desplazamiento temporal
n = np.arange(0, N, 1)

# --- Señal de entrada ---
x = np.zeros_like(n, dtype=float)
x[0] = 1 # delta[n]

# --- Definición del Sistema T4[x(n)] = 10*sin(0.1*pi*n)*x(n) ---
def sistema_T4(x_in, n_in):
    sinusoidal = 10 * np.sin(0.1 * np.pi * n_in)
    return sinusoidal * x_in

# --- Cálculos para Invarianza ---
# Salida original y(n) = T[x(n)]
original_output = sistema_T4(x, n)

# Entrada desplazada x(n-k)
x_shifted_input = np.roll(x, k)
x_shifted_input[:k] = 0 

# Salida para la entrada desplazada T[x(n-k)]
y_shifted_input = sistema_T4(x_shifted_input, n)

# Salida original desplazada y(n-k)
y_shifted_output = np.roll(original_output, k)
y_shifted_output[:k] = 0 

# ... (El código continúa con la generación de las figuras de comparación)
