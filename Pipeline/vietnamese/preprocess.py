from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox
import docx2pdf
import win32com.client
import os
from PIL import Image

import numpy as np
import requests

import requests
from PIL import Image
from io import BytesIO
import torch
import shutil 


class PDF2img: 
    def __init__(self, folder_path): 
        self.folder_path = folder_path

    def convert(self, file_path, save_folder): 

        try : 
            print(file_path)
            images = convert_from_path(file_path)
            print(3)
            for i in range(len(images)): 
                images[i].save(save_folder + '/' + '_' + str(i) + '_' + '.png' , 'PNG')

        except  :
            Result = "NO pdf found"
            messagebox.showinfo("Result", Result)

class Doc2img: 
    def __init__(self, folder_path): 
        self.folder_path = folder_path

    def convert(self, file_path, save_folder):
        try: 
            docx2pdf.convert(file_path, save_folder)
            images = convert_from_path(save_folder)

            for i in range(len(images)): 
                images[i].save(save_folder + '_' + str(i) , 'PNG')
        except : 
            result = "No docx found"
            messagebox.showinfo("Result", result)



class pptx2img: 
    def __init__(self, folder_path): 
        self.folder_path = folder_path
        self.application = win32com.client.Dispatch("PowerPoint.Application")


    def convert(self, file_path, save_folder): 
        try:
            # khởi tạo presentation 
            Presentation = self.application.Presentations.Open(file_path, WithWindow=False)

            # set folder để lưu file 
            slides_folder = os.path.join(os.path.dirname(save_folder), "Slides")
            if not os.path.exists(slides_folder):
                os.makedirs(slides_folder)

            # duyệt qua từng slide để lưu ảnh 
            for i, slide in enumerate(Presentation.Slides):
                image_path = os.path.join(slides_folder, f"{i + 1}.png")
                slide.Export(image_path, "JPG")

            
            Presentation.Close()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            
            self.application.Quit()

# đầu vào là đường dẫn tới file 
def transform_input(data_path, save_path): 
    # kiểm tra file có tồn tại hay không
    if not os.path.exists(data_path):
        messagebox.showinfo("Result", "No file found")
    
    file_name = os.path.basename(data_path)
    if file_name.endswith(".docx"): 
        result = Doc2img(data_path)
        result.convert(data_path, save_path)

    elif file_name.endswith(".pdf"): 
        result = PDF2img(data_path)
        print(os.path.exists(data_path))
        result.convert(data_path, save_path)

    elif file_name.endswith(".pptx"): 
        result = pptx2img(data_path)
        result.convert(data_path, save_path)

    else : 
        shutil.move(data_path, save_path)
    

if __name__ == '__main__': 
    data_path = 'Pipeline/vietnamese/preprocessing_img/de-thi-thu-toan-tot-nghiep-thpt-2024-lan-2-truong-thpt-mai-anh-tuan-thanh-hoa.pdf'
    save_path = './Pipeline/vietnamese/first_img'

    data_path = os.path.join(os.getcwd(), 'Pipeline', 'vietnamese', 'preprocessing_img')
    save_path = os.path.join(os.getcwd(), 'Pipeline', 'vietnamese', 'first_img')
    file_name = os.listdir(data_path)[0]
    data_path = os.path.join(data_path, file_name)
    print(data_path)
    transform_input(data_path, save_path)