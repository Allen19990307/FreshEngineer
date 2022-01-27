import os,shutil
if __name__ == '__main__':
    """使用python进行数据的下载和导入，发现核心价值的数据"""
    # with open('Resource/siddhartha.txt','r') as f:
    #     for i in f.readlines():
    #         print(i.strip())

    # with open('Resource/WealthFree.txt','a') as w:
    #     w.write('\nTake 10 min to imagine you have done what you want.')

    # 文件的创建等操作  C:\Users\Allen\Desktop\web_crawler
    """注意这边的反斜杠的转换操作,单个反斜杠在字符串中用\\表示"""
    # getcwd = os.getcwd()
    # print(getcwd)
    # listdir = os.listdir('C:\\Users\\Allen\\Desktop\\web_crawler')
    # print(listdir)
    # os.remove('C:\\Users\\Allen\\Desktop\\web_crawler\\s1\\s1.txt')
    # crawler = 'C:\Users\Allen\Desktop\web_crawler\s1'
    # s1 = crawler.replace("\\","\\\\")
    os.removedirs('C:\\Users\\Allen\\Desktop\\web_crawler\\s1')