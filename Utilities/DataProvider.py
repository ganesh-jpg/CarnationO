import openpyxl
from Utilities import ExcelReader

def get_data(sheetName):
    path = "..\\Excel\\Test.xlsx"
    workbook = openpyxl.load_workbook(path)
    sheet=workbook[sheetName]
    rowcnt= ExcelReader.get_rows(path,"Register")
    colcnt = ExcelReader.get_columns(path,"Register")
    mainlist = []
    for i in range(2, rowcnt+1):
        datalist=[]
        for j in range(1,colcnt+1):
            data= sheet.cell(row=i,column=j).value
            datalist.insert(j,data)
        mainlist.insert(i,datalist)
    return mainlist

#print(get_data("Register"))