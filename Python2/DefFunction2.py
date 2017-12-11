import math

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-3));

# pass空函数:还没想好怎么写函数的代码,可以先放一个pass，让代码能运行起来。
def nop():
    pass

#允许整数和浮点数类型的参数,检查可以用内置函数isinstance()
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type');
    if x>=0:
        return x
    else:
        return -x
print(my_abs2(1));

# 返回多个值
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
print(move(100,100,60,math.pi/6))

# math.sqrt()平方根
print(math.sqrt(2))