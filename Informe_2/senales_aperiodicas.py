import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-20, 41) # Muestras (rango de -20 a 40)

def u(n):
    return np.where(n >= 0, 1, 0)

def delta(n):
    return np.where(n == 0, 1, 0)

# Señales
exp_decreciente = np.exp(-n) * (u(n) - u(n - 10))
exp_creciente = np.exp(n) * (u(n) - u(n - 10))
impulso = delta(n)
escalon = u(n)

# Graficación
plt.figure(figsize=(10, 8))

# Exponencial decreciente
plt.subplot(4, 1, 1)
m, c, b = plt.stem(n, exp_decreciente, basefmt="-")
plt.setp(c, markersize=6)
plt.setp(b, linewidth=2)
plt.title(r'$x[n] = e^{-n}[u[n] - u[n-10]]$')
plt.ylabel("Amplitud")
plt.grid(True)

# Exponencial creciente
plt.subplot(4, 1, 2)
m, c, b = plt.stem(n, exp_creciente, basefmt="-")
plt.setp(c, markersize=6)
plt.setp(b, linewidth=2)
plt.title(r'$x[n] = e^{n}[u[n] - u[n-10]]$')
plt.ylabel("Amplitud")
plt.grid(True)

# Impulso
plt.subplot(4, 1, 3)
m, c, b = plt.stem(n, impulso, basefmt="-")
plt.setp(m, markersize=0) # Los marcadores de impulso se ven como la línea central
plt.setp(c, linewidth=2)
plt.title(r'$x[n] = \delta[n]$')
plt.ylabel("Amplitud")
plt.grid(True)

# Escalón
plt.subplot(4, 1, 4)
m, c, b = plt.stem(n, escalon, basefmt="-")
plt.setp(c, markersize=6)
plt.setp(b, linewidth=2)
plt.title(r'$x[n] = u[n]$')
plt.ylabel("Amplitud")
plt.grid(True)

plt.tight_layout()
plt.show()
