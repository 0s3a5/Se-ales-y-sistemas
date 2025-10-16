import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

# Parámetros
fs = 1000
dt = 1 / fs
n = np.arange(-1000, 1000, 20) # Rango de -1000 a 980, paso 20
t_input = n * dt
f = 5

# Señal de entrada (Triangular simétrica)
x = sawtooth(2 * np.pi * f * t_input, 0.5)

# Impulso discreto centrado en t=0 (n=0)
h = np.where(n == 0, 1, 0)

# Convolución discreta
y = np.convolve(x, h)
# Rango de salida
n_output = np.arange(len(y)) + n[0] # n[0] es -1000

# Gráficas
fig, axs = plt.subplots(3, 1, figsize=(14, 8), sharex=False)

axs[0].stem(n, x, linefmt='-', markerfmt='o', basefmt="")
axs[0].set_title('Señal Triangular de Entrada (Discreta)')
axs[0].grid(True)

axs[1].stem(n, h, linefmt='-', markerfmt='o', basefmt="")
axs[1].set_title('Respuesta al Impulso Discreto (Delta en n=0)')
axs[1].grid(True)

axs[2].stem(n_output, y, linefmt='-', markerfmt='o', basefmt="")
axs[2].set_title('Salida del Sistema (Convolución Discreta)')
axs[2].set_xlabel('n')
axs[2].grid(True)

plt.tight_layout()
plt.show()
