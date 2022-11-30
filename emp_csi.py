import csv

csv_file = []


# открыть файл
def file_open(file_name):
    with open(file_name, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_file.append(row)
        print("Файл открыт. Записей: ", len(csv_file))
