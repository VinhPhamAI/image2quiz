import easyocr
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def load_image(image_path):
    # Kiểm tra xem tệp có tồn tại không
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file at {image_path} does not exist.")
    
    # Đọc ảnh
    image = cv2.imread(image_path)
    
    # Kiểm tra xem ảnh có được đọc thành công không
    if image is None:
        raise IOError(f"Unable to open or read the file at {image_path}.")
    
    return image

def detect_words(image_path):
    # Tạo đối tượng OCR reader
    reader = easyocr.Reader(['en', 'vi'])  # Hỗ trợ tiếng Anh và tiếng Việt

    # Đọc văn bản từ ảnh
    results = reader.readtext(image_path, detail=1)
    return results

def plot_word_bboxes(image, results):
    # Hiển thị ảnh
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    for (bbox, text, prob) in results:
        # Vẽ bounding box
        rect = patches.Polygon(bbox, closed=True, edgecolor='r', linewidth=2, facecolor='none')
        plt.gca().add_patch(rect)
        plt.text(bbox[0][0], bbox[0][1] - 10, text, fontsize=12, color='r', weight='bold')
    
    plt.show()

def main(image_path):
    try:
        # Bước 1: Đọc ảnh
        image = load_image(image_path)

        # Bước 2: Nhận diện từng từ
        results = detect_words(image_path)

        # Bước 3: Hiển thị kết quả
        plot_word_bboxes(image, results)

    except Exception as e:
        print(f"An error occurred: {e}")

# Đường dẫn đến tệp ảnh
image_path = 'images/stanford.jpg'

# Chạy pipeline
main(image_path)
