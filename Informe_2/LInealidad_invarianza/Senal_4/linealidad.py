import numpy as np
import matplotlib.pyplot as plt

# --- Parámetros ---
N = 100
n = np.arange(0, N, 1)
a1 = 3
a2 = 4

# --- Señales de entrada ---
x1 = np.zeros(N, dtype=float)
x1[5] = 1 # delta[n-5]
x2 = np.where(n >= 0, 1, 0) # Escalón unitario u[n]

# Combinación lineal de entrada
x = a1 * x1 + a2 * x2

# --- Sistema T4[x(n)] = 10*sin(0.1*pi*n)*x(n) ---
def sistema_T4(x_in, n_in):
    sinusoidal = 10 * np.sin(0.1 * np.pi * n_in)
    return sinusoidal * x_in

# --- Cálculos ---
y1 = sistema_T4(x1, n)
y2 = sistema_T4(x2, n)
y = sistema_T4(x, n) # T[a1*x1 + a2*x2]
y_comb = a1 * y1 + a2 * y2 # a1*T[x1] + a2*T[x2]

# ... (El código continúa con el muestreo y la generación de las figuras)
