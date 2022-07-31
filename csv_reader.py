import csv


def parse_email():
    with open('./csv/Base.csv', newline='', encoding='utf-8-sig') as csvfile:
        list_of_nicks = []
        reader = csv.reader(csvfile, delimiter=';', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            if '@' in row[1]:
                list_of_nicks.append(row[1].split("@")[0])
    return list_of_nicks
