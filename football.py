import random
import cv2
import numpy as np

width = 400
height = 700
football_image = np.ones((width, height, 3))
football_image = np.array(football_image, dtype=np.uint8)

for i in range(7):
    football_image[:, (i*100):(i*100 + 100), 1] = 100 + ((i+1) % 2)*50


cv2.rectangle(football_image, (30, 30),
              (height - 30, width - 30), (255, 255, 255), 4)
cv2.rectangle(football_image, (30, 110),
              (140, width - 110), (255, 255, 255), 4)
cv2.rectangle(football_image, (30, 150), (80, width - 150), (255, 255, 255), 4)
cv2.rectangle(football_image, (height - 30, 110),
              (height - 140, width - 110), (255, 255, 255), 4)
cv2.rectangle(football_image, (height - 30, 150),
              (height - 80, width - 150), (255, 255, 255), 4)
cv2.circle(football_image, (height//2, width//2), 70, (255, 255, 255), 4)
cv2.circle(football_image, (height//2, width//2), 0, (255, 255, 255), 15)
cv2.line(football_image, (height//2, 30),
         (height//2, width-30), (255, 255, 255), 4)


cv2.imshow('football image', football_image)
cv2.imwrite('output\Football_image.jpg', football_image)
cv2.waitKey()
