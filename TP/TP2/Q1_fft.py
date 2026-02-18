import numpy as np
import matplotlib.pyplot as plt

fs = 44100
t = np.linspace(0, 1, fs)

x = np.sin(2*np.pi*440*t) + np.sin(2*np.pi*880*t)

X = np.fft.fft(x)
f = np.fft.fftfreq(len(X), 1/fs)

plt.plot(f[:20000], np.abs(X)[:20000])
plt.title("FFT signal")
plt.show()
