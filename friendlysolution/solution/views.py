from django.http import HttpResponse
from multiprocessing.sharedctypes import Value
from sre_constants import CATEGORY_UNI_NOT_LINEBREAK
from tkinter import image_names
from urllib import response
from urllib.parse import urlsplit
import requests
import json
from PIL import Image, ImageColor
import glob
import webcolors
import os

def index(request):

    return HttpResponse("Hello, world. You're at the polls index.")

response_API = requests.get('https://jsonplaceholder.typicode.com/photos')
# id, title, album id, width, heigh, color (dominant color), url (url to locally stored file)
resp = requests.get('https://jsonplaceholder.typicode.com/photos')


image_info_dict = {

}
image_info_list = []

# function to get dominant color and change RGB into HEX
def get_dominant_color(pil_img):
    img = pil_img.copy()
    img = img.convert("RGB")
    img = img.resize((1, 1), resample=0)
    dominant_color = img.getpixel((0, 0))
    dominant_color = webcolors.rgb_to_hex(dominant_color)
    return dominant_color

for filename in glob.glob('*.png'):
    im = Image.open(filename)
    width, height, = im.size
    file_url = os.path.abspath(filename)
    color = get_dominant_color(im)
    new_url = f'https://via.placeholder.com/600{filename}'


print(image_info_dict)
save_to_json = json.dumps(image_info_dict)

with open('sample.json', 'w') as f:
    f.write(save_to_json)