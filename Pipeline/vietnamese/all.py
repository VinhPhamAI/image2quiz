from dla import get_image_position
from text_vn_recognition import get_text_from_image
from white_box import white_boxes, extract_bounding_boxes
from find_question import return_response

image_path = 'images/dialy2.png' # Đề thi
image_save_path = "image_save/" # Lưu vị trí hình ảnh được detect
llm_question_image_path = "que_img/response.json"


# DLA xác định ảnh
image_position = get_image_position(image_path)
print(image_position)
print(len((image_position)))

# Trường hợp không có ảnh nào xuất hiện (thuần text)
if (len(image_position) == 0):
    pass

# Trường hợp có ảnh xuất hiện
else :
    # Bôi trắng các image và trả về file chứa ảnh đã được bôi trắng các image
    white_boxes_output_path = white_boxes(image_path, image_position)
    # Lưu lại các image đã được DLA detect
    extract_bounding_boxes(image_path, image_position)
    # OCR những ảnh đã được bôi trắng
    text_ocr = get_text_from_image(white_boxes_output_path)
    
    file_path = 'folder_check/output.txt'
    with open(file_path, 'r') as file:
        content = file.read()
    # LLM detect các câu cần image trước.
    return_response(content, llm_question_image_path)
    # Tìm image đó thuộc question nào và assign nó cho câu hỏi đó.

    # Đưa vào LLM và dùng spell checking để nhận diện những câu còn lại.

    # Output : json file (Nếu câu đó yêu cầu ảnh thì đính kèm thêm link folder chứa ảnh đó)

