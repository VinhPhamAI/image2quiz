import json


def search_question(source_text_path):
    with open(source_text_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    words_question_img = []
    for key, value in data.items():
        question = value.get('Câu hỏi', '')
        # Tách câu hỏi dựa trên ký tự "\n"
        parts = question.split('\n')
        first_part = parts[0]  # Lấy phần đầu tiên trước "\n"

        # Tách phần đầu tiên thành các từ
        words = first_part.split()
        words_question_img.append(words)
    return words_question_img


word_question_img = search_question('que_img/response.json')
print(word_question_img)