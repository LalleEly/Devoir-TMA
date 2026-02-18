import numpy as np
import matplotlib.pyplot as plt

fs = 100
t = np.linspace(0, 1, fs)
x = np.sin(2*np.pi*10*t)

bruit = np.random.randn(len(t))
y = x + bruit

plt.plot(t, y)
plt.title("Signal avec bruit")
plt.show()
