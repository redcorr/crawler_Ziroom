import re
from text_recognition import text_recognition


def get_price(price_items):
    num_pool_link = 'http:'+re.search('//.*\\)', price_items[0])[0][:-1]
    num_pool = text_recognition(num_pool_link)
    price = 0
    for price_item in price_items:
        num_position_px = re.search('n:\\s.*px', price_item)[0][3:-2]
        num_position = -int(float(num_position_px) / 21.4)
        num = num_pool[num_position]
        price = price * 10 + int(num)
    return price
