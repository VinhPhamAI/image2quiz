import cv2
import pytesseract
from PIL import Image, ImageDraw
import numpy as np

def search_text(image_path, text):
    image_cv = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

    # Perform OCR to detect text
    detection_data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT, lang='viet')
    # Convert the OpenCV image to a Pillow image
    image_pil = Image.fromarray(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))
    n_boxes = len(detection_data['level'])
    words_position = []
    for i in range(n_boxes):
        if text in detection_data['text'][i]:
            (x, y, w, h) = (detection_data['left'][i], detection_data['top'][i], detection_data['width'][i], detection_data['height'][i])
            # Draw a rectangle around the detected text
            draw = ImageDraw.Draw(image_pil)
            draw.rectangle(((x, y), (x + w, y + h)), outline="red", width=2)
            # Output the coordinates of the rectangle
            print(f"Detected '{text}' at coordinates: Top-Left ({x}, {y}), Bottom-Right ({x + w}, {y + h})")
            words_position.append([x, y, x+w, y+h])

    # Save the image with the highlighted text
    image_pil.save("folder_check/highlighted_text.png")
    return words_position


text = ["Cho", "biểu", "Theo", "với", "cao"]
all_positions = []

# Get positions of all occurrences of text
for t in range(len(text)):
    positions = search_text("images/dialy2.png", text[t])
    all_positions.append(positions)

# Extract and print top positions for each word
for i, word_positions in enumerate(all_positions):
    top_positions = [pos[1] for pos in word_positions]  # Extract the top (y) positions
    print(f"Top positions for '{text[i]}': {top_positions}")

