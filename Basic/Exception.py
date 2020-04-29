import datetime
import traceback


def read_date(in_date):
    try:
        res = datetime.datetime.strptime(in_date, "%Y-%m-%d %H:%M:%S")
        print(res)
    except ValueError as e:
        print('ValueError:', e)
        traceback.print_exc()


class MyException(Exception):
    def __init__(self, message):
        super.__init__(message)


read_date("2020-04-06 12:17:05")
read_date("20-04-06 12:17:05")