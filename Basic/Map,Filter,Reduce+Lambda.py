# lambda x: x * 2 equals
# def anomaly(x):
#     return x * 2

"""# ##############################   MAP   ####################################
# #####################   使用map将所有元素变为两倍   ########################
# ####################   map: 对列表元素依次执行函数   #######################
to_be_mapped = [1, 2, 3, 4, 5]

# Method 1: Use Lambda
mapped = map(lambda x: x * 2, to_be_mapped)

# Method 2: Use Function
# def double_elem(x):
#     return x
# map_list = map(double_elem, origin_list)

for i in mapped:
    print(i)
# #############################   END LINE   ####################################"""

"""# ##############################   FILTER   ####################################
# ##################   Filter: 返回执行结果为True的入参   #######################
to_be_filtered = [1, 10, 2, 9, 3, 8, 4, 6, 5]

# 1: 找出所有大于5的参数
filtered = filter(lambda x: x > 5, to_be_filtered)

# 2: 找出所有偶数
filtered = filter(lambda x: x % 2 == 0, to_be_filtered)

# 3: 找出所有奇数
filtered = filter(lambda x: x % 2, to_be_filtered)

for i in filtered:
    print(i)
# #############################   END LINE   ####################################"""

"""# ############################   REDUCE   ##################################
# #########################   Reduce: 累积   ###############################
# ##  Reduce将1、2元素相计算，得出的结果与3计算，得出的结果与4计算，以此类推  ##
from functools import reduce        # Python3中已没有该内置函数，需要导入
to_be_reduced = range(10, 0, -1)    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 1: 求和
reduced = reduce(lambda x, y: x + y, to_be_reduced)
print(reduced)

# 1.1: 求和。 reduce可以接收第三个参数，使其从该参数开始运算
# 这里设置第三个参数为100，表示从100开始累加，即 100 + 10 + 9 + ... + 1
reduced = reduce(lambda x, y: x + y, to_be_reduced, 100)
print(reduced)

# 2: 求积
reduced = reduce(lambda x, y: x * y, to_be_reduced)
print(reduced)

# 3: 转换成string直接连接
reduced = reduce(lambda x, y: str(x)+str(y), to_be_reduced)
print(reduced)
# #############################   END LINE   ####################################"""
