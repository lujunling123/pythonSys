a = ['Michael', 'Bob', 'Tracy']
for name in range(10):
    a.append(name)
print(a)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
print("End")

n2 = 1
while n2 <= 10:
    if n2 > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n2)
    n2 = n2 + 1
print('END')