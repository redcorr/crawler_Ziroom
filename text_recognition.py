import base64
import urllib
from typing import BinaryIO
from urllib.parse import urlencode
from urllib import request
import requests
from urllib.request import urlopen
import json
import ssl
from skimage import io
from PIL import Image


def text_recognition(image_url):
    client_id = '【百度云id】'
    client_secret = '【百度云key】'
    ssl._create_default_https_context = ssl._create_unverified_context
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&' \
           'client_id=' + client_id + '&client_secret=' + client_secret
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    res = requests.get(url=host, headers=headers).json()
    access_token = res['access_token']
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=' + access_token

    image = io.imread(image_url)
    io.imsave('ori.png', image)
    original_image = Image.open('ori.png')
    background = Image.new('RGBA', original_image.size, (255, 255, 255))
    background.paste(original_image, (0, 0, 300, 28), original_image)
    background.save('background_ed.png')

    f: BinaryIO = open(r'background_ed.png', "rb")
    op: bytes = f.read()
    img_r = base64.b64encode(op)
    params = {'image': img_r}
    params2 = urllib.parse.urlencode(params).encode(encoding='UTF8')
    request1 = request.Request(url, params2)
    request1.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urlopen(request1)

    content: object = response.read()
    result: object = content.decode()
    json1 = json.loads(result)
    words_result = json1['words_result']
    price_array = words_result[0]['words']
    return price_array
