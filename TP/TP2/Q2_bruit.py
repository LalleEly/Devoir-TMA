import numpy as np
import matplotlib.pyplot as plt

fs = 44100
t = np.linspace(0, 1, fs)

x = np.sin(2*np.pi*440*t) + np.sin(2*np.pi*880*t)
bruit = 0.2*np.sin(2*np.pi*5000*t)

s = x + bruit

S = np.fft.fft(s)
f = np.fft.fftfreq(len(S), 1/fs)

plt.plot(f[:20000], np.abs(S)[:20000])
plt.title("FFT avec bruit")
plt.show()
