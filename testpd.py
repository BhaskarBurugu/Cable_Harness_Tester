
'''
from openpyxl import load_workbook
frompinlist = []
topinlist = []
minvallist = []
maxvallist = []
workbook = load_workbook(filename="Reports/SelfTest/SelfTest10_11_2022_16_22_29.xlsx")
sheet = workbook.active
nr = sheet.max_row
for i in range(8, nr):
    fp=sheet.cell(i, 2).value
    frompinlist.append(fp)
    topinlist.append(sheet.cell(i,3).value)
    minvallist.append(sheet.cell(i,6).value)
    maxvallist.append(sheet.cell(i, 7).value)

    print(fp[4:])
'''
#frominlist_byte = bytearray(frompinlist)
#topinlist_byte =  bytearray(topinlist)
print((10).to_bytes(1, byteorder='big'))
