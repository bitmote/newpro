#coding=utf-8
import math
def convert(str):
    length = len(str)
    index = int(math.ceil(length / 2.0)) - 1
    while index > 0:
        # 截取包含ch的左边字符串与剩余字符串匹配
        if str[index + 1:].startswith(str[index::-1]):
            str1 = str[:2 * index + 1:-1]
            str = str1 + str
            return str
        # 截取不包含ch的左边字符串与不包括ch的右边剩余字符串匹配

        elif str[index + 1:].startswith(str[index - 1::-1]):
            str1 = str[:2 * index:-1]

            str = str1 + str

            return str
        else:
            index -= 1
    else:
        if str[0] != str[1]:
            str1 = str[:0:-1]
            str = str1 + str
            print str1
            return str
        else:
            return str


str=raw_input('please input the string: ')
while str:
    print '    ',convert(str)
    str = raw_input('please input the string...:')