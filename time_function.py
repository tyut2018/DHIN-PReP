import numpy as np
import math
import xlrd


def excel_to_matrix(path, index):
    table = xlrd.open_workbook(path).sheets()[index]
    row = table.nrows
    col = table.ncols
    datamatrix = np.zeros((row, col))
    for x in range(col):
        cols = np.matrix(table.col_values(x))
        datamatrix[:, x] = cols
    datamatrix = datamatrix.astype(np.int)
    return datamatrix


def timeImpactFun(timeInfData):
    matrix = np.zeros(12561).reshape(1, 12561)
    preIndex = 0
    preYear = 0
    domainCount = 0
    prePathCount = 0
    m, n = timeInfData.shape
    for i in range(m):
        if timeInfData[i][0] == preIndex:
            domainCount += 1
            prePathCount += timeInfData[i][2]
            preYear += timeInfData[i][3]
        else:
            value = (preYear * 0.01 + pow(10, -50)) / (prePathCount * domainCount * 3 * domainCount)
            matrix[0, preIndex] = math.exp(-value)
            print(matrix[0, preIndex])
            domainCount = 1
            preIndex = timeInfData[i][0]
            prePathCount = timeInfData[i][2]
            preYear = timeInfData[i][3]
    value = (preYear * 0.01 + pow(10, -50)) / (prePathCount * domainCount * 3 * domainCount)
    matrix[0, preIndex] = math.exp(-value)
    print (matrix[0, preIndex])
    return matrix


if __name__ == '__main__':
    datafile = r'E:/hujialun/for_DHIN-PReP/time_function2.xls'
    timeInfData = excel_to_matrix(datafile, 0)
    matrixTimeImp = timeImpactFun(timeInfData)
