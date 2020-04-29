import csv

csv_path = ".\\csv_test.csv"

# csv读取函数
# csv.reader(csvfile, dialect='excel', **fmtparams)
# 返回一个读取器reader对象。
# 该文件是utf-8编码，但是应该用utf-8-sig读取。如果直接用utf-8读取，会在开头出现'\ufeff'的乱码。
with open(csv_path, 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file, dialect=csv.excel)
    for row in reader:
        print('|'.join(row))

# csv写入函数
# csv.writer(csvfile, dialect='excel', **fmtparams)
# 该函数返回一个写入器writer对象。
# 如果这里的newline不设置成''，那么每次写入时在最后都会多出来一个空行。
with open(csv_path, 'a+', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Kobayashi', '24', 'Japan'])
