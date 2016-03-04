#!/usr/bin/env python
# coding=utf-8

import cv2
import numpy as np

drawing = np.zeros([500, 500, 3])
cv2.rectangle(drawing, (0, 0), (250, 250), (100, 99, 159), -1)
cv2.imshow("result", drawing)
cv2.waitKey()

