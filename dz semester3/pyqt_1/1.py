import csv


with open('ikea.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    expensive = sorted(reader, key=lambda x: int(x['price']), reverse=True)

for record in expensive[:10]:
    print(record)


"""
with open('ikea.csv', "r", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index > 10:
            break
        print(row)
"""