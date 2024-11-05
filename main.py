import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('image.jpg')

#モノクロに変換
#0~256
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#中央値フィルター適用
#カーネルサイズ->3
filtered = cv2.medianBlur(gray, 3)


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('original')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.title('median filter')
plt.imshow(filtered, cmap='gray')
plt.show()
