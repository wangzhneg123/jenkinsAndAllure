# coding: utf-8
import os
import xlrd
# 获取当前文件所在的路径  [注意一定要是用这个绝对路径  重要指数*****]
ProjectPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


# ----------------------------------------------------------excel文件读取的封装
def readFile_excelContent(fileName, tableName):
    """
    用来读取excel的方法，为参数化使用的工具类
    :param fileName: excel文件的名字【注：要添加后缀】
    :param tableName: 要读取那个sheet表名
    :return: 一个list 列表 形式[(),(),...]
    """
    filePath = ProjectPath + "\\data\\" + fileName

    readbook = xlrd.open_workbook(filePath)
    sheet = readbook.sheet_by_name(tableName)
    nrows = sheet.nrows  # 行
    ncols = sheet.ncols  # 列
    mlist = []
    for row in range(1, nrows):
        tempList = []
        for col in range(0, ncols):
            tempList.append(sheet.cell_value(row, col))
        tup1 = tuple(tempList)
        mlist.append(tup1)
    return mlist


# -----------------------------------------------------------yaml文件读取的封装
# def readFile_yaml(fileName=""):
#
#     return []
