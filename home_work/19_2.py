import csv
from openpyxl import Workbook

with open('my_dict.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]
for row in data:
    del row[2]
transposed_data = list(map(list, zip(*data)))

transposed_data.insert(0, [])

workbook = Workbook()
worksheet = workbook.active
for row in transposed_data:
    worksheet.append(row)
for i, column in enumerate(worksheet.columns, start=1):
    column_letter = column[0].column_letter
    column_name = f"Person{i-1}" if i > 1 else column[0].value
    worksheet[f"{column_letter}1"] = column_name
workbook.save('my_dict.xlsx')
