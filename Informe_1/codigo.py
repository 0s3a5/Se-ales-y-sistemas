import numpy as np
from scipy.io import wavfile
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

Fs, data = wavfile.read(r"C:\Users\nhaya_zfkr13k\OneDrive\Music\acoustic.wav")

if data.ndim > 1:
    data = data[:, 0]

data = data / np.max(np.abs(data))

N = len(data)
yf = np.abs(fft(data))
xf = fftfreq(N, 1 / Fs)

xf = xf[:N//2]
yf = yf[:N//2]

threshold = 0.01 * np.max(yf)
freq_max = xf[yf > threshold][-1]

Fs_ideal = 2 * freq_max

print(f"Frecuencia de muestreo del archivo: {Fs} Hz")
print(f"Frecuencia máxima significativa: {freq_max:.2f} Hz")
print(f"Frecuencia de muestreo ideal (Nyquist): {Fs_ideal:.2f} Hz")

plt.plot(xf, yf)
plt.title("Espectro de la señal")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()
