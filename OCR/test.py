import easyocr
import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def load_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"The file at {image_path} does not exist.")
    
    image = cv2.imread(image_path)
    if image is None:
        raise IOError(f"Unable to open or read the file at {image_path}.")
    
    return image

def detect_words(image_path):
    try:
        reader = easyocr.Reader(['en', 'vi'])  # Initialize OCR for English and Vietnamese
    except Exception as e:
        raise RuntimeError(f"Error initializing OCR reader: {e}")
    
    try:
        results = reader.readtext(image_path, detail=1)
    except Exception as e:
        raise RuntimeError(f"Error detecting text: {e}")
    
    return results

def plot_word_bboxes(image, results, save_path=None):
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    for (bbox, text, prob) in results:
        rect = patches.Polygon(bbox, closed=True, edgecolor='r', linewidth=2, facecolor='none')
        plt.gca().add_patch(rect)
        plt.text(bbox[0][0], bbox[0][1] - 10, f'{text} ({prob:.2f})', fontsize=12, color='r', weight='bold')
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

def main(image_path):
    try:
        image = load_image(image_path)
        results = detect_words(image_path)

        # Optional: Save the results plot as an image
        save_path = 'output.png'
        plot_word_bboxes(image, results, save_path=save_path)
        print(f"Resulting image saved as {save_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the image file
image_path = 'images/stanford.jpg'

# Run the pipeline
main(image_path)
