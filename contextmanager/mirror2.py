import contextlib

@contextlib.contextmanager
def lookging_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])


    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'Please, don\'t divide on zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)

with lookging_glass() as s:
    print('ABC')
    print(s)
