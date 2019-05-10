import re

import pandas as pd
import numpy as np
from blaze.tests.test_cached import df
from distributed.counter import Counter
from pandas import Series, DataFrame
import xlrd
from pyecharts.charts import Bar
from pyecharts import options as opts

"""
create by XuChao on 2019/5/10
"""

#进行数据清理和获取数据
def load_data(filename):
    df = pd.read_excel(filename)
    return df



if __name__ == "__main__":

    # load_data("E:/PythonPractice/LaGou/lagou_py.xls")
    # load_data("E:/PythonPractice/LaGou/lagou_java.xls")
    # 显示excel的数据shape
    # print(df.shape)
    # 显示各列数据的数据类型
    # print(df.dtypes)
    # 读取后五行数据
    # print(df.tail(5))
    # 数据清洗 删除空格
    # df.dropna(how='any')

    df = pd.read_excel("E:/PythonPractice/LaGou/lagou_py.xls")
    # df = pd.read_excel("E:/PythonPractice/LaGou/lagou_java.xls")
    # 获取数据使用 分开获取
    # dazhuan = df.groupby(['学历要求']).size()['大专']
    # benke = df.groupby(['学历要求']).size()['本科']
    # shuoshi = df.groupby(['学历要求']).size()['硕士']
    # buxian = df.groupby(['学历要求']).size()['不限']
    # 整体获取
    # 不限
    # 15
    # 大专
    # 44
    # 本科
    # 239
    # 硕士
    # 2
    # 上面为结果
    # rows = df.groupby([' ']).size()
    # print(dazhuan)
    # print(benke)
    # print(shuoshi)
    # print(buxian)
    #py
    # num_people_py = [37, 240, 1, 22]
    # # java
    # num_people_java = [44,239,2,15]
    # degree = ['大专', '本科', '硕士', '不限']



    # 9
    # 29
    # 33
    # 71
    # 111
    # 47

    # 处理工资数据  上边为py结果
    dazhuan = df.groupby(['薪资']).size()
    print(dazhuan)
    # 取得每个薪资范围的平均值
    df = df['薪资'].str.split('-').map(lambda x: np.median((int(re.findall('\d+', x[0])[0]), int(re.findall('\d+', x[1])[0]))))
    sal1 = np.array(df)
    # sal = sal1.astype(int)
    sal = np.sort(sal1)
    print(len(sal[[sal < 6]]))
    print(len(sal[(sal < 11) & (sal >= 6)]))
    print(len(sal[(sal < 15) & (sal >= 11)]))
    print(len(sal[(sal < 20) & (sal >= 15)]))
    print(len(sal[(sal < 30) & (sal >= 20)]))
    print(len(sal[sal >=30]))






