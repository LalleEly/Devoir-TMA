import numpy as np
import matplotlib.pyplot as plt

fs = 100
t = np.linspace(0, 1, fs)
x = np.sin(2*np.pi*10*t)

plt.plot(t, x)
plt.title("Signal sinus 10Hz")
plt.show()
