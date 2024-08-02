from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox
import docx2pdf
import win32com.client
import os
from huggingface_hub import from_pretrained_keras
from PIL import Image

import tensorflow as tf
import numpy as np
import requests

import requests
from PIL import Image
from io import BytesIO
from diffusers import LDMSuperResolutionPipeline
import torch


class PDF2img: 
    def __init__(self, folder_path): 
        self.folder_path = folder_path

    def convert(self, file_path, save_folder): 

        try : 
            images = convert_from_path(file_path)
            for i in range(len(images)): 
                images[i].save(self.folder_path + '_' + str(i) + '_' + save_folder , 'PNG')

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
                images[i].save(self.folder_path + '_' + str(i) + '_' + save_folder, 'PNG')
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



class Image_denoising: 
    def __init__(self): 
        
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_id = "CompVis/ldm-super-resolution-4x-openimages"
        self.pipeline = LDMSuperResolutionPipeline.from_pretrained(self.model_id)
        self.pipeline = self.pipeline.to(device)
    
    def denoising(self, img): 
        low_res_img = Image.open(BytesIO(img)).convert("RGB")
        low_res_img = low_res_img.resize((128, 128))
        upscaled_image = self.pipeline(low_res_img, num_inference_steps=100, eta=1).images[0]
        return upscaled_image
    
    def save(self, img, save_path): 
        img.save(save_path)

    
