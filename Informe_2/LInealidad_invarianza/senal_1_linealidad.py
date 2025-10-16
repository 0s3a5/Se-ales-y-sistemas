import numpy as np
import matplotlib.pyplot as plt

# --- Definición de Parámetros y Señales de Entrada ---
N = 100
t = np.linspace(0, 5, N, endpoint=False)
n = np.arange(len(t)) # n es el índice discreto
a1 = 3
a2 = 4

# x1[n]: Escalón unitario discreto (aproximado)
x1 = np.where(t >= 0, 1.0, 0.0)
# x2[n]: Pulso atenuado (exponencial decreciente en un tramo)
x2 = np.exp(-t) * (np.where(t >= 0, 1.0, 0.0) - np.where(t >= 1, 1.0, 0.0))

# Combinación lineal de la entrada
x = a1 * x1 + a2 * x2

# --- Cálculo de Salidas (Sistema T1[x] = 3x^2) ---
y1 = 3 * (x1**2) # T[x1]
y2 = 3 * (x2**2) # T[x2]
y = 3 * (x**2)   # T[a1*x1 + a2*x2]
y_comb = a1 * y1 + a2 * y2 # a1*T[x1] + a2*T[x2]

# --- Muestreo Discreto para la Gráfica ---
k = 8
n_m = n[::k]
y_m = y[::k]
y_comb_m = y_comb[::k]
# ... (El código continúa con la generación de las tres figuras de comparación)
