import pytesseract
from PIL import Image

# Đường dẫn tới hình ảnh chứa câu hỏi trắc nghiệm
image_path = 'images/de-van-2024.jpg'
image = Image.open(image_path)

# Sử dụng Tesseract để nhận diện văn bản từ hình ảnh
text = pytesseract.image_to_string(image)
# Đường dẫn tới tệp đầu ra
output_path = 'output.txt'

# Ghi đầu ra vào tệp văn bản
with open(output_path, 'w', encoding='utf-8') as file:
    file.write(text)

print(f'Text has been written to {output_path}')
