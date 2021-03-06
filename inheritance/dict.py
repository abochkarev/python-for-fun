import collections


class AnwerDict(dict):
    def __getitem__(self, key):
        return 32


class DoppelDict2(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, [value] * 2)


if __name__ == '__main__':
    print('Answer dict == wrong behavior')
    ad = AnwerDict(a='foo')
    print(ad['a'])

    d = {}
    d.update(ad)
    print(d['a'])

    print(d)
    print('Doppel dict == right behavior')

    dd = DoppelDict2(one=1)
    print(dd)

    dd['two'] = 2
    print(dd)

    dd.update(three=3)
    print(dd)
