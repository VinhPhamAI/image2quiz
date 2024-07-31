import cv2
import pytesseract
from pytesseract import Output
import numpy as np
from PIL import Image

image_path = 'images/van.png'

img = cv2.imread(image_path)

# Chuyển ảnh sang màu xám
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Áp dụng ngưỡng
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Tìm các contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Lọc các contours theo kích thước
min_contour_area = 1000
filtered_contours = [c for c in contours if cv2.contourArea(c) > min_contour_area]

# Vẽ các contours lên ảnh gốc
for contour in filtered_contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Hiển thị ảnh đã xử lý
cv2.imshow('Detected Bounding Boxes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Sử dụng Tesseract để nhận diện văn bản và các bounding box
d = pytesseract.image_to_data(Image.open(image_path), output_type=Output.DICT)

n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Hiển thị kết quả nhận diện văn bản
cv2.imshow('Detected Text Bounding Boxes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu ảnh đã xử lý
cv2.imwrite('output_image_with_bounding_boxes.png', img)
