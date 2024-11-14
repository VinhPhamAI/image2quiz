from dla import get_image_position
from text_vn_recognition import get_text_from_image
from white_box import white_boxes, extract_bounding_boxes
from llm import return_response_contain_image, return_response_alltext
from search_sentence_in_image import search_sentence, search_question, search_image_belong_question
from update_json_image import find_and_update_json

image_path = 'images/pdf_5.png' # Đề thi
all_text_path = 'all_text/response.json'
image_save_path = "image_save/" # Lưu vị trí hình ảnh được detect
question_image_path = "que_img/response.json"
file_path = 'folder_check/output.txt'


text_ocr = get_text_from_image(image_path)
with open(file_path, 'r') as file:
    content = file.read()
return_response_alltext(content, all_text_path)

# DLA xác định ảnh
image_position = get_image_position(image_path)
print(image_position)
print(len((image_position)))


# Trường hợp không có ảnh nào xuất hiện (thuần text)
if (len(image_position) > 0):
    # Bôi trắng các image và trả về file chứa ảnh đã được bôi trắng các image
    white_boxes_output_path = white_boxes(image_path, image_position)
    # Lưu lại các image đã được DLA detect
    extract_bounding_boxes(image_path, image_position)
    # OCR những ảnh đã được bôi trắng
    text_ocr = get_text_from_image(white_boxes_output_path)
    
    with open(file_path, 'r') as file:
        content = file.read()
    # LLM detect các câu cần image trước.
    return_response_contain_image(content, question_image_path)
    # Tìm câu hỏi đó ở vị trí nào trong image
    sentences = search_question(question_image_path)
    print("sentences: ", sentences)
    for sentence in sentences:
        words = sentence.split()  # Split the sentence into words
        first_three_words = ' '.join(words[:3])  # Join the first three words back into a string
        sentence_position = search_sentence(image_path, first_three_words)
        key = search_image_belong_question(sentence_position, image_position)
        image_file_name = "image_save/" + f"{key}.png"
        print(image_file_name)
        find_and_update_json(question_image_path, first_three_words, image_file_name)


