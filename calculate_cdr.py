import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = '/home/legal/Datasets/REFUGE/crop_train/mask/g0009.bmp'
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image[image != 128] = 0
# plt.imshow(image)
# plt.axis('off')
# plt.show()

_, contours, hierarch = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

x0, y0, w0, h0 = cv2.boundingRect(contours[0])
x1, y1, w1, h1 = cv2.boundingRect(contours[1])
CDR = h1 / h0
cv2.rectangle(image, (x0, y0), (x0 + w0, y0 + h0), (255, 0, 0), 2)
cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 2)

cv2.putText(image,  'CDR is {:.2f}'.format(CDR),
            (int(x0), int(y0 - 10)),
            cv2.FONT_HERSHEY_COMPLEX_SMALL,
            0.8, (255, 0, 0), 1)
plt.imshow(image)
plt.axis('off')
plt.show()
# print(r1, r2)
# print(rect, rect2)
# cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
