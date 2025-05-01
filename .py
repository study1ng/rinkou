import cv2
import matplotlib.pyplot as plt

# 画像の読み込み（BGR形式）
bgr_img = cv2.imread('static/images/rgb.jpeg')

# BGRからYUVに変換
yuv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2YUV)

# チャンネルに分離（Y, U, V）
y_channel, u_channel, v_channel = cv2.split(yuv_img)

# 表示
plt.figure(figsize=(10, 8))

# 元画像（BGR→RGBに変換して表示）
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB))
plt.axis('off')

# Yチャンネル
plt.subplot(2, 2, 2)
plt.imshow(y_channel, cmap='gray')
plt.axis('off')

# Uチャンネル
plt.subplot(2, 2, 3)
plt.imshow(u_channel, cmap='gray')
plt.axis('off')

# Vチャンネル
plt.subplot(2, 2, 4)
plt.imshow(v_channel, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
