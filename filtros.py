# -*- coding: utf-8 -*-

# filtrado de imagenes

import cv2
import numpy as np

manzana = cv2.imread('carro.jpg')

cv2.imwrite('original.jpg', manzana)

#cv2.imshow("Original", manzana)

kernel_3x3 = np.ones((3,3))/(3*3)

output_3x3 = cv2.filter2D(manzana, -1, kernel_3x3)

cv2.imwrite('filtro3x3.jpg', output_3x3)

#cv2.imshow('filtro de 3x3', output_3x3)

kernel_11x11 = np.ones((11,11))/(11*11)

output_11x11 = cv2.filter2D(manzana, -1, kernel_11x11)

cv2.imwrite('filtro11x11.jpg', output_11x11)

#cv2.imshow('filtro de 11x11', output_11x11)

kernel_31x31 = np.ones((31,31))/(31*31)

output_31x31 = cv2.filter2D(manzana, -1, kernel_31x31)

cv2.imwrite('filtro31x31.jpg', output_31x31)

#cv2.imshow('filtro de 31x31', output_31x31)