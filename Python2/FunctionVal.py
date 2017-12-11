import math
def power(x):
    return math.sqrt(x)
print(power(2))

def power2(x, n):
    if not isinstance(x, (int)):
        raise TypeError('bad operand type');
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power2(2,3))

def enroll(name, gender, city='beijing'):
    return ('name:%s'%name+'\ngender:%s'%gender+'\ncity:%s'%city)
print(enroll('admin','F'))
print(enroll('admin','F',city='wuhan'))

def add_end(a):
    a.append('End')
    return a
s=[1,2,3]
print(add_end(s))
print(add_end([]))

def add_end2(a=None):
    if a is None:
        a = []
    a.append('End')
    return a
print(add_end2())

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 3, 5, 7))
# 传入可变的参数,list或tuple参数
nums = [1, 2, 3]
print(calc(*nums))

# 关键字参数
def person (name, age, **kw):
    print('name:',name,'age:',age,'other:',kw)
person('admin',12,city='hubei',job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack',18,city=extra['city'],job=extra['job'])

# 检查关键字参数
def person2 (name,age,**kw):
    if('city'in kw):
        pass
    if('job' in kw):
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person2('Makc', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
f1(1, 2, 3, 'a', 'b', x=99)





