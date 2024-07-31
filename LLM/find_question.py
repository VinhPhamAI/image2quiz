from IPython.display import display
from IPython.display import Markdown
import google.generativeai as genai
import os
import time
import textwrap
from prompt import system_instruction_question
import json

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key="AIzaSyBHo2zdLSj-4uEop6r1CBtaKwuEExQlTDI")

model =  genai.GenerativeModel('gemini-1.5-pro-latest',
                               system_instruction=system_instruction_question,
                               )

file_path = 'text/text1.txt'
with open(file_path, 'r') as file:
    content = file.read()
    
response = model.generate_content(content)

# In ra kết quảa
print(response.text)

json_str = (response.text).strip('```json\n').strip('```')

# Chuyển đổi chuỗi JSON thành đối tượng Python
response_json = json.loads(json_str)

# Lưu vào tệp JSON
with open('output/response.json', 'w') as json_file:
    json.dump(response_json, json_file, indent=4)

print("Response has been saved to output/response.json")