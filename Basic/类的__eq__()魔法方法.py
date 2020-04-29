# 在比较实例时，会默认调用__eq__()方法。
# 由于__eq__()方法是没有默认定义的，因此我们需要重新定义该方法以达到比较目的。
# 我们可以指定两个实例相等的条件：
# 比如两个人名字和年龄相同时我们认为这两个人是相等的。


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Person类没有定义__eq__()方法，其默认返回False
wang = Person('wang', 12)
wang2 = Person('wang', 12)
print(wang == wang2)


class Person2(Person):
    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False


# 这里的Person2重写了__eq__()方法，因此返回True
wang = Person2('wang', 12)
wang2 = Person2('wang', 12)
print(wang == wang2)