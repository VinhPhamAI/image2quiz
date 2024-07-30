from pdf2image import convert_from_path
from tkinter import *
from tkinter import messagebox


class PDF2img: 
    def __init__(self, folder_path): 
        self.folder_path = folder_path

    def convert(self, file_path, save_folder): 

        try : 
            images = convert_from_path(file_path)
            for i in range(min(len(images), 4)): 
                images[i].save(self.folder_path + '_' + str(i) + '_' + save_folder , 'PNG')

        except  :
            Result = "NO pdf found"
            messagebox.showinfo("Result", Result)




