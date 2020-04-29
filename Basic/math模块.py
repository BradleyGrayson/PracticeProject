import math

# 舍入函数: math.ceil(num) & math.floor(num) & round(num)
# ceil=>天花板, floor=>地板
# ceil向上取整，floor向下取整，round四舍五入
print(math.ceil(10.2), math.ceil(10.8))     # 11, 11
print(math.floor(10.2), math.floor(10.8))   # 10, 10
print(round(10.2), round(10.8))     # 10, 11

# 幂和对数: math.pow(num, power) & math.log(num, base)
# math.pow(num, power): 返回num的power次幂
# math.log(num, base): 返回以base为底，num的对数；不指定base时为自然对数
print(math.pow(2, 3))   # 8.0
print(math.log(8, 2))   # 3.0

# 三角函数: sin(rad), cos(rad), tan(rad), ...
# 上述函数中的参数是弧度(rad)，math提供了弧度和角度(degree, X°)的转换函数
# 1 ° = π/180 rad, 1 rad = 180/π °
# 一般我们用 float * math.pi 表示弧度
# 弧度转角度：math.degrees(rad), 角度转弧度：math.radians(degree)
print(math.degrees(0.5 * math.pi))      # 90.0
print(math.radians(180 / math.pi))      # 1.0
