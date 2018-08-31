def log(func):
    def arg(*args):
        print('Start')
        result = func(args)
        print('Stop')

    return arg


@log
def func(num):
    print('%s' % num)


func(123)
