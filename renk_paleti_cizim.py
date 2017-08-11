#! /usr/bin python
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def palet_callback(x):
    pass


def sekil_ciz(event, x, y, flags, param):
    global ix, iy
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        cv2.line(resim, (ix, iy), (x, y), (mavi_position, yesil_position, kirmizi_position), 3)



palet_alani = np.zeros((300, 300, 3), np.uint8)
cv2.namedWindow('palet')
# trackbar oluşturuyoruz
resim = cv2.imread('dybala.jpg', 1)
cv2.namedWindow('dybala')
cv2.setMouseCallback('dybala', sekil_ciz)
cv2.createTrackbar('K', 'palet', 0, 255, palet_callback)
cv2.createTrackbar('Y', 'palet', 0, 255, palet_callback)
cv2.createTrackbar('M', 'palet', 0, 255, palet_callback)

while True:
    cv2.imshow('palet', palet_alani)
    cv2.imshow('dybala', resim)

    if cv2.waitKey(1) & 0xFF == 27:
        break
    kirmizi_position = cv2.getTrackbarPos('K', 'palet')
    yesil_position = cv2.getTrackbarPos('Y', 'palet')
    mavi_position = cv2.getTrackbarPos('M', 'palet')
    palet_alani[:] = [mavi_position, yesil_position, kirmizi_position]

cv2.destroyAllWindows()

