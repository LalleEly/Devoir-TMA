import cv2

img = cv2.imread("image.png", 0)

if img is None:
    print("mettre image.png dans le dossier")
else:
    img4 = (img // 64) * 64
    img2 = (img // 128) * 128

    small = cv2.resize(img, (img.shape[1]//8, img.shape[0]//8))
    pixel = cv2.resize(small, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)

    cv2.imshow("image", img)
    cv2.imshow("4 niveaux", img4)
    cv2.imshow("2 niveaux", img2)
    cv2.imshow("pixelisation", pixel)
    cv2.waitKey(0)

