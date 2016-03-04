#!/usr/bin/env python
# coding=utf-8

import cv2
video = cv2.VideoCapture(0)
fbg =  cv2.BackgroundSubtractorMOG()

while True:
    ret, frame = video.read()
    fgmask = fbg.apply(frame)
    cv2.imshow('frame', fgmask)

video.release()
cv2.destroyAllWindows()



