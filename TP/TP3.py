# TP3 – Partie Audio : Mise en évidence de l’aliasing par sous-échantillonnage d’un signal
#       contenant des fréquences élevées (jusqu’à 20 kHz) et affichage des spectrogrammes.
#       Partie Image : Réduction du nombre de niveaux de gris (quantification à 4 et 2 niveaux)
#       et pixelisation par sous-échantillonnage spatial (facteur 8).


import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# ---- Partie Audio : Aliasing ----
fs_orig = 44100
t = np.linspace(0, 1, fs_orig, endpoint=False)

x_audio = sum(amp * np.sin(2*np.pi*f*t) for f, amp in 
              zip([1000,5000,10000,15000,20000], [1,0.5,0.3,0.2,0.1]))


x_sub = x_audio[::10]
fs_sub = fs_orig // 10


f, t_spec, Sxx_orig = signal.spectrogram(x_audio, fs_orig)
f2, t_spec2, Sxx_sub = signal.spectrogram(x_sub, fs_sub)

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.pcolormesh(t_spec, f, 10*np.log10(Sxx_orig+1e-10), shading='gouraud')
plt.title("Spectrogramme original (44.1 kHz)")
plt.ylabel("Fréq. (Hz)")
plt.ylim(0,22000)
plt.colorbar(label="dB")

plt.subplot(1,2,2)
plt.pcolormesh(t_spec2, f2, 10*np.log10(Sxx_sub+1e-10), shading='gouraud')
plt.title("Spectrogramme sous-échantillonné (4.41 kHz)")
plt.xlabel("Temps (s)")
plt.ylim(0, fs_sub/2)
plt.colorbar(label="dB")
plt.tight_layout()
plt.show()

# ---- Partie Image : Quantification et Pixelisation ----
# Création d'une image de test (dégradé + disque)
taille = 256
x = np.linspace(0,1,taille)
X, Y = np.meshgrid(x, x)
img = (X + ((X-0.5)**2 + (Y-0.5)**2 < 0.2)*0.8) * 255
img = img.astype(np.uint8)


def quantifier(I, niveaux):
    pas = 256 // niveaux
    return (I // pas) * pas

img_4 = quantifier(img, 4)
img_2 = quantifier(img, 2)


img_small = img[::8, ::8]
img_pix = np.repeat(np.repeat(img_small, 8, axis=0), 8, axis=1)


plt.figure(figsize=(12,8))
plt.subplot(2,3,1); plt.imshow(img, cmap='gray'); plt.title("Originale")
plt.subplot(2,3,2); plt.imshow(img_4, cmap='gray'); plt.title("4 niveaux")
plt.subplot(2,3,3); plt.imshow(img_2, cmap='gray'); plt.title("2 niveaux")
plt.subplot(2,3,4); plt.imshow(img[150:250,150:250], cmap='gray'); plt.title("Zoom original")
plt.subplot(2,3,5); plt.imshow(img_4[150:250,150:250], cmap='gray'); plt.title("Zoom 4 niv. (banding)")
plt.subplot(2,3,6); plt.imshow(img_pix, cmap='gray'); plt.title("Pixelisation x8")
for i in range(1,7): plt.subplot(2,3,i).axis('off')
plt.tight_layout()
plt.show()