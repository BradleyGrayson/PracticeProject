import configparser


def parse_demo():
    """使用ConfigParser读取配置文件
    """
    # 创建配置解析器对象
    config = configparser.ConfigParser()

    # 读取并解析配置文件
    # 指定读取文件字符集为utf-8。如果文件中有中文，必须正确指定字符集，否则会有解析错误。
    config.read('.\\setup.ini', encoding='utf-8')

    # 返回所有的节
    print(config.sections())        # ['StartUp', 'Product', 'Windows 10']

    # 返回StartUp节
    section1 = config['StartUp']
    # 返回StartUp节中所有配置项
    print(config.options('StartUp'))    # ['requireos', 'requiremsi', 'requireie']
    # 读取StartUp节中配置项RequireOS键对应的值
    print(section1['RequireOS'])        # Windows 10
    print(section1['RequireIE'])        # 6.0.2600.0

    print(config['Product']['msi'])     # AcroRead.msi

    # 返回MajorVersion数据
    print(config['Windows 10']['MajorVersion'])     # <class 'str'>

    # 返回MajorVersion数据，get()返回字符串
    value = config.get('Windows 10', 'MajorVersion')
    print(type(value), value)   # <class 'str'> 5

    # 返回MajorVersion数据，getint()返回整数类型
    value = config.getint('Windows 10', 'MajorVersion')
    print(type(value), value)   # <class 'int'> 5

    # 类似的还有getfloat(), getboolean()方法，分别返回浮点数和布尔类型数据。


def write_demo():
    # 此处与读取是相同的
    config = configparser.ConfigParser()
    config.read('.\\setup.ini', encoding='utf-8')

    # 修改节的配置项
    config['StartUp']['RequireMSI'] = '8.0'
    config['Product']['RequireMSI'] = '4.0'

    # 添加节
    config.add_section('Add_section')
    # 添加配置项,参数从左到右为: 添加的目的节名; 新配置项的键; 新配置项的值
    config.set('Add_section', 'name', 'Mac')

    # 将修改后的配置文件写入原文件
    with open('.\\setup.ini', 'w') as file:
        config.write(file)


parse_demo()
# write_demo()
