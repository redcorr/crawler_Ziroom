import get_page
import re
import get_single_page_items
import save_data


def get_save_all_pages_items():
    district = {
        'd23008614': '东城', 'd23008626': '西城', 'd23008613': '朝阳', 'd23008618': '海淀', 'd23008617': '丰台', 'd23008623':
        '石景山', 'd23008625': '通州', 'd23008611': '昌平', 'd23008615': '大兴', 'd23008629': '亦庄开发区', 'd23008624': '顺义',
        'd23008616': '房山', 'd23008620': '门头沟'}
    district_index = 0
    for district_code in district.keys():
        district_index += 1
        district_name = district.get(district_code)
        url = 'http://www.ziroom.com/z/z1-' + district_code + '-r0-p1/?cp=1TO2500&isOpen=0'
        first_page = get_page.get_page(url)
        try:
            page_amount = re.search('共\\d*页', first_page)[0][1:-1]
        except TypeError:
            page_amount = 1
        for i in range(int(page_amount)):
            print('[' + district_name + ']' + str(district_index) + '/' + '13' + ' * ' + str(i + 1) + '/' + str(
                page_amount) + ' started')
            url = 'http://www.ziroom.com/z/z1-' + district_code + '-r0-p' + str(i + 1) + '/?cp=1TO2500&isOpen=0'
            items = get_single_page_items.get_single_page_items(district_name, get_page.get_page(url))
            save_data.save_data(items)
            print('[' + district_name + ']' + str(district_index) + '/' + '13' + ' * ' + str(i + 1) + '/' + str(
                page_amount) + ' completed')
