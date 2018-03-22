# -*- coding:utf-8 -*-
'''**
**  author: Star-Chen
**  date: 2018.03.22
**  function: save lockscreen background image to current 'output' directory.
**'''
import os
import getpass
from PIL import Image

path = 'C:\Users\\' + getpass.getuser() + '\\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
output_path = '.\output'
if not os.path.exists(output_path):
                os.makedirs(output_path)
                print('create output dir complete!')
print('begin to save background img to output')
for root, dirs, files in os.walk(path):
    for file_name in files:
        img_file = os.path.join(path, file_name)
        img = Image.open(img_file)
        img_width, img_height = img.size
        if img_width == 1920 and img_height == 1080:
            output_filename = os.path.join(output_path, file_name[:5]+'.jpg')
            with open(img_file, 'rb') as file_in:
                with open(output_filename, 'wb') as file_out:
                    file_out.write(file_in.read())
print('work complete!')
os.startfile(output_path)
