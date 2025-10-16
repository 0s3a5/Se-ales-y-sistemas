import numpy as np
import matplotlib.pyplot as plt

# Parámetros y rangos
n_input = np.arange(-40, 41)
n_impulse = np.arange(0, 10) # Asumiendo 10 muestras (de 0 a 9)
f = 0.05

# Señal de entrada (Senoidal)
x = np.sin(2 * np.pi * f * n_input)

# Respuesta al impulso (Exponencial decreciente en un tramo)
h = np.exp(-n_impulse)
# NOTA: El código de la imagen parece tener un error aquí, usa np.ones(1) en el ejemplo, 
# pero la descripción habla de una exponencial. Usamos la exponencial h.

# Convolución discreta
y = np.convolve(x, h)

# Rango de salida para la convolución
# n_output comienza en n_input[0] + n_impulse[0] y termina en n_input[-1] + n_impulse[-1]
n_output = np.arange(n_input[0] + n_impulse[0], n_input[-1] + n_impulse[-1] + 1)

plt.figure(figsize=(12, 8))

# Gráfico de la señal de entrada
plt.subplot(3, 1, 1)
plt.title('Entrada: Señal Senoidal Discreta')
plt.stem(n_input, x)
plt.ylabel('$x[n]$')
plt.xticks(np.arange(min(n_input), max(n_input) + 1, 10))
plt.grid(True)

# Gráfico de la respuesta al impulso
plt.subplot(3, 1, 2)
plt.title('Respuesta al Impulso: Exponencial Decreciente (tramo)')
plt.stem(n_impulse, h)
plt.ylabel('$h[n]$')
plt.xticks(np.arange(min(n_impulse), max(n_impulse) + 1, 1))
plt.grid(True)

# Gráfico de la salida por convolución
plt.subplot(3, 1, 3)
plt.title('Salida: Convolución $y[n] = x[n] * h[n]$')
plt.stem(n_output, y)
plt.xlabel('$n$')
plt.ylabel('$y[n]$')
plt.xticks(np.arange(min(n_output), max(n_output) + 1, 10))
plt.grid(True)

plt.tight_layout()
plt.show()
