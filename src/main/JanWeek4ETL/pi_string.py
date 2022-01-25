filename = 'Resource/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
s = input("please input your birthday,in the form mmddyy: ")
"""判断自己的名字是否在圆周率的52位数中"""
if s in pi_string:
    print("Your birthday appears in the first million digits of it.")
else:
    print("Your birthday does not appear in the first million digits of it.")
print(f"{pi_string[:52]}")
print(len(pi_string))
