# 记事本 Unicode
# 读取转为uni|保存 转为utf-8
# 文件    utf-8
# 服务器 Unicode
#           |  输出utf-8网页
#         浏览器

#<meta charset="UTF-8" />表示该网页正是用的UTF-8编码。

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Python-中文'
print(s);
b = s.encode('utf-8');
print(b);
print(b.decode('utf-8'));
print(chr(66));
print(ord('中'));
print('亲爱的%s你好！你%d月的话费是%d，余额是%d,%s' %('admin',12,200,120,True))
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))