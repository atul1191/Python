import xlwt

def excel_write():
    workbook = xlwt.Workbook(encoding="utf=8")
    sheet1 = workbook.add_sheet("First")
    sheet2 = workbook.add_sheet("Second")
    
    sheet1.write(0,0,"This is First")
    sheet2.write(0,5,"This is Second")
    
    workbook.save("C:/Users/Atul/Downloads/Python.xls")
    print("saved")

if __name__ == '__main__':
    excel_write()
    