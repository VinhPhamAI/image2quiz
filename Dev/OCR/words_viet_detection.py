import cv2
import pytesseract
from PIL import Image, ImageDraw
import numpy as np

# Load the image from the file path
image_path = 'images/dialy2.png'
image_cv = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

# Perform OCR to detect text
detection_data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT, lang='viet')
# Convert the OpenCV image to a Pillow image
image_pil = Image.fromarray(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))

text = "Theo"
def search_text(text):
    n_boxes = len(detection_data['level'])
    for i in range(n_boxes):
        if text in detection_data['text'][i]:
            (x, y, w, h) = (detection_data['left'][i], detection_data['top'][i], detection_data['width'][i], detection_data['height'][i])
            # Draw a rectangle around the detected text
            draw = ImageDraw.Draw(image_pil)
            draw.rectangle(((x, y), (x + w, y + h)), outline="red", width=2)
            # Output the coordinates of the rectangle
            print(f"Detected '{text}' at coordinates: Top-Left ({x}, {y}), Bottom-Right ({x + w}, {y + h})")

    # Save the image with the highlighted text
    image_pil.save("highlighted_text.png")

text2 = "Cho"
search_text(text2)
# Search for the specific text


