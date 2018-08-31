def printt():
    print('Executing')
    x = yield
    print('Executed %s' % x)


c = printt()
next(c)
c.send(12)
