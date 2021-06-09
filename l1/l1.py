#coding:utf-8
import cv2
img = cv2.imread('lop.png')


cv2.imshow('window',img)
cv2.waitKey(0)
cv2.destoryAllWindows()
