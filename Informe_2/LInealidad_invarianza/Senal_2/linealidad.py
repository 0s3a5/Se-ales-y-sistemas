import numpy as np
import matplotlib.pyplot as plt

# --- Definición de Parámetros y Señales de Entrada ---
N = 101 
n = np.arange(N) 
a1 = 3
a2 = 4

# x1[n]: Escalón unitario u[n]
x1 = np.where(n >= 0, 1.0, 0.0)
# x2[n]: Pulso atenuado (ejemplo para contraste)
pulso = np.where((n >= 20) & (n < 40), 1.0, 0.0)
tau = 10
exponencial = np.exp(-(n - 20) / tau)
x2 = pulso * exponencial

# Combinación lineal de la entrada
x = a1 * x1 + a2 * x2

# --- Definición y Cálculo del Sistema T2[x(n)] = 2x(n-2) + 5 ---
def T2(x_in):
    # Desplazamiento x(n-2)
    x_shifted = np.roll(x_in, 2)
    return 2 * x_shifted + 5

# Cálculo de Salidas Individuales y Combinadas
y1 = T2(x1)
y2 = T2(x2)
y = T2(x) # T[a1*x1 + a2*x2]
y_comb = a1 * y1 + a2 * y2 # a1*T[x1] + a2*T[x2]

# ... (El código continúa con la generación de las figuras de comparación)
