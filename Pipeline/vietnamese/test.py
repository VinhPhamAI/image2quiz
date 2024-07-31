import json

# Mở và đọc nội dung tệp JSON
with open('que_img/response.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Duyệt qua từng câu hỏi trong JSON
for key, value in data.items():
    print(value)
