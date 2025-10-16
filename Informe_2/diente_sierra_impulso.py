import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

# Parámetros
fs = 1000
dt = 1 / fs
n = np.arange(-1000, 3000, 20)
t_input = n * dt
f = 5

# Señal diente de sierra discreta (entrada)
x = sawtooth(2 * np.pi * f * t_input, 0.5) # Diente de sierra simétrica

# Señal escalón unitario discreto u[n]
def escalon(n_in):
    return np.where(n_in >= 0, 1, 0)

h = escalon(n) # La respuesta al impulso es el escalón

# Convolución discreta
y = np.convolve(x, h) * dt # Multiplicación por dt (aproximación a conv. continua)
n_output = np.arange(len(y)) + n[0]

# Graficar con stem para discreto
fig, axs = plt.subplots(3, 1, figsize=(14, 8), sharex=False)

axs[0].stem(n, x, linefmt='-', markerfmt='o', basefmt="")
axs[0].set_title('Señal de Entrada: Diente de Sierra (Discreta)')
axs[0].grid(True)

axs[1].stem(n, h, linefmt='-', markerfmt='o', basefmt="")
axs[1].set_title('Respuesta al Impulso: Escalón Unitario Discreto u[n]')
axs[1].grid(True)

axs[2].stem(n_output, y, linefmt='-', markerfmt='o', basefmt="")
axs[2].set_title('Salida del Sistema (Convolución Discreta)')
axs[2].set_xlabel('n')
axs[2].grid(True)

plt.tight_layout()
plt.show()
