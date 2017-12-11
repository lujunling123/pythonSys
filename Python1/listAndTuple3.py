# 索引0开始  list
classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates),classmates[0])
# 添加 末尾append()
classmates.append('Admin')
# 添加到指定位置insert()
classmates.insert(1,"Admin")
# 删除末尾
classmates.pop()
classmates.pop(2)
# 替换
classmates[1]="Admin"
print(classmates)

# tuple 创建不可修改,但包含list时list可修改
classmates=('Michael', 'Bob', 'Tracy')
# classmates = ['Michael', 'Bob', 'Tracy']
t=(1,)# 消除数学中的运算
t = ('a', 'b', ['A', 'B'])
t[2][0]="X"
t[2][1]="Y"
print(t)
print(classmates)

