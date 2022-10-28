import requests
import json
import webcolors
import os
from PIL import Image
import glob

# open a json file
resp = open('./friendlysolution/photos.json')
# load json file as data
data = json.load(resp)

    #function to get all image information
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

    # this is for loop to get all data from json file
for image in data:
    url = image["url"]
   # here we get image["url"] to get link to download image file 
    image_resp = requests.get(url=f'{url}.png')
    # if respond for our request is 200 (ok) then we save the file into our computer and fetch all data that we need
    if image_resp.status_code:
        fp = open(f'images/{url.rsplit("/", 1)[1]}.png', 'wb')
        fp.write(image_resp.content)
        fp.close()
        for filename in glob.glob(f'images/{url.rsplit("/", 1)[1]}.png'):
            result = get_heigh_width_color(filename)

    # after that we close the file and get another information from jsno file
    photo_id = image["id"]
    albumid = image["albumId"]
    title = image["title"]
    # and here we make a POST request to upload all data into our server
    api_resp = requests.post('http://127.0.0.1:8000/model-viewsett/', json = {
    "photo_id": photo_id,
    "title": f"{title}",
    "albumId": albumid,
    "width": result[0],
    "height": result[1],
   "dominantcolor": result[3],
   "url": result[2],
})

    print(f'{api_resp.status_code},{photo_id}, {title}, {albumid}, {result[0]},{result[1]},{result[2]},{result[3]}')
