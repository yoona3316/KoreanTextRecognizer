from PIL import Image, ImageDraw, ImageFont
import json


class ImageCreator:
    def __init__(self, img_path, pure_data_path, json_path, type, size):
        self.img_path = img_path
        self.pure_data_path = pure_data_path
        self.json_path = json_path
        self.type = type
        self.size = size

    def load_json(self):
        with open(self.json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        return json_data

    def create_image(self):
        json_data = self.load_json()
        for key, value in json_data.items():
            fontsize = 30
            font = ImageFont.truetype('../Font/godoMaum.ttf', fontsize)
            img_name = f'{self.type}_{key}.jpeg'
            img = Image.new('RGB', size=size, color='white')
            d = ImageDraw.Draw(img)
            text_size = d.textsize(value['name'], font)
            img = img.resize(text_size)
            d = ImageDraw.Draw(img)
            d.text((0, 0), value['name'], fill=(0, 0, 0), font=font)
            img.save(self.img_path+img_name)

# img_path = '../Image/Fruits/'
# img_name = '1.jpeg'
# size = (60, 30)
# img = Image.new('RGB', size, color='white')
# img.save(img_path+img_name)

img_path = '../Image/Fruits/'
pure_data_path = '../Data/pure_data'
json_path = '../Data/data_list.json'
type = "Fruits"
size = (60, 30)

if __name__=='__main__':
    ImageCreator(img_path, pure_data_path, json_path, type, size).create_image()