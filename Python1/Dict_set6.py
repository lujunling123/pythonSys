# dict key value
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 替换
d['Michael']=99
# 取值1
for key in d:
    print(key,d[key])
# 取值2
print(d.get('Michael'))
# 删除
d.pop('Bob')
print(d,'\nMichael:', d['Michael'])
'''和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。'''
#set key 去重
'''set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：'''
s=set([1,2,3,3,5])
# 添加
s.add(4)
# 删除
s.remove(4)
s2=set([0,1,2,4,6,1])
print('s&s2:',s&s2,'\ns|s2:',s|s2)
print(s)

s3=['a','c','b','d']
s3.sort()
print(s3)

# 替换
a="aBC"
b=a.replace('a',"A")
print(b)