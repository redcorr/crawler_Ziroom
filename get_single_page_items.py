import re

from bs4 import BeautifulSoup
from get_price import get_price


def get_single_page_items(district_name, html):
    soup = BeautifulSoup(html, 'html.parser')
    single_page_item = []
    room_list = soup.select(".Z_list-box > .item")
    for item in room_list:
        attempts = 0
        while attempts < 3:
            try:
                item = str(item)
                item_soup = BeautifulSoup(item, "html.parser")
                if re.search(r'banner-box|lz-panel|title release', str(item_soup)):
                    break
                try:
                    link = item_soup.find("a").get("href")[2:]
                except:
                    print('can not get page')
                    break
                intro1 = item_soup.h5.text
                block = re.search("·.*\\d居室", intro1).group(0)[1:-3]
                compartment_amount = re.search("\\d居室", intro1).group(0)[0:1]
                orientation = re.search("-.*", intro1).group(0)[1:-1]
                room_info_1 = item_soup.find(name="div", attrs={"class": ""}).text
                area = room_info_1[:room_info_1.find("㎡")]
                floor = room_info_1[room_info_1.find("|") + 2:-1]
                block_location = item_soup.find(name="div", attrs={"class": "location"}).text
                if '站' in block_location:
                    metro_location = block_location[block_location.find("区距") + 2:block_location.find("步行")]
                    metro_location_distance = block_location[block_location.find("行约") + 2:block_location.find("米")]
                else:
                    metro_location = 'null'
                    metro_location_distance = block_location.replace('\n', '')
                price_items = []
                for num_item in item_soup.findAll(name="span", attrs={"class": "num"}):
                    style = num_item.get("style")
                    price_items.append(style)
                try:
                    price = get_price(price_items)
                    if item_soup.find(name='span', attrs={'class': 'unit'}).text == '/天':
                        price = price * 30
                except:
                    print('can not get price')
                    break
                if re.search('转租', item):
                    sublet = True
                else:
                    sublet = False
                single_item = [district_name+'区', link, block, compartment_amount, orientation, area, floor, metro_location,
                               metro_location_distance, price, sublet]
                single_page_item.append(single_item)
                break
            except:
                attempts += 1
                print('failed')
                if attempts == 3:
                    print('can not get item')
                    break
    return single_page_item
