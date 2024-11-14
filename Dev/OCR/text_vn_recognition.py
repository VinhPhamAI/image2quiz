import pytesseract
import PIL
import cv2

img = cv2.imread("images/van.jpg", cv2.IMREAD_GRAYSCALE)
result = pytesseract.image_to_string(img, lang='viet+equ')
output_path = 'vi_output.txt'

# Ghi đầu ra vào tệp văn bản
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(result)

print(f'Text has been written to {output_path}')