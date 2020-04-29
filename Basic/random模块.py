import random

# random生成随机数
# random.random(): 返回[0.0, 1.0]之间的随机浮点数
print(random.random())      # 该函数没有入参

# random.randrange(start, stop, step): 返回[start, stop)之间步长为step的随机整数
print(random.randrange(10, 100, 2))     # 生成[10, 100)之间的随机偶数
print(random.randrange(10, 100, 3))
# 第9行生成了76，不能被3整除，为什么呢？因为76-10=66能被3整除。
# 同样的，第8行生成90也是因为90-10=80能被2整除。

# random.randrange(stop): 和上面一样，只不过只赋予了stop参数，此时返回[0, stop)之间步长为1的随机整数
print(random.randrange(5))

# random.randint(start, stop): 返回[start, stop]之间的随机整数
print(random.randint(0, 1))     # 生成0或1

# random.uniform(start, stop): 返回[start, stop)之间的随机浮点数, start和stop可以是浮点数
print(random.uniform(1.1, 1.2))

# random.choice(str/tuple/list): 返回对象中的随机一个元素
print(random.choice('abcdefg'))
print(random.choice((1, 2, 3)))
print(random.choice([4, 5, 6]))