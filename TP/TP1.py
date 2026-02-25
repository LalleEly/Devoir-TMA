# TP1 : Génération d’un signal sinusoïdal, ajout de bruit blanc gaussien,
#création d’un signal porte et calcul de sa convolution (résultat triangulaire).

import numpy as np
import matplotlib.pyplot as plt

# 1.1 Signal sinusoïdal
f0, A, phi, fs, T = 10, 1, 0, 100, 1
t = np.arange(0, T, 1/fs)
x = A * np.sin(2 * np.pi * f0 * t + phi)

plt.figure()
plt.plot(t, x)
plt.title("Signal sinusoïdal pur")
plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# 1.2 Ajout de bruit
bruit = np.random.normal(0, 0.2, len(t))
y = x + bruit

plt.figure()
plt.plot(t, x, label="Signal pur")
plt.plot(t, y, label="Signal bruité", alpha=0.7)
plt.title("Comparaison signal pur / bruité")
plt.legend()
plt.grid(True)
plt.show()

# 1.3 Porte et convolution
porte = np.zeros(100)
porte[20:41] = 1
conv = np.convolve(porte, porte, mode='full')

plt.figure()
plt.subplot(2,1,1)
plt.stem(porte)   
plt.title("Signal porte")
plt.subplot(2,1,2)
plt.plot(conv)
plt.title("Auto-convolution (triangle)")
plt.tight_layout()
plt.show()