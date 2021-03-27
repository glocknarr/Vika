from PIL import Image
from PIL.ExifTags import TAGS
import json
import os


'''
Функция для очистки exif-данных переданного файла.
Файл-источник перезаписывается!
'''
def clear_exif(file_name):
    image = Image.open(file_name)
    image.save(file_name)
    print("\tEXIF clear!")


'''
Получить все exif-данные из изображения.
Возвращает данные в json 
'''
def read_exif(file_name):
    image = Image.open(file_name)
    exif = image._getexif()
    if exif:
        response = []
        for tag, value in exif.items():
            item = TAGS[tag]
            new_line = [item, value]
            response.append(new_line)
            # print(f'{TAGS[tag]}: {value} ({type(value)})')
        return response
    else:
        return 'None'


if __name__ == '__main__':
    file_name = 'DSC01062.JPG'
    resp = read_exif(file_name)
    if resp != "None":
        for item in read_exif(file_name):
            print(f'{item[0]}: {item[1]}')
        # clear_exif(file_name)
    else:
        print(resp)


