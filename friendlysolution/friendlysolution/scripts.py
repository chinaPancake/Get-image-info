import requests
import json
import webcolors
import os
from PIL import Image
import glob
import time
resp = requests.get('https://jsonplaceholder.typicode.com/photos')

def get_dominant_color(pil_img):
    img = pil_img.copy()
    img = img.convert("RGB")
    img = img.resize((1, 1), resample=0)
    dominant_color = img.getpixel((0, 0))
    dominant_color = webcolors.rgb_to_hex(dominant_color)
    return dominant_color


def get_heigh_width_color(filename):
    im = Image.open(filename)
    file_url = os.path.abspath(filename)
    img = im.copy()
    img = img.convert("RGB")
    img = img.resize((1, 1), resample=0)
    dominant_color = img.getpixel((0, 0))
    dominant_color = webcolors.rgb_to_hex(dominant_color)
    color = dominant_color
    width, height, = im.size
    return width, height, file_url, color

for image in resp.json():
    url = image["url"]
    image_resp = requests.get(url=f'{url}.png')
    if image_resp.status_code:
        fp = open(f'images/{url.rsplit("/", 1)[1]}.png', 'wb')
        fp.write(image_resp.content)
        fp.close()
        for filename in glob.glob(f'images/{url.rsplit("/", 1)[1]}.png'):
            result = get_heigh_width_color(filename)
            

    photo_id = image["id"]
    albumid = image["albumId"]
    title = image["title"]

    api_resp = requests.post('http://127.0.0.1:8000/model-viewsett/', json = {
    "photo_id": photo_id,
    "title": f"{title}",
    "albumId": albumid,
    "width": result[0],
    "height": result[1],
   "dominantcolor": result[3],
   "url": result[2],
   "image": None
})
    print(f'{api_resp.status_code}, {api_resp.json()}')
