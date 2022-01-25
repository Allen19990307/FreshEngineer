import pandas as pa
if __name__ == '__main__':
    # eg.1 使用pandas的package,用一维数组实现
    sc = pa.Series([1,2,3,4,5,6])
    print(sc)

    # eg.2 索引进行标记
    sc = pa.Series([1,2,3,4,5,6],index = ['a','b','c','d','e','f'])
    print(sc)