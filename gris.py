import cv2
img = cv2.imread('D:/respaldo/0badfa1b11174d2ebc7a1a6a978e7feffa41b314161a7a94a1cd25f72e3d07b4.jpg')
#Convertir a escalas de grises BGR primero el azul, el verdes luego el rojo
gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('original',gris)
#cv2.imwrite('Salida/gris.jpg',gris)
cv2.waitKey(0) #mantenga la imagen
cv2.destroyAllWindows() #destruya la imagen