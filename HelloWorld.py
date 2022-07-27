# -*-coding:utf-8 -*-

import pandas as pd
import numpy as np
import Bio

import matplotlib.pyplot as plt

#全部读取，输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替。数据为空，显示NaN。
"""
df = pd.read_csv(r"F:\Python\PythonProject\Data_Sheet_2_Quantitative Prediction"
                 r" of the Landscape of T Cell Epitope Immunogenicity in Sequence Space.csv",
                 )
"""

#print(df)

#to_string()返回 DataFrame 类型的数据(全部输出)
#print(df.to_string())

#读取特定的列
"""
df1 = pd.read_csv(r"F:\Python\PythonProject\Data_Sheet_2_Quantitative Prediction"
                  r" of the Landscape of T Cell Epitope Immunogenicity in Sequence Space.csv",
                  usecols=['DatasetType','Source'])
"""

#print(df1)


#读取前n行df.head(n)默认值为5
#print(df.head().to_string())

#读取末尾5行
#print(df.tail().to_string())

#info()返回表格基本信息
#print(df.info())


#print(type(df))
#print(type(df['DatasetType']))

"""
默认分隔符为“,”但可以使用任何其他定界符,例 “#”
pd.read_csv(".csv", seq = '#')
"""

#将header=None传递给read_csv()

"""
df2 = pd.read_csv(r"F:\Python\PythonProject\Data_Sheet_2_Quantitative Prediction"
                  r" of the Landscape of T Cell Epitope Immunogenicity in Sequence Space.csv",
                  header = 2,)
print(df2)
"""



#print(df2)
"""
df3 = pd.read_csv(r"F:\Python\PythonProject\Data_Sheet_2_Quantitative Prediction"
                  r" of the Landscape of T Cell Epitope Immunogenicity in Sequence Space.csv",
                  skiprows=[2, 3],)
"""

#print(df3)

#print(type(df))

#获取列名
#print(list(df))



#获取3,4行 的MHCType    Peptide
#print(df.loc[[3,4],['MHCType','Peptide']])


#切片获取3-5 DatasetType-Peptide
#print(df.loc[3:5,'DatasetType':'Peptide'])

#iloc 行号 列号70540行和7列之后的
#print(df.iloc[70540:,7:])

#根据条件索引,范围搜索
#print(df[df['Immunogenicity'] == "Positive"])

#print(df['Peptide'][df['Immunogenicity'] == "Positive"])

"""
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[9,8,7],[0,2,5],[7,9,2]])

#行向量元素平方和开根号，保留矩阵二维特性
norm1 = np.linalg.norm(arr1,axis=1,keepdims=True)
norm2 = np.linalg.norm(arr2,axis=1,keepdims=True)

arr1_norm = arr1 / norm1
arr2_norm = arr2 / norm2

cos = np.dot(arr1_norm,arr2_norm.T)
#print(cos)

x = arr1.reshape(1,6)
#print(x)
y = arr2.reshape(1,12)
#print(y)



matrix_1 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
matrix_2 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9],
                     [3, 2, 1],
                     [6, 5, 4],
                     [9, 8, 7]])

def non_loop(test_matrix, train_matrix):
    num_test = test_matrix.shape[0]
    num_train = train_matrix.shape[0]
    dists = np.zeros((num_test, num_train))
    # because(X - X_train)*(X - X_train) = -2X*X_train + X*X + X_train*X_train, so
    d1 = -2 * np.dot(test_matrix, train_matrix.T)    # shape (num_test, num_train)
    d2 = np.sum(np.square(test_matrix), axis=1, keepdims=True)    # shape (num_test, 1)
    d3 = np.sum(np.square(train_matrix), axis=1)     # shape (num_train, )
    dists = np.sqrt(d1 + d2 + d3)  # broadcasting
    return dists

print(non_loop(matrix_1, matrix_2))
"""

a = pd.DataFrame(np.array([[1, 2], [3, 4], [5, 6], [7, 8]]), columns=['x', 'y'], dtype=float)
print(a)
b = pd.DataFrame(np.array([[1, 2], [3, 4]]), columns=['x', 'y'], dtype=float)
# 不重置索引,上下拼接
print(b)
df = pd.concat([a, b], axis=0, join='inner', ignore_index=True)
# m,n = a.shape
# m0,n0 = b.shape

from sklearn.metrics.pairwise import cosine_similarity

r = cosine_similarity(a, b)
print(r)



