import numpy as np
import matplotlib.pyplot as plt

# --- Definición de Parámetros y Señales de Entrada ---
N = 21 
k = 4 # Desplazamiento temporal
t = np.arange(-5, N - 5, 1) # Rango de tiempo discreto
x = np.where(t >= 0, 1, 0) # Entrada: Escalón unitario u(n)

# --- Definición del Sistema T2[x(n)] = 2x(n-2) + 5 ---
def T2(x_in):
    x_shifted = np.roll(x_in, 2)
    return 2 * x_shifted + 5

# --- Cálculos para Invarianza ---
# 1. Salida para la entrada desplazada: y1 = T[x(n-k)]
x_shifted_input = np.roll(x, k)
x_shifted_input[:k] = 0
y1_shifted_output = T2(x_shifted_input)

# 2. Salida original desplazada: y2 = y(n-k)
original_output = T2(x)
y2_shifted_output = np.roll(original_output, k)
y2_shifted_output[:k] = 0

# ... (El código continúa con la generación de las figuras de comparación)
