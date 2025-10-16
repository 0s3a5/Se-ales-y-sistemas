import numpy as np
import matplotlib.pyplot as plt
from scipy import signal # Importar signal si no está implícito en la imagen

# Parámetros de muestreo
fs = 100 # frecuencia de muestreo (muestras por segundo)
T = 1 # duración en segundos
t = np.linspace(0, T, fs, endpoint=False)

# Frecuencia de las Señales
f = 5 # frecuencia en Hz

# Generación de señales periódicas
senoidal = np.sin(2 * np.pi * f * t)
cuadrada = signal.square(2 * np.pi * f * t)
# triangular usa width=0.5 para simetría
triangular = signal.sawtooth(2 * np.pi * f * t, 0.5) 
diente_de_sierra = signal.sawtooth(2 * np.pi * f * t) 

# Graficar señales
plt.figure(figsize=(10, 6))

plt.subplot(4, 1, 1)
plt.plot(t, senoidal)
plt.title('Señal Senoidal (discreta)')
plt.grid()

plt.subplot(4, 1, 2)
plt.plot(t, cuadrada)
plt.title('Señal Cuadrada (discreta)')
plt.grid()

plt.subplot(4, 1, 3)
plt.plot(t, triangular)
plt.title('Señal Triangular (discreta)')
plt.grid()

plt.subplot(4, 1, 4)
plt.plot(t, diente_de_sierra)
plt.title('Señal Diente de Sierra (discreta)')
plt.grid()

plt.tight_layout()
plt.show()
