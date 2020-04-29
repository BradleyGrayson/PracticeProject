from time import localtime, sleep
from abc import abstractclassmethod, ABCMeta


# __slots__、@property（访问器）、@属性名.setter（修改器）
class Person:
    # __slots__可以对类的属性进行限定，除这些属性以外，不能添加其他属性
    # 但是注意，在属性未被声明时对其进行引用会报AttributeError
    # 此外，对该类属性的限定不会影响其子类
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property  # 访问器，方法名不具有特殊要求
    def name(self):
        return self._name

    @property  # 访问器
    def age(self):
        return self._name

    @age.setter  # 修改器，方法名必须与属性名相同
    def age(self, age):
        self._age = age

    #
    # @name.setter
    # def name(self, name):
    #     self._name = name

    def play(self):
        if self._age < 16:
            print('{}{}岁，正在玩飞行棋'.format(self._name, self._age))
        else:
            print('{}{}岁，正在玩斗地主'.format(self._name, self._age))


# a = Person('a', 16)
# a.play()
# a.age = 25
# a._gender = 'male'
# a.name = 'b'  # AttributeError，因为没有为属性name设置修改器

# 静态方法
class Triangle:
    __slots__ = ('_a', '_b', '_c')

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def circumference(self):
        return self._a + self._b + self._c


# # 使用静态方法，就可以在没有实例化类时调用该方法
# if Triangle.is_triangle(3, 4, 5):
#     triangle = Triangle(3, 4, 5)
#     # 三种调用方法
#     print(triangle.circumference())
#     print(Triangle.circumference(triangle))
#     print(Triangle.circumference(Triangle(3, 4, 5)))

# 类方法
class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ct = localtime()
        return cls(ct.tm_hour, ct.tm_min, ct.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


# # 使用类方法创建当前时间的Clock对象
# clock = Clock.now()
# while True:
#     print(clock.show())
#     sleep(1)
#     clock.run()

# Student是Person的子类，Student继承了Person的属性
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self):
        print('{}岁上{}年级的{}正在学习'.format(self._age, self._grade, self._name))


# Teacher是Person的子类，Teacher继承了Person的属性
# 在Teacher中，我们重写(override)了Person的play()方法
class Teacher(Person):
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self):
        print('{}岁的{}老师{}正在上课'.format(self._age, self._title, self._name))

    def play(self):
        print('is playing card')


# student = Student('student', 14, 8)
# teacher = Teacher('teacher', 35, '数学')
# student.study()
# teacher.teach()
# student.play()
# teacher.play()

# 一个抽象类，抽象类不能实例化，抽象类的作用就是专门作为其他类的父类
# 在下面的Pet类中，经过测试，
# 只有ABCMeta和abstractclassmethod同时存在才不能被实例化
# 只要二者有一个不存在就可以实例化Pet
class Pet(metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractclassmethod
    def make_noise(self):
        """发出声音"""
        pass


class Dog(Pet):
    def __init__(self, nickname):
        super().__init__(nickname)

    def make_noise(self):
        print('汪汪汪')


class Cat(Pet):
    def __init__(self, nickname):
        super().__init__(nickname)

    def make_noise(self):
        print('喵喵喵')


dog = Dog('大黄')
cat = Cat('小咪')
dog.make_noise()
cat.make_noise()