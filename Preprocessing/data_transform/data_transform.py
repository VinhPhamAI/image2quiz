from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox
import docx2pdf
import win32com.client
import os


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




