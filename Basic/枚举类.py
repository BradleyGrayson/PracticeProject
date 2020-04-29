# 枚举类可以看作是一组常数的集合，使用枚举类来使程序更清晰和易于维护
# 使用枚举类需要导入enum模块
import enum


# 枚举类继承自enum.Enum类
class JPWeekdays(enum.Enum):
    # 枚举常量列表
    MONDAY = 'げつようび'
    TUESDAY = 'かようび'
    WEDNESDAY = 'すいようび'
    THURSDAY = 'もくようび'
    FRIDAY = 'きんようび'
    SATURDAY = 'どようび'
    SUNDAY = 'にちようび'


# 为了使用方便，枚举类中的常量成员取值应是整数，而且每一个常量成员应该有不同的取值。
# 为了使枚举类常量成员只能使用整数类型，可以使用enum.IntEnum作为父类。
# 为了防止常量成员重复，可以为枚举类加上@enum.unique装饰器。
@enum.unique
class NumWeekDays(enum.IntEnum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


today_jp = JPWeekdays.SATURDAY
today = NumWeekDays.SATURDAY
# 枚举类的调用方法如下，name返回枚举名，value返回枚举值
print(today_jp, today_jp.name, today_jp.value, sep='    ')
print(today, today.name, today.value, sep='    ')


# 枚举类主要是为了提高代码的可读性
# 尤其是在比较时，枚举类非常实用
# 比如要判断明天是否是周日：
if today == NumWeekDays.SATURDAY or today == NumWeekDays.SUNDAY:
    print('Play')
# 可以发现，使用枚举类成员比使用无意义的数字更易读。
