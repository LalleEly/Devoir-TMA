# TP2 : Analyse spectrale d’un signal composé de deux fréquences (440 Hz et 880 Hz),
#       ajout d’une perturbation à 5000 Hz, puis filtrage coupe-bande dans le domaine
#       fréquentiel et reconstruction du signal par IFFT.


import numpy as np
import matplotlib.pyplot as plt
import numpy.fft as fft

# 2.1 Signal avec deux fréquences
fs, T = 44100, 2
t = np.linspace(0, T, int(fs*T), endpoint=False)
x = np.sin(2*np.pi*440*t) + 0.5*np.sin(2*np.pi*880*t)

# Spectre
spectre = fft.fft(x)
freq = fft.fftfreq(len(x), 1/fs)
plt.figure()
plt.plot(freq[freq>=0], np.abs(spectre[freq>=0]))
plt.title("Spectre original (440 Hz et 880 Hz)")
plt.xlabel("Fréquence (Hz)")
plt.xlim(0, 2000)
plt.grid(True)
plt.show()

# 2.2 Ajout d'un bruit à 5000 Hz et filtrage
x_bruite = x + 0.2 * np.sin(2*np.pi*5000*t)
spectre_b = fft.fft(x_bruite)

# Filtre coupe-bande
filtre = np.ones(len(spectre_b), dtype=complex)
indice = int(5000 / fs * len(x_bruite))
largeur = 100
filtre[indice-largeur:indice+largeur] = 0
filtre[-indice-largeur:-indice+largeur] = 0  # symétrie
spectre_filtre = spectre_b * filtre
x_filtre = fft.ifft(spectre_filtre).real

# Affichage temporel (zoom)
plt.figure()
plt.plot(t[:1000], x[:1000], label="Original")
plt.plot(t[:1000], x_filtre[:1000], label="Filtré")
plt.title("Signal temporel avant/après filtrage")
plt.legend()
plt.grid(True)
plt.show()