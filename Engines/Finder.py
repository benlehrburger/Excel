# Find cell values to write out to new file

import pandas
from xlwt import Workbook

emails = {'email@email.com'}
names = {'file_name'}

for name in names:
    wb = Workbook()
    sheet1 = wb.add_sheet('Sheet 1')

    df = pandas.read_excel(name + '.xls', sheet_name='Sheet 1')

    rowNum = 0
    for row in range(df.shape[0]):
        for email in emails:
            if df.loc[row][1] == email:
                sheet1.write(rowNum, 0, df.loc[row][1])
                sheet1.write(rowNum, 1, df.loc[row][2])
                rowNum += 1
                print('Anotha one!')
                wb.save(name + '-Values.xls')

    print('Done!')
