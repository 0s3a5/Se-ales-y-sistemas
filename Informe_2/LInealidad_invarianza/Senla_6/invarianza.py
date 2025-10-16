import numpy as np
import matplotlib.pyplot as plt

# --- Parámetros y Señales de Entrada ---
N = 21 
k = 4 # Desplazamiento temporal
n = np.arange(0, N, 1)

# Entrada: Escalón unitario discreto u[n]
def u(x):
    return np.where(x >= 0, 1, 0)
x = u(n)

# --- Sistema T6[x(n)] (Definición Simplificada) ---
def sistema_T6(x_in):
    y = np.zeros_like(x_in, dtype=float)
    M = len(x_in)
    
    for i in range(M):
        xn = x_in[i] if i >= 0 and i < M else 0
        xn_m1 = x_in[i-1] if i - 1 >= 0 and i - 1 < M else 0
        xn_m2 = x_in[i-2] if i - 2 >= 0 and i - 2 < M else 0
        
        y[i] = (1/2) * xn + (1/2) * xn_m1 + (1/4) * xn_m2
        
    return y

# --- Cálculos para invarianza ---
original_output = sistema_T6(x)

# Entrada desplazada x(n-k)
x_shifted_input = np.roll(x, k)
x_shifted_input[:k] = 0 

# Salida para la entrada desplazada T[x(n-k)]
y_shifted_input = sistema_T6(x_shifted_input)

# Salida original desplazada y(n-k)
y_shifted_output = np.roll(original_output, k)
y_shifted_output[:k] = 0 

# ... (El código continúa con la generación de las figuras de comparación)
