# -*- coding: utf8 -*-
import re
str1 = 'python_abcd'
str2 = '123asdf'
if __name__ == '__main__':
    #判断全是小写
    re_str = r'^[a-z]+$'
    print re.findall(re_str, str1)