import collections

#collections.OrderedDict
odict = collections.OrderedDict()
odict['one'] = 1
odict['two'] = 2
odict['three'] = 3
print (odict)

#collections.Counter
ct = collections.Counter("abracadabra")
print (ct)
ct.update('aaaaaaazzz')
print (ct)
print (ct.most_common(2))

#collections.UserDict
class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


str_key_dict = StrKeyDict()
str_key_dict['1'] = 1
print (str_key_dict)

#MappingProxyType
from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
print (d_proxy)
try:
    d_proxy[2] = 'X'
except TypeError:
    print ('Unable to change the dict')
d[2] = 'X'
print (d)

