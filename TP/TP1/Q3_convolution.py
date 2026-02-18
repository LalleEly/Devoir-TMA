import numpy as np
import matplotlib.pyplot as plt

porte = np.zeros(100)
porte[20:40] = 1

conv = np.convolve(porte, porte)

plt.plot(conv)
plt.title("Convolution porte")
plt.show()
