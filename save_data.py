import csv


def create_file():
    file = open('rent_info_Ziroom.csv', 'w', encoding='UTF-8', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(['district', 'link', ' block', ' compartment_amount', ' orientation', ' area', ' floor', 'metro_location',
                         'metro_location_distance', 'price', 'sublet'])
    file.close()


def save_data(data):
    file = open('rent_info_Ziroom.csv', 'a', encoding='UTF-8', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)
    file.close()
