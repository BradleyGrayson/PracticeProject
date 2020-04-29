import datetime

# datetime类，表示日期和时间等信息
# datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
# 其中hour, minute, second, microsecond均是从0开始计算
print(datetime.datetime(2020, 4, 7))
print(datetime.datetime.today())    # 返回当前本地日期和时间
print(datetime.datetime.now())      # 如果参数tz为None或未指定，等同于today()
print(datetime.datetime.utcnow())   # 返回当前UTC日期和时间

# date类，表示日期等信息
# datetime.date(year, month, day)
print(datetime.date(2020, 4, 7))
print(datetime.date.today())

# time类，表示一天中的时间信息
# datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
print(datetime.time())
# time类没有类似now()的构造方法

# timedelta类：用于计算datetime, date, time对象的时间间隔
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
# 上述所有参数都是可选的，可为正数或负数
today = datetime.datetime.today()
delta_1 = datetime.timedelta(weeks=1)   # 改变一周（后）
delta_2 = datetime.timedelta(days=-5)   # 改变五天（前）
print("目前时间:", today)
print("一周后:", today + delta_1)
print("一周前:", today - delta_1)
print("五天前(加负数):", today + delta_2)
print("五天后(减负数):", today - delta_2)

# 日期时间格式化解析方法——strftime(format) & strptime(str_date, format)
# 格式化方法（类到字符串）：
# datetime, date, time类各有一个strftime(format)方法，换言之strftime必须作用于上述三个类中
now = datetime.datetime.now()
print("格式化为字符串后:", now.strftime("Now is %Y-%m-%d, %H:%m"))  # strftime中的format不要使用中文
# 解析方法（字符串到类）：
# 使用datetime.datetime.strptime(str_date, format)类方法，其返回一个datetime类。
# date和time类没有strptime方法
str_now = "Year2017, Month04, Day7, Time11:13"
cls_now = datetime.datetime.strptime(str_now, "Year%Y, Month%m, Day%d, Time%H:%M")
print("解析后:", type(cls_now), cls_now)