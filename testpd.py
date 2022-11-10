'''

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

frominlist_byte = bytearray(frompinlist)
topinlist_byte =  bytearray(topinlist)
print(len(topinlist_byte))
#print(frompinlist.to_bytes(1, byteorder='big'))
'''
i = 63
j = 127

if (i in range(0,64) and j in range(0,64)):
    print('Specs 0 to 10 Ohm')
elif i in range(0,64) and j in range(64,128):
    print('Spec > 1K Ohm')
elif i in range(64,128) and j in range(0,64):
    print('Spec > 1K Ohm')
elif i in range(64,128) and j in range(64,128):
    print('Specs 0 to 10 Ohm')