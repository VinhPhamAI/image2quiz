import google.generativeai as genai
from prompt import system_instruction_question_vn
import json


genai.configure(api_key="AIzaSyBHo2zdLSj-4uEop6r1CBtaKwuEExQlTDI")

model =  genai.GenerativeModel('gemini-1.5-pro-latest',
                               system_instruction=system_instruction_question_vn,
                               )

def return_response(content, output_path, model = model):
    
    response = model.generate_content(content)
    # In ra kết quảa
    json_str = (response.text).strip('```json\n').strip('```')
    # Chuyển đổi chuỗi JSON thành đối tượng Python
    response_json = json.loads(json_str)
    # Lưu vào tệp JSON
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(response_json, json_file, ensure_ascii=False, indent=4)
