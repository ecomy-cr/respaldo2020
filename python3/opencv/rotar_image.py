import cv2

img = cv2.imread('assets/logo.jpg', 1)
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg', img)#guarda la imagen editada move 90 grados

cv2.imshow('Image', img) # muestra imagen en escritorio PC
cv2.waitKey(0) #se detiene al presionar tecla
cv2.destroyAllWindows() #se destruye 'chs