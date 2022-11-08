from openpyxl import load_workbook
frompinlist = []
topinlist = []
minvallist = []
maxvallist = []
workbook = load_workbook(filename="Input File.xlsx")
sheet = workbook.active
nr = sheet.max_row
for i in range(8, nr):
    frompinlist.append(sheet.cell(i, 1).value)
    topinlist.append(sheet.cell(i,3).value)
    minvallist.append(sheet.cell(i,6).value)
    maxvallist.append(sheet.cell(i, 7).value)

print(minvallist)
