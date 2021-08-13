
from openpyxl import Workbook,load_workbook
from openpyxl.styles import *

################# insert excel  ############

def insertExcel(args,store):

    wb = load_workbook('SW_version_release_test.xlsx')
    ws1 = wb[store]
    for i in args:
        new_commit = []
        for value in i:
            new_commit.append(i[value])
        ws1.append(new_commit)
    wb.save('SW_version_release_test.xlsx')
