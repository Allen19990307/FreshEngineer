"""计算除法"""
    # print("Give me two numbers.")
    # print("Enter q to quit.")
    # while True:
    #     s = input("the first number:")
    #     if s == 'q':
    #         break
    #     s1 = input("the second number:")
    #     if s1 == 'q':
    #         break
    #     try:
    #         count = float(s) / float(s1)
    #     except ZeroDivisionError:
    #         print("I can not deal with the 0 as division.")
    #     else:
    #         print(count)

    #eg1 读取文件
# try:
#    with open('Resource/reason_record.txt',encoding='utf-8')  as open_object:
#        read = open_object.read()
# except FileNotFoundError:
#         print("your file doesn't exist")

"""计算爱丽丝梦游仙境究竟有多少单词"""
filename  = 'Resource/little_women.txt'
def word_count(filename):
    try:
        with open(filename,encoding = 'utf-8') as f:
            read = f.read()
    except:
        print(f"Sorry,the file {filename} does not exist.")
    else:
        words = read.split()
        i = len(words)
        print(f"{filename} has about {i} words")
word_count(filename)


