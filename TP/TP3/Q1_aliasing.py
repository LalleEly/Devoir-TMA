import numpy as np
import matplotlib.pyplot as plt

fs = 44100
t = np.linspace(0, 1, fs)

x = np.sin(2*np.pi*15000*t)
x2 = x[::10]

plt.plot(x2[:2000])
plt.title("Aliasing")
plt.show()

