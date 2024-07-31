from ultralytics import YOLO
import cv2 
import matplotlib.pyplot as plt  
import os 

# dựng tạm một class model để infer ra kết quả với input vào là ảnh 
'''
names: {0: 'Caption', 1: 'Footnote', 2: 'Formula', 3: 'List-item', 4: 'Page-footer', 5: 'Page-header', 
        6: 'Picture', 7: 'Section-header', 8: 'Table', 9: 'Text', 10: 'Title'}
'''
class Model: 
    def __init__(self, path): 
        self.model = YOLO(path)
        self.ENTITIES_COLORS = {
            "Caption": (191, 100, 21),
            "Footnote": (2, 62, 115),
            "Formula": (140, 80, 58),
            "List-item": (168, 181, 69),
            "Page-footer": (2, 69, 84),
            "Page-header": (83, 115, 106),
            "Picture": (255, 72, 88),
            "Section-header": (0, 204, 192),
            "Table": (116, 127, 127),
            "Text": (0, 153, 221),
            "Title": (196, 51, 2)
        }
        self.image_in_img = []
        self.text_in_img = []

        self.img_position = {}
        self.BOX_PADDING = 2

    def detect(self, image_path):
        # load ảnh 
        image = cv2.imread(image_path)

        


        if image is None: return image 

        result = self.model.predict(source = image, conf = 0.2, iou = 0.8)
        result[0].save("result.png")
        boxes = result[0].boxes

        for box in boxes: 
            detection_clf  = round(box.conf.item(), 2)
            cls = list(self.ENTITIES_COLORS)[int(box.cls)]


            start_box = (int(box.xyxy[0][0]), int(box.xyxy[0][1]))
            end_box = (int(box.xyxy[0][2]), int(box.xyxy[0][3]))


            sub_img = image.copy()
            sub_img = sub_img[start_box[1]:end_box[1], start_box[0]:end_box[0]]

            if box.cls == 8 or box.cls == 6: 
                self.image_in_img.append(sub_img)
                self.img_position[len(self.image_in_img) - 1] =  {(start_box, end_box)}

                continue 
            if box.cls in [2, 3, 9]: 
                self.text_in_img.append(sub_img)
                continue 
            


    def display(self, img, dpi = 80 ): 

        # lấy chiều cao, chiều rộng của ảnh 
        height, width, = img.shape[0], img.shape[1]

        figsize = (height / float(dpi), width / float(dpi))

        fig, ax = plt.subplots(figsize = figsize)

        ax.axis("off")
        ax.imshow(img, cmap = 'gray')

        plt.show()

        


    def save(self, folder_path): 
        cwd = os.getcwd()        
        folder_path = os.path.join(cwd, folder_path)
        if not os.path.exists(folder_path):
            print(1)
            return None 
        
        img_file_path = os.path.join(folder_path, "image_img")
        for i in range(len(self.image_in_img)): 
            cv2.imwrite(img_file_path + str(i) + '.png',   self.image_in_img[i])

        text_file_path = os.path.join(folder_path, "text_img")
        for i in range(len(self.text_in_img)): 
            cv2.imwrite(text_file_path + str(i) + '.png', self.text_in_img[i])


    def test(self, image_path): 
        result = self.detect(image_path)
        return result
    

if __name__ == '__main__': 
    model = Model('Multiple-Choice-Question-Detection/best.pt')
    model.detect('Multiple-Choice-Question-Detection/8-de-thi-vao-lop-10-mon-toan-01.png')
    
    






