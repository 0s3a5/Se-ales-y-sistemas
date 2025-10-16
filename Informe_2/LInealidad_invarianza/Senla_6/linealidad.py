import numpy as np
import matplotlib.pyplot as plt

# --- Parámetros y Señales de Entrada ---
N = 21 
n = np.arange(-5, 16, 1) 
a1 = 3
a2 = 4

# u(x)
def u(x):
    return np.where(x >= 0, 1, 0)

# x1[n]: Escalón u(n)
x1 = u(n)
# x2[n]: Pulso u(n)-u(n-3)
x2 = u(n) - u(n - 3)

# --- Sistema T6[x(n)] = 0.5*x(n) + 0.5*x(n-1) + 0.25*x(n-2) ---
def sistema_T6(x_in):
    y = np.zeros_like(x_in, dtype=float)
    M = len(x_in) 
    
    for i in range(M):
        # Aseguramos el acceso a x[n], x[n-1], x[n-2] dentro de los límites
        xn = x_in[i] if i >= 0 and i < M else 0
        xn_m1 = x_in[i-1] if i - 1 >= 0 and i - 1 < M else 0
        xn_m2 = x_in[i-2] if i - 2 >= 0 and i - 2 < M else 0
        
        y[i] = (1/2) * xn + (1/2) * xn_m1 + (1/4) * xn_m2
        
    return y
    
# --- Cálculos ---
x = a1 * x1 + a2 * x2
y1 = sistema_T6(x1)
y2 = sistema_T6(x2)
y = sistema_T6(x)
y_comb = a1 * y1 + a2 * y2

# ... (El código continúa con la generación de las figuras de comparación)
