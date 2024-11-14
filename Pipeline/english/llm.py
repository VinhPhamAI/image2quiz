import google.generativeai as genai
from prompt import *
import json

genai.configure(api_key="AIzaSyCISAOm_T7V1VwZ8BJtOPtvsyJ0u415GRA")

def return_response_contain_image(content, output_path):
    model =  genai.GenerativeModel('gemini-1.5-pro-latest',
                               system_instruction=system_instruction_question_img,
                               )
    response = model.generate_content(content)
    # In ra kết quảa
    json_str = (response.text).strip('```json\n').strip('```')
    # Chuyển đổi chuỗi JSON thành đối tượng Python
    response_json = json.loads(json_str)
    # Lưu vào tệp JSON
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(response_json, json_file, ensure_ascii=False, indent=4)

def return_response_alltext(content, output_path):
    model =  genai.GenerativeModel('gemini-1.5-pro-latest',
                               system_instruction=system_instruction_all_text,
                               )
    response = model.generate_content(content)
    # In ra kết quả
    json_str = (response.text).strip('```json\n').strip('```')
    # Chuyển đổi chuỗi JSON thành đối tượng Python
    response_json = json.loads(json_str)
    # Lưu vào tệp JSON
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(response_json, json_file, ensure_ascii=False, indent=4)

