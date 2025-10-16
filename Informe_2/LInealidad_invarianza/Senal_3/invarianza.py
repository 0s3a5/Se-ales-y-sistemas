import numpy as np
import matplotlib.pyplot as plt

# --- Parámetros ---
N = 21
k = 4 # Desplazamiento
t = np.arange(-5, 16, 1)
n = np.arange(N)

# --- Señal de entrada ---
x = np.where(t >= 0, 1, 0) # Escalón unitario u(n)

# --- Definición del Sistema T3[x(n)] = x(n+1) - x(n-1) ---
def sistema_T3(x_in):
    x_forward = np.roll(x_in, -1)
    x_backward = np.roll(x_in, 1)
    return x_forward - x_backward

# --- Cálculos para Invarianza ---
# 1. Salida para la entrada desplazada: y1 = T[x(n-k)]
x_shifted_input = np.roll(x, k)
x_shifted_input[:k] = 0 
y_shifted_input = sistema_T3(x_shifted_input)

# 2. Salida original desplazada: y2 = y(n-k)
original_output = sistema_T3(x)
y_shift_output = np.roll(original_output, k)
y_shift_output[:k] = 0

# ... (El código continúa con la generación de las figuras de comparación)
