# w和w+都是默认创建一个新文件，如果该文件已经存在就会覆盖原文件
# w+因为是空文件，所以先写后读
with open('open_test.txt', 'w+') as file:
    file.write('w+')

# r和r+必须打开已有文件
# 'r+'如果先读，读完后光标在文件末尾，此时再写就是追加；
# 'r+'如果不读先写，则会覆盖原来的文件。
with open('open_test.txt', 'r+') as file:
    file.read()     # 该行注释和不注释时效果是不一样的
    file.write('r+')

# a没有就新建，有就操作。只能追加，不能读；
# a+与a一样，但是可以读。但此时光标在文件末尾，需要移动光标才能读。使用f.seek(num)移动光标。
with open('open_test.txt', 'a+') as file:
    file.write('a+')
    file.seek(0)
    print(file.read())

# write(str): 写入str，并返回写入的字节数
# writelines(list[str]): 逐元素写入。该方法不提供换行符，所以换行符需要自定义。
lines = ['line1', 'line2']
with open('open_test.txt', 'a+') as file:
    print(file.write(' write\n'))
    file.writelines(['line1', 'line2'])
    file.writelines(['line3\n', 'line4'])
    file.seek(0)
    print(file.read())
    # flush()用来刷新缓冲区，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，无需被动等待缓冲区写入。
    # 一般情况下，文件关闭后会自动刷新缓冲区。但有时需要在关闭前刷新，此时可以调用该方法。
    file.flush()