def get_formatted_name(first,last,middle =''):
    """生成简洁的姓名"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


    #octopus,在实际的开发中使用的设备管理系统