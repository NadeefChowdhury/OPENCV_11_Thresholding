import cv2 as cv
import numpy as np
img =  cv.imread('C:/Users/User 2/Desktop/cats.jpg')
cv.imshow('Meow', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray, 180, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded", thresh)

threshold, thresh_inv = cv.threshold(gray, 180, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresholded", thresh_inv)


##Adaptive thresholding lets the computer calculate the threshold value and it is more effective
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive', adaptive_thresh)


cv.waitKey(0)