# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import cv2
import numpy as np

manzana = cv2.imread('carro.jpg')

print (manzana[0,0,:])

b = manzana[:,:,0]
g = manzana[:,:,1]
r = manzana[:,:,2]

cv2.imwrite('original.jpg', manzana)

#cv2.imshow('', manzana)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite('canal_azul.jpg', b)

#cv2.imshow('', b)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite('canal_rojo.jpg', r)

#cv2.imshow('', r)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

img_gris = cv2.cvtColor(manzana, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gris.jpg', img_gris)

binaria = np.uint8(255*(img_gris>155))

binaria = np.uint8(255*(img_gris<200))

cv2.imwrite('binaria.jpg', binaria)

# cv2.imshow('', binaria)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#segmentar por escala de grises

gris_segmentada = img_gris*(binaria/255)
gris_segmentada = np.uint8(img_gris*(binaria/255))

cv2.imwrite('gris_segmentada.jpg', gris_segmentada)

#segmentar por color
seg_color = manzana.copy()

seg_color[:,:,0] = np.uint8(b*(binaria/255)) 
seg_color[:,:,1] = np.uint8(g*(binaria/255)) 
seg_color[:,:,2] = np.uint8(r*(binaria/255)) 

cv2.imwrite('segmentacion_color.jpg', seg_color)

#cv2.imshow('', seg_color)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Histograma de frecuencias

import matplotlib.pyplot as plt

arreglo_img = img_gris.flatten()

plt.hist(img_gris.flatten(), bins = 15)
plt.savefig('histograma.png')
plt.show()

#binaria = np.uint8(255*(img_gris<139))

# utilizando CV2 con Otsu}

th_otsu,_ = cv2.threshold(img_gris, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

binaria_otsu = np.uint8(255*(img_gris<th_otsu))

cv2.imwrite('binaria_otsu.jpg', binaria_otsu)