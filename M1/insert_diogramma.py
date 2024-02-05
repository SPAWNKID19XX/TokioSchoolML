import openpyxl
from openpyxl.chart import LineChart
import matplotlib.pyplot as plt

xlsx_file = "M1/solutions.xlsx"
wb = openpyxl.load_workbook(xlsx_file)

'''
for sheet in wb.sheetnames:
    chart = 
    for row in wb[sheet]:
        print(row[0].value, row[1].value)'''