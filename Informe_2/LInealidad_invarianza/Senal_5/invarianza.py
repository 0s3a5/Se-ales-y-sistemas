import numpy as np
import matplotlib.pyplot as plt

# --- Parámetros ---
N = 20
k = 4 # Desplazamiento temporal
n = np.arange(0, N, 1)

# --- Señal de entrada ---
x = np.zeros_like(n, dtype=float)
x[0] = 1 # delta[n]

# --- Definición del Sistema T5[x(n)] = x(n+1) - x(1-n) ---
def sistema_T5(x_in):
    x_shift_1 = np.roll(x_in, -1)
    x_flip = np.flip(x_in)
    x_shift_2 = np.roll(x_flip, -1)
    return x_shift_1 - x_shift_2

# --- Cálculos para invarianza ---
original_output = sistema_T5(x)

# Entrada desplazada x(n-k)
x_shifted_input = np.roll(x, k)
x_shifted_input[:k] = 0 

# Salida para la entrada desplazada T[x(n-k)]
y_shifted_input = sistema_T5(x_shifted_input)

# Salida original desplazada y(n-k)
y_shifted_output = np.roll(original_output, k)
y_shifted_output[:k] = 0 

# ... (El código continúa con la generación de las figuras de comparación)
