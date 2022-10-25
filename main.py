'''Design and implement a simple backend application for managing photos.
We want to store photo title, album ID, width, height and dominant color (as a hex code) in local
database; the files should be stored in local filesystem.

Functionalities:
• Photos REST resource (list, create, update, delete)

Output fields (list): ID, title, album ID, width, height, color (dominant color), URL (URL to
locally stored file)

Input fields (create, update): title, album ID, URL
• Import photos from external API at https://jsonplaceholder.typicode.com/photos; via both
REST API and a CLI script

• Import photos from JSON file (expecting the same data format as the external API's); via
both REST API and a CLI script

Suggestions:
• Use any frameworks and libraries you'll find useful for the task (we prefer Django)
• Try to follow the best coding practices
• Don't be afraid to write tests '''

# done
# saved file in the local filesystem,
# get dominant hex color of the file,


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

'''        image_info_list.append(f'Width: {width}')
        image_info_list.append(f'Height: {height}')
        image_info_list.append(f'Url (file_url): {file_url}')'''
    # download files

'''    url = image["url"]
    image_resp = requests.get(url=f'{url}.png')

    if image_resp.status_code:
        fp = open(f'{url.rsplit("/", 1)[1]}.png', 'wb')
        fp.write(image_resp.content)
        fp.close()'''

# file_url -> twardego dysku
# color, width, height pliku pobieram z twardegi dysku
# id, title, album id - > pobieramy z requesta na strone 

'''image_list.append(f'Id: {id},Title: {title}, AlbumId: {albumId},Width: {im.width}, Height: {im.height},  Color: {get_dominant_color(im)}, Url (path to file): {file_url}')
print(image_list)'''

# Zapisywanie width hegih color file_url do list, wszystko osobno 
