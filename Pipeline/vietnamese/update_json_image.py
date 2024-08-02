import json

def find_and_update_json(json_path, target_phrase, new_value):
    # Đọc dữ liệu từ file JSON
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Kiểm tra từng câu hỏi và cập nhật nếu tìm thấy
    for question_key, question_value in data.items():
        if 'Câu hỏi' in question_value:
            question_text = question_value['Câu hỏi']
            if target_phrase in question_text:
                print(f"Found '{target_phrase}' in question '{question_key}'")
                question_value['link_image'] = new_value  # Thêm giá trị mới
                # Ghi dữ liệu đã cập nhật vào file JSON
                with open(json_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
                print(f"Added 'link_image' to question '{question_key}'")
                return question_key  # Trả về key của câu hỏi tìm thấy
    print(f"'{target_phrase}' not found in any question")
    return None
